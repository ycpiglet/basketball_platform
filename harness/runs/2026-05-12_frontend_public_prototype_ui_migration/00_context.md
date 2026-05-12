---
id: 2026_05_12_frontend_public_prototype_ui_migration_context
title: Frontend Public Prototype UI Migration Context
type: run
category: frontend
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - frontend
  - ui
  - public_index_reference
  - field_pilot
  - vercel
related_runs:
  - harness/runs/2026-05-12_sandbox_compound_framework/
related_files:
  - public/index.html
  - frontend/src/shared/styles/base.css
  - frontend/src/app/layouts/AppLayout.vue
---

# 00 Context

## Request

- User request: Continue work. Frontend has been deployed through Vercel as a
  deployment test only. Actual UI design should follow `public/index.html`.
  Preserve enough records to resume if interrupted.
- Date: 2026-05-12
- Owner/coordinator: Codex

## Requirement Trace

- Requirement source:
  - `docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md`
  - `public/index.html` as UI/IA reference
  - `AGENTS.md` frontend, UI/accessibility, and Phase 1 rules
- Requirement section or domain:
  - Phase 1 field pilot frontend
  - Scoreboard control
  - Digital scorekeeping
  - Public scoreboard display
  - Result and box score view
- Phase: Phase 1 / MVP
- Out of scope:
  - Backend API integration
  - Production auth
  - Payment/credit/reservation/ad/notification features
  - Hardware control

## Applicable Skills

- Python coding: No.

## Reuse And Compound Check

- Relevant compound records:
  - `harness/compound/state/2026-05-12_project_context_compound.md`
  - `harness/compound/patterns/2026-05-12_plan_work_review_compound_pattern.md`
- Existing services/docs/templates to reuse:
  - `public/index.html` UI direction
  - Existing Vue Router structure
  - Existing dev role guard
- Known mistakes to avoid:
  - Do not replace Vue Router with single-file vanilla JS navigation.
  - Do not expose admin controls on public display route.
  - Do not implement Phase 2 commercial features.
- Sandbox needed: No. This is a direct UI migration from an existing prototype
  reference.

## Affected Layers

- Frontend: Vue components, styles, demo data.
- Backend: Not affected.
- Database: Not affected.
- Document processing: Not affected.
- Integration: Not affected.
- Tests: Frontend tests/build/lint.
- Docs: Harness/status records.

## Permission And Privacy

- Roles involved:
  - Guest for public display/result viewing.
  - Team Manager for scoreboard control/live sheet in current route guard.
- Ownership rules:
  - No backend ownership behavior changed.
- Sensitive fields:
  - Demo player names only; no real private data.
- API-level enforcement needed:
  - Later, when backend pilot API is implemented.

## Logging And Error Handling

- Runtime logs required: N/A for static demo UI.
- Error states to handle: UI includes static sync/status indicators only.
- Values that must never be logged: passwords, tokens, private keys, payment
  credentials, unnecessary personal data.

