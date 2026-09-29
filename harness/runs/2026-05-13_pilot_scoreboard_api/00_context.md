---
id: 2026_05_13_pilot_scoreboard_api_context
title: Pilot Scoreboard API Context
type: run
category: backend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: engineering_manager
tags:
  - run
  - context
  - scoreboard
  - field_pilot
  - backend
related_runs:
  - harness/runs/2026-05-13_pilot_scoreboard_api/
related_files:
  - docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md
  - backend/app/services/scoreboard_state.py
  - backend/app/api/routes/scoreboard.py
related_issues:
  - harness/issue_log/2026-05-12_backend_test_environment.md
---

# 00 Context

## Request

- User request: "역할에 따라서 작업 시작해줘"
- Date: 2026-05-13
- Owner/coordinator: Engineering Manager

## Requirement Trace

- Requirement source:
  - `requirements_en.md` section 2.1 Phase 1 feature scope
  - `AGENTS.md` sections 3, 5, 8, 10, 11, 12, 13, 21
  - `docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md` work package FP-001
- Requirement section or domain: Game operation, scoreboard control, digital
  scorekeeping, field pilot API.
- Phase: Phase 1 / MVP.
- Out of scope:
  - Production authentication.
  - Payment, credit, ad, notification, reservation payment, hardware control.
  - Persistent PostgreSQL/MongoDB implementation beyond pilot-only state.

## Applicable Skills

- Engineering Manager: Yes.
- Lead Staff Engineer: Yes.
- QA Debugger: Yes.
- Security Release Engineer: Yes.
- Technical Writer: Yes.
- Python coding: Yes. Read `harness/skills/python_coding/SKILL.md`.

## Role Assignments

- Founder Product Lead: Preserve Phase 1 field pilot scope.
- Engineering Manager: Keep this run scoped to FP-001 backend API and visible blockers.
- Lead Staff Engineer: Implement conservative API over existing deterministic
  service.
- QA Debugger: Add API regression tests for normal, invalid, finalized, and
  permission paths.
- Security Release Engineer: Review backend role guardrails and sensitive data
  handling.
- Technical Writer: Keep run records, issue status, and final summary current.

## Reuse And Compound Check

- Relevant compound records:
  - `harness/compound/state/2026-05-12_project_context_compound.md`
  - `harness/compound/lessons/2026-05-12_backend_environment_compound.md`
  - `harness/compound/patterns/2026-05-13_agent_operating_model.md`
- Existing services/docs/templates to reuse:
  - `ScoreboardStateService`
  - Existing FastAPI router and structured error patterns
  - Existing RBAC helper
- Known mistakes to avoid:
  - Do not debug Python 3.11-only imports under Python 3.10 as product failures.
  - Do not treat frontend demo state as authoritative.
  - Do not add Phase 2 behavior.
- Sandbox needed: No.

## Affected Layers

- Frontend: Not in this slice.
- Backend: Scoreboard API routes, schemas, pilot state store, API tests.
- Database: No persistent schema change.
- Document processing: No.
- Integration: No.
- Tests: Backend API tests added; execution may be blocked by Python 3.11
  environment.
- Docs: Harness run records and status if direction changes.

## Permission And Privacy

- Roles involved: Guest, Team Manager, System Administrator.
- Ownership rules: Pilot state-changing scoreboard endpoints require at least
  Team Manager role. Guest can read public scoreboard state.
- Sensitive fields: No phone, address, account, payment, card, password, token,
  or private team member data in this slice.
- API-level enforcement needed: Yes, via backend role guardrails using request
  headers until production authentication exists.

## Logging And Error Handling

- Runtime logs required:
  - Existing scoreboard service structured logs for score, timer, foul, timeout,
    quarter, correction, and finalization actions.
  - API validation failures through existing exception handler.
- Error states to handle:
  - Missing game.
  - Duplicate pilot game id.
  - Invalid role header.
  - Unauthorized state change.
  - Scoreboard validation errors.
  - Finalized game mutation.
- Values that must never be logged:
  - Passwords, tokens, private keys, payment credentials, unnecessary personal
    data.
