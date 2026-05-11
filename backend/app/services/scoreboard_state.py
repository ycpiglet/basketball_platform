from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from app.core.logging import log_structured_event

logger = logging.getLogger(__name__)

VALID_SCORING_VALUES = {1, 2, 3}
DEFAULT_TIMEOUTS_PER_TEAM = 5
DEFAULT_QUARTER_SECONDS = 10 * 60


class ScoreboardValidationError(ValueError):
    """Raised when a scoreboard operation would create invalid game state."""


class TeamSide(StrEnum):
    HOME = "home"
    AWAY = "away"


class ClockStatus(StrEnum):
    STOPPED = "stopped"
    RUNNING = "running"


class GameStatus(StrEnum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    FINAL = "final"


class ScoreboardEventType(StrEnum):
    SCORE_ADDED = "score_added"
    SCORE_CORRECTED = "score_corrected"
    TEAM_FOUL_ADDED = "team_foul_added"
    PLAYER_FOUL_ADDED = "player_foul_added"
    TIMEOUT_USED = "timeout_used"
    CLOCK_STARTED = "clock_started"
    CLOCK_STOPPED = "clock_stopped"
    QUARTER_SET = "quarter_set"
    GAME_ENDED = "game_ended"


@dataclass(slots=True)
class GameClockState:
    quarter: int = 1
    remaining_seconds: int = DEFAULT_QUARTER_SECONDS
    status: ClockStatus = ClockStatus.STOPPED


@dataclass(slots=True)
class PlayerStatLine:
    points: int = 0
    fouls: int = 0


@dataclass(slots=True)
class ScoreboardEventLogEntry:
    sequence: int
    event_type: ScoreboardEventType
    occurred_at: datetime
    summary: str
    payload: dict[str, Any]


@dataclass(slots=True)
class ScoreboardState:
    game_id: str
    home_score: int = 0
    away_score: int = 0
    clock: GameClockState = field(default_factory=GameClockState)
    team_fouls: dict[TeamSide, int] = field(
        default_factory=lambda: {TeamSide.HOME: 0, TeamSide.AWAY: 0}
    )
    timeouts_remaining: dict[TeamSide, int] = field(
        default_factory=lambda: {
            TeamSide.HOME: DEFAULT_TIMEOUTS_PER_TEAM,
            TeamSide.AWAY: DEFAULT_TIMEOUTS_PER_TEAM,
        }
    )
    player_stats: dict[str, PlayerStatLine] = field(default_factory=dict)
    game_status: GameStatus = GameStatus.NOT_STARTED
    event_log: list[ScoreboardEventLogEntry] = field(default_factory=list)

    @property
    def quarter(self) -> int:
        return self.clock.quarter


class ScoreboardStateService:
    """Pure MVP scoreboard state rules, isolated from UI, database, and hardware control."""

    def create_game(self, game_id: str | None = None) -> ScoreboardState:
        return ScoreboardState(game_id=game_id or str(uuid4()))

    def add_points(
        self,
        state: ScoreboardState,
        team: TeamSide,
        player_id: str,
        points: int,
        actor_user_id: str | None = None,
    ) -> ScoreboardState:
        self._ensure_mutable_game(state)
        if points not in VALID_SCORING_VALUES:
            raise ScoreboardValidationError("Scoring updates must be 1, 2, or 3 points.")

        before = self._state_summary(state)
        if team is TeamSide.HOME:
            state.home_score += points
        else:
            state.away_score += points

        player_stats = self._player_stats(state, player_id)
        player_stats.points += points
        state.game_status = GameStatus.IN_PROGRESS

        self._record_change(
            state,
            ScoreboardEventType.SCORE_ADDED,
            f"Added {points} point(s) for {team.value}.",
            actor_user_id=actor_user_id,
            before_state=before,
            payload={"team": team.value, "player_id": player_id, "points": points},
        )
        return state

    def correct_score(
        self,
        state: ScoreboardState,
        team: TeamSide,
        corrected_score: int,
        reason: str,
        actor_user_id: str | None = None,
    ) -> ScoreboardState:
        self._ensure_mutable_game(state)
        if corrected_score < 0:
            raise ScoreboardValidationError("Corrected score cannot be negative.")
        if not reason.strip():
            raise ScoreboardValidationError("Score corrections require a reason.")

        before = self._state_summary(state)
        if team is TeamSide.HOME:
            state.home_score = corrected_score
        else:
            state.away_score = corrected_score

        self._record_change(
            state,
            ScoreboardEventType.SCORE_CORRECTED,
            f"Corrected {team.value} score.",
            actor_user_id=actor_user_id,
            before_state=before,
            payload={"team": team.value, "corrected_score": corrected_score, "reason": reason},
        )
        return state

    def add_team_foul(
        self,
        state: ScoreboardState,
        team: TeamSide,
        actor_user_id: str | None = None,
    ) -> ScoreboardState:
        self._ensure_mutable_game(state)
        before = self._state_summary(state)
        state.team_fouls[team] += 1
        state.game_status = GameStatus.IN_PROGRESS

        self._record_change(
            state,
            ScoreboardEventType.TEAM_FOUL_ADDED,
            f"Added team foul for {team.value}.",
            actor_user_id=actor_user_id,
            before_state=before,
            payload={"team": team.value, "team_fouls": state.team_fouls[team]},
        )
        return state

    def add_player_foul(
        self,
        state: ScoreboardState,
        team: TeamSide,
        player_id: str,
        actor_user_id: str | None = None,
    ) -> ScoreboardState:
        self._ensure_mutable_game(state)
        before = self._state_summary(state)
        player_stats = self._player_stats(state, player_id)
        player_stats.fouls += 1
        state.team_fouls[team] += 1
        state.game_status = GameStatus.IN_PROGRESS

        self._record_change(
            state,
            ScoreboardEventType.PLAYER_FOUL_ADDED,
            f"Added player foul for {player_id}.",
            actor_user_id=actor_user_id,
            before_state=before,
            payload={
                "team": team.value,
                "player_id": player_id,
                "player_fouls": player_stats.fouls,
                "team_fouls": state.team_fouls[team],
            },
        )
        return state

    def set_quarter(
        self,
        state: ScoreboardState,
        quarter: int,
        remaining_seconds: int = DEFAULT_QUARTER_SECONDS,
        actor_user_id: str | None = None,
    ) -> ScoreboardState:
        self._ensure_mutable_game(state)
        if quarter < 1:
            raise ScoreboardValidationError("Quarter must be 1 or greater.")
        if remaining_seconds < 0:
            raise ScoreboardValidationError("Clock remaining seconds cannot be negative.")

        before = self._state_summary(state)
        state.clock.quarter = quarter
        state.clock.remaining_seconds = remaining_seconds
        state.clock.status = ClockStatus.STOPPED

        self._record_change(
            state,
            ScoreboardEventType.QUARTER_SET,
            f"Set quarter to {quarter}.",
            actor_user_id=actor_user_id,
            before_state=before,
            payload={"quarter": quarter, "remaining_seconds": remaining_seconds},
        )
        return state

    def use_timeout(
        self,
        state: ScoreboardState,
        team: TeamSide,
        actor_user_id: str | None = None,
    ) -> ScoreboardState:
        self._ensure_mutable_game(state)
        if state.timeouts_remaining[team] <= 0:
            raise ScoreboardValidationError("No timeouts remaining for this team.")

        before = self._state_summary(state)
        state.timeouts_remaining[team] -= 1

        self._record_change(
            state,
            ScoreboardEventType.TIMEOUT_USED,
            f"Used timeout for {team.value}.",
            actor_user_id=actor_user_id,
            before_state=before,
            payload={"team": team.value, "timeouts_remaining": state.timeouts_remaining[team]},
        )
        return state

    def start_clock(
        self,
        state: ScoreboardState,
        actor_user_id: str | None = None,
    ) -> ScoreboardState:
        self._ensure_mutable_game(state)
        if state.clock.remaining_seconds < 0:
            raise ScoreboardValidationError("Clock remaining seconds cannot be negative.")

        before = self._state_summary(state)
        state.clock.status = ClockStatus.RUNNING
        state.game_status = GameStatus.IN_PROGRESS

        self._record_change(
            state,
            ScoreboardEventType.CLOCK_STARTED,
            "Started game clock.",
            actor_user_id=actor_user_id,
            before_state=before,
            payload={"remaining_seconds": state.clock.remaining_seconds},
        )
        return state

    def stop_clock(
        self,
        state: ScoreboardState,
        remaining_seconds: int,
        actor_user_id: str | None = None,
    ) -> ScoreboardState:
        self._ensure_mutable_game(state)
        if remaining_seconds < 0:
            raise ScoreboardValidationError("Clock remaining seconds cannot be negative.")

        before = self._state_summary(state)
        state.clock.status = ClockStatus.STOPPED
        state.clock.remaining_seconds = remaining_seconds

        self._record_change(
            state,
            ScoreboardEventType.CLOCK_STOPPED,
            "Stopped game clock.",
            actor_user_id=actor_user_id,
            before_state=before,
            payload={"remaining_seconds": remaining_seconds},
        )
        return state

    def end_game(
        self,
        state: ScoreboardState,
        actor_user_id: str | None = None,
    ) -> ScoreboardState:
        self._ensure_non_negative_score(state.home_score)
        self._ensure_non_negative_score(state.away_score)
        before = self._state_summary(state)
        state.game_status = GameStatus.FINAL
        state.clock.status = ClockStatus.STOPPED

        self._record_change(
            state,
            ScoreboardEventType.GAME_ENDED,
            "Ended game.",
            actor_user_id=actor_user_id,
            before_state=before,
            payload={"home_score": state.home_score, "away_score": state.away_score},
        )
        return state

    def _record_change(
        self,
        state: ScoreboardState,
        event_type: ScoreboardEventType,
        summary: str,
        actor_user_id: str | None,
        before_state: dict[str, Any],
        payload: dict[str, Any],
    ) -> None:
        self._validate_non_negative_state(state)
        after_state = self._state_summary(state)
        entry = ScoreboardEventLogEntry(
            sequence=len(state.event_log) + 1,
            event_type=event_type,
            occurred_at=datetime.now(UTC),
            summary=summary,
            payload={**payload, "before_state": before_state, "after_state": after_state},
        )
        state.event_log.append(entry)
        log_structured_event(
            logger,
            action=event_type.value,
            result="success",
            user_id=actor_user_id,
            target_entity_type="scoreboard_state",
            target_entity_id=state.game_id,
            before_state_summary=before_state,
            after_state_summary=after_state,
            event_sequence=entry.sequence,
        )

    def _player_stats(self, state: ScoreboardState, player_id: str) -> PlayerStatLine:
        if not player_id.strip():
            raise ScoreboardValidationError("Player id is required.")
        return state.player_stats.setdefault(player_id, PlayerStatLine())

    def _ensure_mutable_game(self, state: ScoreboardState) -> None:
        if state.game_status is GameStatus.FINAL:
            raise ScoreboardValidationError("Finalized games cannot be changed.")

    def _validate_non_negative_state(self, state: ScoreboardState) -> None:
        self._ensure_non_negative_score(state.home_score)
        self._ensure_non_negative_score(state.away_score)
        for team, fouls in state.team_fouls.items():
            if fouls < 0:
                raise ScoreboardValidationError(f"{team.value} team fouls cannot be negative.")
        for team, timeouts in state.timeouts_remaining.items():
            if timeouts < 0:
                raise ScoreboardValidationError(f"{team.value} timeouts cannot be negative.")
        for player_id, player_stats in state.player_stats.items():
            if player_stats.points < 0 or player_stats.fouls < 0:
                raise ScoreboardValidationError(f"Player stats cannot be negative: {player_id}.")

    def _ensure_non_negative_score(self, score: int) -> None:
        if score < 0:
            raise ScoreboardValidationError("Scores cannot be negative.")

    def _state_summary(self, state: ScoreboardState) -> dict[str, Any]:
        return {
            "home_score": state.home_score,
            "away_score": state.away_score,
            "quarter": state.clock.quarter,
            "clock_status": state.clock.status.value,
            "remaining_seconds": state.clock.remaining_seconds,
            "home_team_fouls": state.team_fouls[TeamSide.HOME],
            "away_team_fouls": state.team_fouls[TeamSide.AWAY],
            "home_timeouts_remaining": state.timeouts_remaining[TeamSide.HOME],
            "away_timeouts_remaining": state.timeouts_remaining[TeamSide.AWAY],
            "game_status": state.game_status.value,
        }
