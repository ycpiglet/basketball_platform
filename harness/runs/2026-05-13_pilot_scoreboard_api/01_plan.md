---
id: 2026_05_13_pilot_scoreboard_api_plan
title: Pilot Scoreboard API Plan
type: run
category: backend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: lead_staff_engineer
tags:
  - run
  - plan
  - scoreboard
  - backend_api
related_runs:
  - harness/runs/2026-05-13_pilot_scoreboard_api/
---

# 01 Plan

## Goal

- Implement the Phase 1 FP-001 pilot scoreboard API over the existing
  `ScoreboardStateService` so frontend control, display, and result routes can
  later share backend-owned game state.

## Acceptance Criteria

- Replace the scoreboard placeholder router with concrete pilot endpoints.
- Add Pydantic request/response schemas for scoreboard state and actions.
- Add a clearly marked pilot-only in-memory state store.
- State-changing endpoints require at least Team Manager role through backend
  guardrails.
- Validation and state errors return structured HTTP errors.
- Tests cover create/read, score update, correction reason, team/player fouls,
  clock/quarter/timeout/finalization, finalized mutation rejection, and role
  guardrails.
- No Phase 2 behavior or production auth is introduced.

## Applicable Skills

- Engineering Manager
- Lead Staff Engineer
- QA Debugger
- Security Release Engineer
- Technical Writer
- Python coding

## Reuse Plan

- Compound records read:
  - `harness/compound/state/2026-05-12_project_context_compound.md`
  - `harness/compound/lessons/2026-05-12_backend_environment_compound.md`
- Existing code/docs to reuse:
  - `backend/app/services/scoreboard_state.py`
  - `backend/app/core/rbac.py`
  - `backend/app/core/exception_handlers.py`
  - Existing `fastapi.testclient` test style
- Sandbox experiments to consult: None.
- Work not to recreate:
  - Score calculation business rules already in `ScoreboardStateService`.

## Tasks

| Status | Owner | Task | Notes |
|---|---|---|---|
| Complete | Lead Staff Engineer | Add pilot scoreboard schemas, store, and route endpoints | Backend only. |
| Complete | QA Debugger | Add API regression tests | Include adversarial/finalized/permission cases. |
| Complete | Security Release Engineer | Verify no secrets/sensitive data and backend role guardrails | Header-based pilot guardrail only. |
| Blocked | Evaluator | Run backend tests and ruff | Python 3.11 and ruff are not currently available. |
| Complete | Technical Writer | Update run records and status | Captured blocker and next step. |

## Test Plan

- Automated:
  - `pytest` from `backend/` once Python 3.11+ and dependencies are available.
  - Targeted test file: `backend/tests/test_scoreboard_api.py`.
  - `ruff check .` from `backend/` once dependencies/tooling are available.
- Manual:
  - Inspect route response models and role guardrails.
  - Confirm `git diff --check`.
- Not applicable:
  - Frontend tests in this slice.
  - Database migration tests.

## Risks

- Local Python is 3.10.12 and `python3.11` is not on PATH, so backend tests are
  expected to remain blocked until environment setup is fixed.
- Header-based role guardrails are not production authentication. They are an MVP
  pilot safeguard only.
