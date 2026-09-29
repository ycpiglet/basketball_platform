---
id: 2026_05_13_frontend_scoreboard_api_connection_context
title: Frontend Scoreboard API Connection Context
type: run
category: frontend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: engineering_manager
tags:
  - run
  - context
  - scoreboard
  - frontend
  - field_pilot
related_runs:
  - harness/runs/2026-05-13_pilot_scoreboard_api/
  - harness/runs/2026-05-13_frontend_scoreboard_api_connection/
related_files:
  - frontend/src/features/scoreboard/ScoreboardControlView.vue
  - frontend/src/features/scoreboard/ScoreboardDisplayView.vue
  - backend/app/api/routes/scoreboard.py
---

# 00 Context

## Request

- User request: Continue work after backend FP-001 API verification.
- Date: 2026-05-13
- Owner/coordinator: Engineering Manager

## Requirement Trace

- Requirement source: `docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md`
- Requirement section or domain: FP-003 scoreboard control UI and FP-004 display
  route sync.
- Phase: Phase 1 / MVP.
- Out of scope: Production authentication, persistent storage, payments,
  notifications, hardware control.

## Applicable Skills

- Engineering Manager: Yes.
- Lead Staff Engineer: Yes.
- Senior Designer: Yes.
- QA Debugger: Yes.
- Security Release Engineer: Yes.
- Technical Writer: Yes.
- Python coding: No.

## Affected Layers

- Frontend: API client, scoreboard views, tests.
- Backend: No new backend behavior planned.
- Database: No.
- Tests: Frontend tests and existing backend verification context.
- Docs: Harness/status records.

## Permission And Privacy

- Frontend sends current dev role as `x-user-role` for pilot state changes.
- Backend remains the authority for permission enforcement.
- No sensitive data fields are introduced.

## Logging And Error Handling

- Frontend must show loading, error, and retry states without crashing.
- Backend structured logs already cover scoreboard state changes.
