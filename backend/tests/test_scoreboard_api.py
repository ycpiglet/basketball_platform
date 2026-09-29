from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app.api.routes.scoreboard import pilot_scoreboard_store
from app.core.config import get_settings
from app.main import app

client = TestClient(app)

OPERATOR_HEADERS = {"x-user-role": "team_manager", "x-user-id": "operator-1"}
ADMIN_HEADERS = {"x-user-role": "system_admin", "x-user-id": "admin-1"}


@pytest.fixture(autouse=True)
def clear_pilot_scoreboard_store() -> Iterator[None]:
    pilot_scoreboard_store.clear()
    yield
    pilot_scoreboard_store.clear()


def create_game(game_id: str = "game-api") -> dict:
    response = client.post(
        "/api/v1/scoreboard/games",
        json={"game_id": game_id},
        headers=OPERATOR_HEADERS,
    )
    assert response.status_code == 201
    return response.json()


def test_creates_and_reads_public_scoreboard_game() -> None:
    created = create_game()

    response = client.get(f"/api/v1/scoreboard/games/{created['game_id']}")

    assert response.status_code == 200
    payload = response.json()
    assert payload["game_id"] == "game-api"
    assert payload["game_status"] == "not_started"
    assert payload["home"]["score"] == 0
    assert payload["away"]["score"] == 0
    assert payload["clock"]["remaining_seconds"] == 600


def test_score_changes_require_operator_role() -> None:
    response = client.post("/api/v1/scoreboard/games", json={"game_id": "forbidden-game"})

    assert response.status_code == 403
    assert response.json()["error"]["message"] == (
        "Scoreboard changes require team_manager or system_admin role."
    )


def test_invalid_role_header_is_rejected() -> None:
    response = client.post(
        "/api/v1/scoreboard/games",
        json={"game_id": "bad-role-game"},
        headers={"x-user-role": "owner"},
    )

    assert response.status_code == 403
    assert response.json()["error"]["message"] == "Invalid x-user-role header."


def test_header_role_is_refused_outside_local_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_ENV", "production")
    get_settings.cache_clear()
    try:
        response = client.post(
            "/api/v1/scoreboard/games",
            json={"game_id": "deployed-guard-game"},
            headers=ADMIN_HEADERS,
        )
    finally:
        get_settings.cache_clear()

    assert response.status_code == 403
    assert response.json()["error"]["message"] == (
        "Header-based scoreboard roles are only available in local development."
    )


def test_public_read_still_works_outside_local_env(monkeypatch: pytest.MonkeyPatch) -> None:
    created = create_game("public-read-game")
    monkeypatch.setenv("APP_ENV", "production")
    get_settings.cache_clear()
    try:
        response = client.get(f"/api/v1/scoreboard/games/{created['game_id']}")
    finally:
        get_settings.cache_clear()

    assert response.status_code == 200


def test_records_points_and_player_totals() -> None:
    create_game()

    response = client.post(
        "/api/v1/scoreboard/games/game-api/points",
        json={"team": "home", "player_id": "home-player-1", "points": 3},
        headers=OPERATOR_HEADERS,
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["home"]["score"] == 3
    assert payload["away"]["score"] == 0
    assert payload["game_status"] == "in_progress"
    assert payload["player_stats"] == [
        {"player_id": "home-player-1", "points": 3, "fouls": 0}
    ]
    assert payload["event_log"][-1]["event_type"] == "score_added"
    assert payload["event_log"][-1]["payload"]["points"] == 3


def test_rejects_invalid_scoring_values_with_structured_validation_error() -> None:
    create_game()

    response = client.post(
        "/api/v1/scoreboard/games/game-api/points",
        json={"team": "home", "player_id": "home-player-1", "points": 4},
        headers=OPERATOR_HEADERS,
    )

    assert response.status_code == 422
    payload = response.json()
    assert payload["error"]["code"] == "validation_error"
    assert "body.points" in payload["error"]["fields"]


def test_score_correction_requires_non_blank_reason() -> None:
    create_game()

    response = client.post(
        "/api/v1/scoreboard/games/game-api/score-corrections",
        json={"team": "home", "corrected_score": 2, "reason": " "},
        headers=OPERATOR_HEADERS,
    )

    assert response.status_code == 400
    assert response.json()["error"]["message"] == "Score corrections require a reason."


def test_records_fouls_timeout_and_clock_transitions() -> None:
    create_game()

    team_foul_response = client.post(
        "/api/v1/scoreboard/games/game-api/team-fouls",
        json={"team": "away"},
        headers=ADMIN_HEADERS,
    )
    player_foul_response = client.post(
        "/api/v1/scoreboard/games/game-api/player-fouls",
        json={"team": "home", "player_id": "home-player-2"},
        headers=OPERATOR_HEADERS,
    )
    timeout_response = client.post(
        "/api/v1/scoreboard/games/game-api/timeouts",
        json={"team": "home"},
        headers=OPERATOR_HEADERS,
    )
    quarter_response = client.post(
        "/api/v1/scoreboard/games/game-api/quarters",
        json={"quarter": 2, "remaining_seconds": 480},
        headers=OPERATOR_HEADERS,
    )
    start_response = client.post(
        "/api/v1/scoreboard/games/game-api/clock/start",
        headers=OPERATOR_HEADERS,
    )
    stop_response = client.post(
        "/api/v1/scoreboard/games/game-api/clock/stop",
        json={"remaining_seconds": 455},
        headers=OPERATOR_HEADERS,
    )

    assert team_foul_response.status_code == 200
    assert player_foul_response.status_code == 200
    assert timeout_response.status_code == 200
    assert quarter_response.status_code == 200
    assert start_response.status_code == 200
    assert stop_response.status_code == 200

    payload = stop_response.json()
    assert payload["home"]["team_fouls"] == 1
    assert payload["away"]["team_fouls"] == 1
    assert payload["home"]["timeouts_remaining"] == 4
    assert payload["clock"] == {
        "quarter": 2,
        "remaining_seconds": 455,
        "status": "stopped",
    }
    assert payload["player_stats"] == [
        {"player_id": "home-player-2", "points": 0, "fouls": 1}
    ]


def test_finalized_game_rejects_future_mutations() -> None:
    create_game()

    finalize_response = client.post(
        "/api/v1/scoreboard/games/game-api/finalize",
        headers=OPERATOR_HEADERS,
    )
    mutation_response = client.post(
        "/api/v1/scoreboard/games/game-api/points",
        json={"team": "home", "player_id": "home-player-1", "points": 1},
        headers=OPERATOR_HEADERS,
    )

    assert finalize_response.status_code == 200
    assert finalize_response.json()["game_status"] == "final"
    assert mutation_response.status_code == 400
    assert mutation_response.json()["error"]["message"] == "Finalized games cannot be changed."


def test_missing_game_returns_structured_not_found_error() -> None:
    response = client.get("/api/v1/scoreboard/games/missing-game")

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "not_found"
