---
id: 2026_05_12_frontend_public_prototype_ui_migration_plan
title: Frontend Public Prototype UI Migration Plan
type: run
category: frontend
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - frontend
  - ui
  - plan
  - field_pilot
related_runs:
  - harness/runs/2026-05-12_frontend_public_prototype_ui_migration/
---

# 01 Plan

## Goal

- Rework the Vue frontend shell so it visually follows `public/index.html`.
- Keep the app deployable on Vercel.
- Preserve existing routing and public display route behavior.
- Use demo state only; leave backend integration for the next slice.

## Acceptance Criteria

- App layout uses global/sub navigation style inspired by `public/index.html`.
- Home route becomes a field-pilot oriented operations landing page.
- Scoreboard control route has touch-first score/timer/foul/timeout controls.
- Public display route renders full-screen dark scoreboard with no admin nav.
- Live score sheet route shows player event entry and event log UI.
- Result route shows final score and basic box score UI.
- CRUD placeholder routes use the same visual language.
- Frontend tests/build/lint are run and recorded.

## Applicable Skills

- Python coding: N/A.

## Reuse Plan

- Compound records read:
  - `harness/compound/state/2026-05-12_project_context_compound.md`
- Existing code/docs to reuse:
  - `frontend/src/routes`
  - Existing route guard and public display meta.
  - `public/index.html` design direction.
- Sandbox experiments to consult:
  - None.
- Work not to recreate:
  - Do not recreate vanilla JS navigation/state from `public/index.html`.

## Tasks

| Status | Owner | Task | Notes |
|---|---|---|---|
| Done | Generator | Add shared demo pilot data | Reusable static state for routes. |
| Done | Generator | Replace shared styles with prototype-inspired system | Kept accessibility and mobile-first rules. |
| Done | Generator | Update layout and main routes | Preserved public display route without nav. |
| Done | Evaluator | Run frontend tests, lint, build | All passed. |

## Test Plan

- Automated:
  - `npm run test -- --run`
  - `npm run lint`
  - `npm run build`
- Manual:
  - Inspect route components for public display nav exclusion.
  - Start dev server and provide local URL.

## Risks

- `public/index.html` contains single-file prototype logic that should not be
  copied directly into Vue.
- Existing CSS may conflict with new names. Prefer replacing shared CSS cleanly.
