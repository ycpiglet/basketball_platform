---
id: 2026_05_12_backend_environment_compound
title: Backend Test Environment Compound
type: compound
category: backend
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - backend
  - python_3_11
  - pytest
  - test_environment
  - dependency_install
related_runs:
  - harness/runs/2026-05-12_amateur_club_field_pilot_spec/
related_files:
  - backend/pyproject.toml
related_issues:
  - harness/issue_log/2026-05-12_backend_test_environment.md
related_debug:
  - harness/debugging/2026-05-12_backend_pytest_collection_failure.md
search_terms:
  - pytest collection failure
  - datetime UTC
  - StrEnum
  - sqlalchemy missing
---

# Backend Test Environment Compound

## Synthesis

Backend test failures observed on 2026-05-12 were environment failures, not a
confirmed backend logic failure. The active local interpreter was Python 3.10.12,
but the backend declares Python `>=3.11` and uses Python 3.11 features.
Dependencies such as SQLAlchemy were also missing.

## Evidence

- `pytest` failed during collection.
- Errors included `datetime.UTC`, `StrEnum`, and missing `sqlalchemy`.
- `backend/pyproject.toml` declares `requires-python = ">=3.11"`.

## Reuse

- Use Python 3.11+ before running backend tests.
- Install dependencies with `pip install -e '.[dev]'`.
- Read `harness/skills/python_coding/SKILL.md` before backend Python changes.

## Avoid

- Do not spend time debugging `datetime.UTC` or `StrEnum` under Python 3.10.
- Do not mark backend tests as product failures until the declared runtime and
  dependencies are active.

## Next Actions

- Create or select a Python 3.11+ virtual environment.
- Install backend dev dependencies.
- Run `pytest` and `ruff check .`.
- Update this compound if failures remain after the environment is correct.

