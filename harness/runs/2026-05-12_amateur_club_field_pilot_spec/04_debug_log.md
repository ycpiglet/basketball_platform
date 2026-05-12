# 04 Debug Log

## Symptoms

- Backend tests failed during collection.
- Frontend tests passed.

## Hypotheses

- Backend runtime did not match declared Python version.
- Backend dependencies were not installed in the active environment.

## Checks Performed

| Check | Result | Evidence |
|---|---|---|
| Backend test run | Failed | `pytest` reported Python 3.10.12 collection errors for `datetime.UTC`, `StrEnum`, and missing `sqlalchemy`. |
| Backend project metadata | Confirmed | `backend/pyproject.toml` declares `requires-python = ">=3.11"`. |
| Frontend test run | Passed | `npm run test -- --run` reported 2 files and 5 tests passed. |

## Root Cause

- Backend tests were run outside the declared Python runtime and without all
  backend dependencies installed.

## Fix Notes

- Use a Python 3.11+ virtual environment.
- Install dependencies with `pip install -e '.[dev]'`.
- Re-run `pytest` and `ruff check .`.

