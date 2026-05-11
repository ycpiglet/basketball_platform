# Backend

FastAPI backend foundation for the Phase 1 MVP.

## Scope in this skeleton

Implemented now:

- Health-check API route at `GET /api/v1/health`.
- Versioned API router structure under `/api/v1`.
- Placeholder routers for users, teams, players, games, leagues, tournaments, and scoreboard.
- Structured JSON logging with request id propagation and sensitive-field masking.
- Global request middleware for request ids, request completion logs, and unhandled exception responses.
- Structured HTTP and validation error responses.
- Pydantic request validation pattern via `POST /api/v1/{resource}/validation-preview` placeholder endpoints.
- Pytest setup with minimal health and error-handling tests.

Not implemented in this Phase 1 backend foundation:

- Production authentication or authorization.
- Payment, credit, wallet, point, settlement, or refund behavior.
- Gym rental payment or commercial reservation flows.
- Notification, advertising, or external verification providers.
- RS-485/RF hardware control or packet transmission.

## Placeholder API routes

| Route | Purpose |
|---|---|
| `GET /api/v1/health` | Health check for local development and deployment probes. |
| `GET /api/v1/users` | Placeholder for future user profile and role APIs. |
| `GET /api/v1/teams` | Placeholder for future team CRUD and roster APIs. |
| `GET /api/v1/players` | Placeholder for future player CRUD and privacy-safe profile APIs. |
| `GET /api/v1/games` | Placeholder for future game setup, state, result, and box-score APIs. |
| `GET /api/v1/leagues` | Placeholder for future league CRUD, schedules, standings, and results. |
| `GET /api/v1/tournaments` | Placeholder for future tournament CRUD, brackets, and result workflows. |
| `GET /api/v1/scoreboard` | Placeholder for future scoreboard state and display synchronization APIs. |
| `POST /api/v1/{resource}/validation-preview` | Pydantic validation example; accepts a `name` and optional `notes`. |

## Local commands

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
pytest
ruff check .
```

The API defaults to `http://localhost:8000/api/v1`.

## Example validation request

```bash
curl -X POST http://localhost:8000/api/v1/teams/validation-preview \
  -H 'Content-Type: application/json' \
  -d '{"name":"Example team","notes":"Validation-only placeholder"}'
```

Invalid payloads return a structured error response with a request id and field paths.
