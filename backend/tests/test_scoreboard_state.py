import logging

import pytest

from app.services.scoreboard_state import (
    ClockStatus,
    GameStatus,
    ScoreboardEventType,
    ScoreboardStateService,
    ScoreboardValidationError,
    TeamSide,
)


def test_adds_one_two_and_three_points_and_player_points(caplog: pytest.LogCaptureFixture) -> None:
    service = ScoreboardStateService()
    state = service.create_game("game-1")

    with caplog.at_level(logging.INFO, logger="app.services.scoreboard_state"):
        service.add_points(state, TeamSide.HOME, "home-player-1", 1)
        service.add_points(state, TeamSide.HOME, "home-player-1", 2)
        service.add_points(state, TeamSide.AWAY, "away-player-1", 3)

    assert state.home_score == 3
    assert state.away_score == 3
    assert state.player_stats["home-player-1"].points == 3
    assert state.player_stats["away-player-1"].points == 3
    assert [entry.sequence for entry in state.event_log] == [1, 2, 3]
    assert [entry.event_type for entry in state.event_log] == [
        ScoreboardEventType.SCORE_ADDED,
        ScoreboardEventType.SCORE_ADDED,
        ScoreboardEventType.SCORE_ADDED,
    ]
    assert [record.action for record in caplog.records] == ["score_added"] * 3


def test_corrects_score_with_auditable_event() -> None:
    service = ScoreboardStateService()
    state = service.create_game("game-2")

    service.add_points(state, TeamSide.HOME, "home-player-1", 3)
    service.correct_score(state, TeamSide.HOME, corrected_score=2, reason="Scorekeeper correction")

    assert state.home_score == 2
    assert state.event_log[-1].event_type == ScoreboardEventType.SCORE_CORRECTED
    assert state.event_log[-1].payload["reason"] == "Scorekeeper correction"
    assert state.event_log[-1].payload["before_state"]["home_score"] == 3
    assert state.event_log[-1].payload["after_state"]["home_score"] == 2


def test_adds_team_fouls() -> None:
    service = ScoreboardStateService()
    state = service.create_game("game-3")

    service.add_team_foul(state, TeamSide.AWAY)
    service.add_team_foul(state, TeamSide.AWAY)

    assert state.team_fouls[TeamSide.AWAY] == 2
    assert state.event_log[-1].event_type == ScoreboardEventType.TEAM_FOUL_ADDED


def test_adds_player_fouls_and_team_foul() -> None:
    service = ScoreboardStateService()
    state = service.create_game("game-4")

    service.add_player_foul(state, TeamSide.HOME, "home-player-2")

    assert state.player_stats["home-player-2"].fouls == 1
    assert state.team_fouls[TeamSide.HOME] == 1
    assert state.event_log[-1].event_type == ScoreboardEventType.PLAYER_FOUL_ADDED


@pytest.mark.parametrize("invalid_points", [0, -1, 4])
def test_prevents_invalid_scoring_values(invalid_points: int) -> None:
    service = ScoreboardStateService()
    state = service.create_game("game-5")

    with pytest.raises(ScoreboardValidationError, match="1, 2, or 3"):
        service.add_points(state, TeamSide.HOME, "home-player-1", invalid_points)

    assert state.home_score == 0
    assert state.event_log == []


def test_rejects_negative_score_correction() -> None:
    service = ScoreboardStateService()
    state = service.create_game("game-6")

    with pytest.raises(ScoreboardValidationError, match="cannot be negative"):
        service.correct_score(state, TeamSide.AWAY, corrected_score=-1, reason="bad correction")

    assert state.away_score == 0
    assert state.event_log == []


def test_sets_quarter_and_resets_clock() -> None:
    service = ScoreboardStateService()
    state = service.create_game("game-quarter")

    service.set_quarter(state, quarter=2, remaining_seconds=480)

    assert state.quarter == 2
    assert state.clock.remaining_seconds == 480
    assert state.clock.status == ClockStatus.STOPPED
    assert state.event_log[-1].event_type == ScoreboardEventType.QUARTER_SET


def test_rejects_negative_clock_and_timeout_underflow() -> None:
    service = ScoreboardStateService()
    state = service.create_game("game-7")

    with pytest.raises(ScoreboardValidationError, match="Clock remaining seconds"):
        service.stop_clock(state, remaining_seconds=-1)

    state.timeouts_remaining[TeamSide.HOME] = 0
    with pytest.raises(ScoreboardValidationError, match="No timeouts remaining"):
        service.use_timeout(state, TeamSide.HOME)

    assert state.event_log == []


def test_ending_game_stops_clock_logs_event_and_prevents_future_changes() -> None:
    service = ScoreboardStateService()
    state = service.create_game("game-8")

    service.start_clock(state)
    service.add_points(state, TeamSide.HOME, "home-player-1", 2)
    service.end_game(state)

    assert state.game_status == GameStatus.FINAL
    assert state.clock.status == ClockStatus.STOPPED
    assert state.event_log[-1].event_type == ScoreboardEventType.GAME_ENDED

    with pytest.raises(ScoreboardValidationError, match="Finalized games"):
        service.add_points(state, TeamSide.HOME, "home-player-1", 1)
