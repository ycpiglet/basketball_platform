---
id: 2026_05_12_backend_pytest_collection_failure
title: Backend Pytest Collection Failure
type: debug
category: backend
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - backend
  - pytest
  - python_3_11
  - datetime_utc
  - strenum
  - sqlalchemy
related_runs:
  - harness/runs/2026-05-12_amateur_club_field_pilot_spec/
related_issues:
  - harness/issue_log/2026-05-12_backend_test_environment.md
related_files:
  - backend/pyproject.toml
---

# Debugging Note: Backend Pytest Collection Failure

## Symptom

`pytest` in `backend/` collected zero tests and failed during import.

## Reproduction

```bash
cd backend
pytest
```

## Investigation

Observed errors:

- `ImportError: cannot import name 'UTC' from 'datetime'`
- `ImportError: cannot import name 'StrEnum' from 'enum'`
- `ModuleNotFoundError: No module named 'sqlalchemy'`

`backend/pyproject.toml` declares `requires-python = ">=3.11"`, but the observed
local Python was 3.10.12.

## Root Cause

The backend was tested outside its declared Python runtime and without installed
backend dependencies.

## Fix

Use Python 3.11+ and install backend dev dependencies before running backend
tests.

## Verification

Pending. Re-run after a Python 3.11+ environment is available.
