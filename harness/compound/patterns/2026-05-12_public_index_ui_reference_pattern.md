---
id: 2026_05_12_public_index_ui_reference_pattern
title: Public Index UI Reference Pattern
type: compound
category: frontend
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - frontend
  - ui_reference
  - public_index
  - vue
  - field_pilot
related_runs:
  - harness/runs/2026-05-12_frontend_public_prototype_ui_migration/
related_files:
  - public/index.html
  - frontend/src/shared/styles/base.css
  - frontend/src/shared/demo/pilotGame.ts
search_terms:
  - public index design
  - prototype UI reference
  - field pilot frontend
---

# Public Index UI Reference Pattern

## Synthesis

`public/index.html` is the visual and information-architecture reference for the
Phase 1 field pilot frontend. It should not be copied as single-file vanilla JS.
The Vue implementation should reuse its visual direction while preserving Vue
Router, component boundaries, TypeScript, and future backend API replacement.

## Evidence

- The frontend UI migration run redesigned the Vue app using the reference.
- `frontend/src/shared/demo/pilotGame.ts` centralizes demo state.
- `frontend/src/shared/styles/base.css` contains the prototype-inspired design
  system for the Vue app.

## Reuse

- Reuse the shared demo state until backend pilot APIs exist.
- Reuse route-level Vue components instead of screen switching.
- Reuse the public display route's nav-free behavior.

## Avoid

- Do not reintroduce localStorage as authoritative game state.
- Do not copy the single-file prototype's vanilla JS navigation.
- Do not expose admin controls on the display route.

## Next Actions

- Connect the UI to backend pilot scoreboard APIs.
- Run mobile/tablet/TV viewport visual QA.
- Decide whether `public/index.html` should be tracked as a docs prototype.

