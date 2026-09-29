import logging
from collections.abc import Callable
from dataclasses import dataclass
from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.core.config import get_settings
from app.core.logging import log_structured_event
from app.core.rbac import Role, has_minimum_role
from app.schemas.scoreboard import (
    AddPointsRequest,
    CorrectScoreRequest,
    CreateScoreboardGameRequest,
    PlayerFoulRequest,
    ScoreboardStateResponse,
    SetQuarterRequest,
    StopClockRequest,
    TeamActionRequest,
    scoreboard_state_to_response,
)
from app.services.scoreboard_state import (
    ScoreboardState,
    ScoreboardStateService,
    ScoreboardValidationError,
)
from app.services.scoreboard_store import (
    InMemoryScoreboardStore,
    ScoreboardGameConflictError,
    ScoreboardGameNotFoundError,
)

router = APIRouter(prefix="/scoreboard", tags=["scoreboard"])
logger = logging.getLogger(__name__)
scoreboard_service = ScoreboardStateService()
pilot_scoreboard_store = InMemoryScoreboardStore(scoreboard_service)


@dataclass(frozen=True, slots=True)
class ScoreboardActor:
    """Pilot actor context derived from request headers until production auth exists."""

    role: Role
    user_id: str | None
    request_id: str | None


# x-user-role is client-supplied, so honouring it lets any caller claim
# system_admin and rewrite scores. It is a stand-in until production auth exists,
# so it is accepted only while running locally; any other app_env refuses rather
# than authorize a scoreboard change on an unverified header.
_HEADER_ROLE_ENVS = frozenset({"local", "test"})


def get_scoreboard_actor(request: Request) -> ScoreboardActor:
    """Read the pilot actor role and user id from request headers."""

    if get_settings().app_env not in _HEADER_ROLE_ENVS:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail="Header-based scoreboard roles are only available in local development.",
        )

    role_value = request.headers.get("x-user-role", Role.GUEST.value)
    try:
        role = Role(role_value)
    except ValueError as exc:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail="Invalid x-user-role header.",
        ) from exc

    return ScoreboardActor(
        role=role,
        user_id=request.headers.get("x-user-id"),
        request_id=getattr(request.state, "request_id", None),
    )


def require_scoreboard_operator(
    actor: Annotated[ScoreboardActor, Depends(get_scoreboard_actor)],
) -> ScoreboardActor:
    """Require a pilot operator role for state-changing scoreboard endpoints."""

    if not has_minimum_role(actor.role, Role.TEAM_MANAGER):
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail="Scoreboard changes require team_manager or system_admin role.",
        )
    return actor


ScoreboardOperator = Annotated[ScoreboardActor, Depends(require_scoreboard_operator)]


