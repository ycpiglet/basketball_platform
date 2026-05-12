---
id: 2026_05_12_backend_test_environment
title: Backend Test Environment Not Ready
type: issue
category: backend
status: open
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - backend
  - pytest
  - python_3_11
  - test_environment
  - dependency_install
related_runs:
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

## Evidence

- Command: `pytest`
- Working directory: `backend/`
- Result: collection failed with import errors for `datetime.UTC`, `StrEnum`,
  and missing `sqlalchemy`.

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
