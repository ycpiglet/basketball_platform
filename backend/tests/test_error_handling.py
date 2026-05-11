from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_validation_errors_use_structured_error_response() -> None:
    response = client.post("/api/v1/teams/validation-preview", json={"notes": "missing name"})

    assert response.status_code == 422
    payload = response.json()
    assert payload["error"]["code"] == "validation_error"
    assert payload["error"]["message"] == "Request validation failed."
    assert payload["error"]["request_id"]
    assert "body.name" in payload["error"]["fields"]