@router.post(
    "/games",
    response_model=ScoreboardStateResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_scoreboard_game(
    payload: CreateScoreboardGameRequest,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Create a pilot scoreboard game."""

    try:
        state = pilot_scoreboard_store.create_game(payload.game_id)
    except ScoreboardGameConflictError as exc:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail=str(exc)) from exc

    log_structured_event(
        logger,
        action="scoreboard_game_created",
        result="success",
        request_id=actor.request_id,
        user_id=actor.user_id,
        role=actor.role.value,
        target_entity_type="scoreboard_game",
        target_entity_id=state.game_id,
    )
    return scoreboard_state_to_response(state)


@router.get("/games/{game_id}", response_model=ScoreboardStateResponse)
def get_scoreboard_game(game_id: str) -> ScoreboardStateResponse:
    """Return public scoreboard state for control, display, and result views."""

    return scoreboard_state_to_response(_get_game_or_404(game_id))


@router.post("/games/{game_id}/points", response_model=ScoreboardStateResponse)
def add_points(
    game_id: str,
    payload: AddPointsRequest,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Record a 1, 2, or 3 point scoring event."""

    return _mutate_game_or_error(
        game_id,
        lambda state: scoreboard_service.add_points(
            state,
            payload.team,
            payload.player_id,
            payload.points,
            actor_user_id=actor.user_id,
        ),
        actor=actor,
        api_action="scoreboard_points_added",
    )


@router.post("/games/{game_id}/score-corrections", response_model=ScoreboardStateResponse)
def correct_score(
    game_id: str,
    payload: CorrectScoreRequest,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Correct a team score with an auditable reason."""

    return _mutate_game_or_error(
        game_id,
        lambda state: scoreboard_service.correct_score(
            state,
            payload.team,
            payload.corrected_score,
            payload.reason,
            actor_user_id=actor.user_id,
        ),
        actor=actor,
        api_action="scoreboard_score_corrected",
    )


@router.post("/games/{game_id}/team-fouls", response_model=ScoreboardStateResponse)
def add_team_foul(
    game_id: str,
    payload: TeamActionRequest,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Record a team foul."""

    return _mutate_game_or_error(
        game_id,
        lambda state: scoreboard_service.add_team_foul(
            state,
            payload.team,
            actor_user_id=actor.user_id,
        ),
        actor=actor,
        api_action="scoreboard_team_foul_added",
    )


@router.post("/games/{game_id}/player-fouls", response_model=ScoreboardStateResponse)
def add_player_foul(
    game_id: str,
    payload: PlayerFoulRequest,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Record a player foul and the related team foul."""

    return _mutate_game_or_error(
        game_id,
        lambda state: scoreboard_service.add_player_foul(
            state,
            payload.team,
            payload.player_id,
            actor_user_id=actor.user_id,
        ),
        actor=actor,
        api_action="scoreboard_player_foul_added",
    )


@router.post("/games/{game_id}/quarters", response_model=ScoreboardStateResponse)
def set_quarter(
    game_id: str,
    payload: SetQuarterRequest,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Set the active quarter and remaining game time."""

    return _mutate_game_or_error(
        game_id,
        lambda state: scoreboard_service.set_quarter(
            state,
            payload.quarter,
            payload.remaining_seconds,
            actor_user_id=actor.user_id,
        ),
        actor=actor,
        api_action="scoreboard_quarter_set",
    )


@router.post("/games/{game_id}/timeouts", response_model=ScoreboardStateResponse)
def use_timeout(
    game_id: str,
    payload: TeamActionRequest,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Use one team timeout."""

    return _mutate_game_or_error(
        game_id,
        lambda state: scoreboard_service.use_timeout(
            state,
            payload.team,
            actor_user_id=actor.user_id,
        ),
        actor=actor,
        api_action="scoreboard_timeout_used",
    )


@router.post("/games/{game_id}/clock/start", response_model=ScoreboardStateResponse)
def start_clock(
    game_id: str,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Start the game clock."""

    return _mutate_game_or_error(
        game_id,
        lambda state: scoreboard_service.start_clock(state, actor_user_id=actor.user_id),
        actor=actor,
        api_action="scoreboard_clock_started",
    )


@router.post("/games/{game_id}/clock/stop", response_model=ScoreboardStateResponse)
def stop_clock(
    game_id: str,
    payload: StopClockRequest,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Stop the game clock and record the current remaining time."""

    return _mutate_game_or_error(
        game_id,
        lambda state: scoreboard_service.stop_clock(
            state,
            payload.remaining_seconds,
            actor_user_id=actor.user_id,
        ),
        actor=actor,
        api_action="scoreboard_clock_stopped",
    )


@router.post("/games/{game_id}/finalize", response_model=ScoreboardStateResponse)
def finalize_game(
    game_id: str,
    actor: ScoreboardOperator,
) -> ScoreboardStateResponse:
    """Finalize the pilot game and reject future mutations."""

    return _mutate_game_or_error(
        game_id,
        lambda state: scoreboard_service.end_game(state, actor_user_id=actor.user_id),
        actor=actor,
        api_action="scoreboard_game_finalized",
    )


def _get_game_or_404(game_id: str) -> ScoreboardState:
    try:
        return pilot_scoreboard_store.get_game(game_id)
    except ScoreboardGameNotFoundError as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(exc)) from exc


def _mutate_game_or_error(
    game_id: str,
    operation: Callable[[ScoreboardState], ScoreboardState],
    actor: ScoreboardActor,
    api_action: str,
) -> ScoreboardStateResponse:
    try:
        state = pilot_scoreboard_store.mutate_game(game_id, operation)
    except ScoreboardGameNotFoundError as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=str(exc)) from exc
    except ScoreboardValidationError as exc:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(exc)) from exc

    log_structured_event(
        logger,
        action=api_action,
        result="success",
        request_id=actor.request_id,
        user_id=actor.user_id,
        role=actor.role.value,
        target_entity_type="scoreboard_game",
        target_entity_id=game_id,
    )
    return scoreboard_state_to_response(state)
