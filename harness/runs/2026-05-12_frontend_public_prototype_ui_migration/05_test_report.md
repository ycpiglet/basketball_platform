---
id: 2026_05_12_frontend_public_prototype_ui_migration_test_report
title: Frontend Public Prototype UI Migration Test Report
type: run
category: frontend
status: complete
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - frontend
  - test_report
  - ui
related_runs:
  - harness/runs/2026-05-12_frontend_public_prototype_ui_migration/
---

# 05 Test Report

## Automated Tests

| Command | Result | Notes |
|---|---|---|
| `npm run test -- --run` | Passed | 2 files, 5 tests passed. |
| `npm run lint -- --fix` | Passed | Auto-fixed Vue formatting. |
| `npm run lint` | Passed | No warnings after fix. |
| `npm run build` | Passed | Production build completed. |
| `git diff --check` | Passed | No whitespace errors. |

## Manual Checks

| Scenario | Result | Evidence |
|---|---|---|
| Public display route has no app nav | Passed by code inspection | `AppLayout.vue` renders only `RouterView` when `route.meta.publicDisplay === true`. |
| Dev server starts | Passed | Vite running at `http://localhost:5173/`. |
| Static demo state shared across routes | Passed by code inspection | `frontend/src/shared/demo/pilotGame.ts`. |

## Coverage Notes

- Score updates: UI controls only; no state mutation/API yet.
- Timer transitions: UI controls only; no state mutation/API yet.
- Player/team foul updates: UI controls and score sheet display only.
- Box score aggregation: Static demo box score only.
- Permission checks: Existing route guard tests passed.
- Sensitive data masking: Demo data only; no sensitive fields added.
- PDF fallback to `N/A`: N/A.
- API validation failures: N/A.
- Frontend critical flow: Routes render against existing tests/build.

## Skipped Tests

| Test | Reason | Risk |
|---|---|---|
| Browser screenshot/device viewport QA | No browser automation tool configured in this run. | Medium for final visual polish. |
| Backend tests | No backend code changed; backend environment issue remains tracked separately. | Low for this UI-only work. |

