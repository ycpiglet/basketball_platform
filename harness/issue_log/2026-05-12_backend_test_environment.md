---
id: 2026_05_12_backend_test_environment
title: Backend Test Environment Not Ready
type: issue
category: backend
status: active
created: 2026-05-12
updated: 2026-05-13
phase: phase1_mvp
tags:
  - backend
  - pytest
  - python_3_11
  - test_environment
  - dependency_install
related_runs:
  - harness/runs/2026-05-13_pilot_scoreboard_api/
  - harness/runs/2026-05-12_amateur_club_field_pilot_spec/
related_debug:
  - harness/debugging/2026-05-12_backend_pytest_collection_failure.md
related_files:
  - backend/pyproject.toml
---

# Issue: Backend Test Environment Not Ready

## Severity

- High

## Status

- Open

## Area

- Backend / test environment

## Summary

Backend tests currently fail during collection in the local environment. The
project declares Python `>=3.11`, but the observed local interpreter was Python
3.10.12. The backend also lacked installed dependencies such as SQLAlchemy in
that environment.

The issue was reproduced again on 2026-05-13 while validating
`harness/runs/2026-05-13_pilot_scoreboard_api/`. The active `python` and
`python3` commands are Python 3.10.12, `python3.11` is not on PATH, and `ruff`
is not installed.

The FP-001 backend verification was completed through Docker with the official
`python:3.11-slim` image:

- `pytest tests/test_scoreboard_api.py`: 9 passed.
- `pytest`: 28 passed.
- `ruff check .`: all checks passed.

Host-local setup is still not ready.

## Evidence

- Command: `pytest`
- Working directory: `backend/`
- Result: collection failed with import errors for `datetime.UTC`, `StrEnum`,
  and missing `sqlalchemy`.
- Command: `pytest tests/test_scoreboard_api.py`
- Working directory: `backend/`
- Result on 2026-05-13: collection failed at `from enum import StrEnum` under
  Python 3.10.12.
- Command: `ruff check .`
- Result on 2026-05-13: `ruff` command not found.

## Expected Behavior

Backend tests should collect and run under a Python 3.11+ virtual environment
with dev dependencies installed.

## Actual Behavior

Tests fail before execution in Python 3.10.12 and without installed backend
dependencies.

## Owner

- Backend / DevOps

## Next Step

- Create/use Python 3.11+ virtual environment.
- Install backend dev dependencies with `pip install -e '.[dev]'`.
- Re-run `pytest` and `ruff check .`.
- Or document Docker Python 3.11 verification as the standard backend test path.
