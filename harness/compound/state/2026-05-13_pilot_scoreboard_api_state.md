---
id: 2026_05_13_pilot_scoreboard_api_state
title: Pilot Scoreboard API State
type: compound
category: backend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - scoreboard
  - backend_api
  - field_pilot
  - python_3_11
  - docker_verified
related_runs:
  - harness/runs/2026-05-13_pilot_scoreboard_api/
related_files:
  - backend/app/api/routes/scoreboard.py
  - backend/app/schemas/scoreboard.py
  - backend/app/services/scoreboard_store.py
  - backend/tests/test_scoreboard_api.py
related_issues:
  - harness/issue_log/2026-05-12_backend_test_environment.md
search_terms:
  - pilot scoreboard api
  - FP-001
  - scoreboard api verification blocked
  - backend game state
---

# Pilot Scoreboard API State

## Synthesis

FP-001 has a backend implementation slice: concrete scoreboard routes now wrap
`ScoreboardStateService`, use a pilot-only in-memory store, serialize shared game
state, and enforce backend role guardrails for state-changing operations.

The implementation is verified through Docker Python 3.11.15:

- `pytest tests/test_scoreboard_api.py`: 9 passed.
- `pytest`: 28 passed.
- `ruff check .`: all checks passed.

The host environment still only has Python 3.10.12 and no `ruff` executable, so
host-local verification remains an operational follow-up.

## Reuse

- Reuse `backend/app/api/routes/scoreboard.py` as the API surface for frontend
  control, display, live record, and result routes.
- Reuse `backend/app/schemas/scoreboard.py` response shape for frontend API
  clients.
- Reuse `backend/app/services/scoreboard_store.py` only as a controlled
  pilot-state store. Replace it with persistent storage before broader use.
- Reuse `backend/tests/test_scoreboard_api.py` as the regression target once
  Python 3.11+ and backend dev dependencies are available locally, or through
  the Docker Python 3.11 verification command used in the run.

## Avoid

- Do not treat the in-memory store as durable persistence.
- Do not treat `x-user-role` headers as production authentication.
- Do not treat host Python 3.10 test failures as product failures; use Python
  3.11+ or the Docker verification path.
- Do not start frontend API connection work without accounting for the current
  backend verification blocker.

## Next Actions

- Decide whether to standardize backend verification on Docker or install
  Python 3.11+ and dev dependencies on the host.
- Continue with FP-003 and FP-004: connect frontend control and display routes
  to the backend scoreboard state.
