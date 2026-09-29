---
id: 2026_05_13_frontend_scoreboard_api_connection_state
title: Frontend Scoreboard API Connection State
type: compound
category: frontend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - scoreboard
  - frontend
  - display_sync
  - control_ui
  - field_pilot
related_runs:
  - harness/runs/2026-05-13_frontend_scoreboard_api_connection/
  - harness/runs/2026-05-13_pilot_scoreboard_api/
related_files:
  - frontend/src/features/scoreboard/scoreboardApi.ts
  - frontend/src/features/scoreboard/useScoreboardGame.ts
  - frontend/src/features/scoreboard/ScoreboardControlView.vue
  - frontend/src/features/scoreboard/ScoreboardDisplayView.vue
  - frontend/src/tests/scoreboardApi.test.ts
search_terms:
  - frontend scoreboard api connection
  - FP-003
  - FP-004
  - display route polling
---

# Frontend Scoreboard API Connection State

## Synthesis

FP-003 and FP-004 now have a first connected frontend slice. The control route
creates or loads the pilot game, sends scoreboard actions to the backend, and
renders backend-owned score, foul, timeout, clock, and event state. The display
route reads the same backend state and polls for updates without admin controls.

## Reuse

- Reuse `scoreboardApi.ts` for typed calls to the backend scoreboard routes.
- Reuse `useScoreboardGame.ts` for loading, retry, action pending, polling, and
  user-facing API error states.
- Reuse `scoreboardViewModel.ts` for clock/status/team/event mapping.
- Reuse `scoreboardApi.test.ts` for frontend regression coverage around headers,
  not-found creation, backend validation errors, and view mapping.

## Avoid

- Do not move permission authority into the frontend. The frontend only sends
  pilot headers; backend remains authoritative.
- Do not add display-route admin controls.
- Do not assume the backend server is running; preserve error/retry states.

## Next Actions

- Add result/box score route connection from backend final state.
- Add manual browser QA across phone, tablet, and TV-size viewports.
- Decide whether to add a dedicated frontend test for control/display component
  rendering once the UI flow stabilizes.
