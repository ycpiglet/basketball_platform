---
id: 2026_05_13_frontend_scoreboard_api_connection_plan
title: Frontend Scoreboard API Connection Plan
type: run
category: frontend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: lead_staff_engineer
tags:
  - run
  - plan
  - scoreboard
  - frontend
related_runs:
  - harness/runs/2026-05-13_frontend_scoreboard_api_connection/
---

# 01 Plan

## Goal

- Connect scoreboard control and display routes to the backend pilot scoreboard
  API while keeping the existing mobile/tablet/TV layout.

## Acceptance Criteria

- Add a typed frontend scoreboard API client.
- Control route creates or loads the pilot game and sends score, foul, timeout,
  clock, quarter, correction, and finalize actions to backend.
- Display route reads the same backend state and polls for updates.
- Loading, error, retry, and disabled-action states are visible.
- Frontend tests cover API request headers, state mapping, and error handling.
- Existing route guard tests still pass.

## Tasks

| Status | Owner | Task | Notes |
|---|---|---|---|
| Complete | Lead Staff Engineer | Add frontend API client and composable state helper | Uses `VITE_API_BASE_URL`. |
| Complete | Senior Designer | Preserve field-operation layout and states | Large controls and no admin controls on display. |
| Complete | QA Debugger | Add frontend regression tests | Mock fetch. |
| Complete | Evaluator | Run frontend lint/test/build if dependencies exist | All passed. |
| Complete | Technical Writer | Update run and status records | Linked next step. |

## Test Plan

- `cd frontend && npm run test`
- `cd frontend && npm run lint`
- `cd frontend && npm run build`

## Risks

- Backend dev server may not be running during frontend manual use.
- Header-based dev role is pilot-only and not production authentication.
