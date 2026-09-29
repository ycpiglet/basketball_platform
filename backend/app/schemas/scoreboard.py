from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from app.services.scoreboard_state import (
    DEFAULT_QUARTER_SECONDS,
    ClockStatus,
    GameStatus,
    ScoreboardEventLogEntry,
    ScoreboardEventType,
    ScoreboardState,
    TeamSide,
)


class CreateScoreboardGameRequest(BaseModel):
    """Request body for creating a pilot scoreboard game."""

    game_id: str | None = Field(default=None, min_length=1, max_length=120)


class AddPointsRequest(BaseModel):
    """Request body for recording player points."""

    team: TeamSide
    player_id: str = Field(min_length=1, max_length=120)
    points: int = Field(ge=1, le=3)


class CorrectScoreRequest(BaseModel):
    """Request body for auditable score correction."""

    team: TeamSide
    corrected_score: int = Field(ge=0)
    reason: str = Field(min_length=1, max_length=500)


class TeamActionRequest(BaseModel):
    """Request body for a team-scoped scoreboard action."""

    team: TeamSide


class PlayerFoulRequest(BaseModel):
    """Request body for recording a player foul."""

    team: TeamSide
    player_id: str = Field(min_length=1, max_length=120)


class SetQuarterRequest(BaseModel):
    """Request body for setting quarter and game clock."""

    quarter: int = Field(ge=1)
    remaining_seconds: int = Field(default=DEFAULT_QUARTER_SECONDS, ge=0)


class StopClockRequest(BaseModel):
    """Request body for stopping the game clock at a known remaining time."""

    remaining_seconds: int = Field(ge=0)


class GameClockResponse(BaseModel):
    """Serialized public game clock state."""

    quarter: int
    remaining_seconds: int
    status: ClockStatus


class TeamScoreboardResponse(BaseModel):
    """Serialized public team scoreboard values."""

    score: int
    team_fouls: int
    timeouts_remaining: int


class PlayerStatResponse(BaseModel):
    """Serialized player box-score line for the pilot scoreboard state."""

    player_id: str
    points: int
    fouls: int


class ScoreboardEventResponse(BaseModel):
    """Serialized scoreboard event log entry."""

    sequence: int
    event_type: ScoreboardEventType
    occurred_at: datetime
    summary: str
    payload: dict[str, Any]


class ScoreboardStateResponse(BaseModel):
    """Serialized scoreboard state shared by control, display, and result views."""

    game_id: str
    game_status: GameStatus
    clock: GameClockResponse
    home: TeamScoreboardResponse
    away: TeamScoreboardResponse
    player_stats: list[PlayerStatResponse]
    event_log: list[ScoreboardEventResponse]


def scoreboard_state_to_response(state: ScoreboardState) -> ScoreboardStateResponse:
    """Convert the deterministic service state into an API response model."""

    return ScoreboardStateResponse(
        game_id=state.game_id,
        game_status=state.game_status,
        clock=GameClockResponse(
            quarter=state.clock.quarter,
            remaining_seconds=state.clock.remaining_seconds,
            status=state.clock.status,
        ),
        home=TeamScoreboardResponse(
            score=state.home_score,
            team_fouls=state.team_fouls[TeamSide.HOME],
            timeouts_remaining=state.timeouts_remaining[TeamSide.HOME],
        ),
        away=TeamScoreboardResponse(
            score=state.away_score,
            team_fouls=state.team_fouls[TeamSide.AWAY],
            timeouts_remaining=state.timeouts_remaining[TeamSide.AWAY],
        ),
        player_stats=[
            PlayerStatResponse(player_id=player_id, points=stats.points, fouls=stats.fouls)
            for player_id, stats in sorted(state.player_stats.items())
        ],
        event_log=[_event_to_response(event) for event in state.event_log],
    )


def _event_to_response(event: ScoreboardEventLogEntry) -> ScoreboardEventResponse:
    return ScoreboardEventResponse(
        sequence=event.sequence,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        summary=event.summary,
        payload=event.payload,
    )
