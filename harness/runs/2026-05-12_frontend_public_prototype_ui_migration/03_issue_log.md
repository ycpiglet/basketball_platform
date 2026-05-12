---
id: 2026_05_12_frontend_public_prototype_ui_migration_issue_log
title: Frontend Public Prototype UI Migration Issue Log
type: run
category: frontend
status: complete
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - frontend
  - issue_log
  - ui
related_runs:
  - harness/runs/2026-05-12_frontend_public_prototype_ui_migration/
---

# 03 Issue Log

| ID | Severity | Status | Area | Summary | Owner | Next Step |
|---|---|---|---|---|---|---|
| FUI-001 | Medium | Open | Frontend / Backend | UI uses static demo state and is not connected to backend game state. | Frontend / Backend | Implement pilot scoreboard API and replace demo state with API state. |
| FUI-002 | Medium | Open | Visual QA | No browser screenshot or device viewport inspection was performed in this run. | Frontend | Manually inspect mobile, tablet, and TV display route. |
| FUI-003 | Low | Open | Prototype source | Root `public/index.html` is still untracked and outside the Vite frontend tree. | Product / Frontend | Decide whether to keep it as tracked prototype reference or move it under docs. |

## Scope Questions

- Should the demo UI continue to include Korean labels by default for the field
  pilot, with English added later through localization?
- Should `public/index.html` become a tracked docs prototype artifact?

## Blockers

- None for UI demo migration.
- Backend API connection remains a blocker for real field operation.

