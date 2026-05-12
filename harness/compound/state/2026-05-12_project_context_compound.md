---
id: 2026_05_12_project_context_compound
title: Project Context Compound
type: compound
category: field_pilot
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - current_state
  - field_pilot
  - pre_alpha
  - scoreboard
  - handoff
related_runs:
  - harness/runs/2026-05-12_harness_structure/
  - harness/runs/2026-05-12_python_coding_skill_location/
  - harness/runs/2026-05-12_amateur_club_field_pilot_spec/
  - harness/runs/2026-05-12_frontend_public_prototype_ui_migration/
related_files:
  - summary/status.md
  - docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md
  - backend/app/services/scoreboard_state.py
related_issues:
  - harness/issue_log/2026-05-12_backend_test_environment.md
related_debug:
  - harness/debugging/2026-05-12_backend_pytest_collection_failure.md
search_terms:
  - current project state
  - field pilot readiness
  - connected prototype
---

# Project Context Compound

## Synthesis

The current goal is a Phase 1 field pilot for a real amateur basketball club or
practice game. The repository is not field-operable yet. The frontend now has a
demo UI based on `public/index.html`, while backend routes are still mostly
placeholder APIs and game state is not connected to the frontend.

## Evidence

- Field pilot scope is defined in
  `docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md`.
- Current status is summarized in `summary/status.md`.
- Scoreboard domain logic exists in `backend/app/services/scoreboard_state.py`.
- Backend routes are mostly placeholders.
- Frontend control/display/result views now use static demo state in
  `frontend/src/shared/demo/pilotGame.ts`.

## Reuse

- Reuse `ScoreboardStateService` for the pilot scoreboard API.
- Reuse `frontend/src/shared/demo/pilotGame.ts` for static UI until backend
  pilot APIs exist.
- Reuse the field pilot work packages FP-001 to FP-010.
- Reuse the acceptance test case in
  `harness/test_cases/v_model/acceptance_test/tc_acceptance_amateur_club_field_pilot.md`.
- Reuse the run templates in `harness/runs/_template/`.

## Avoid

- Do not start Phase 2 payment, credit, notification, ad, or reservation payment
  work before the field pilot validates game operation.
- Do not rewrite requirements documents in place.
- Do not treat frontend router guards as the only permission enforcement.
- Do not run backend tests under Python 3.10 and assume failures are product
  failures.
- Do not treat static frontend demo state as authoritative game state.

## Next Actions

- Fix backend Python 3.11+ dev environment.
- Implement backend pilot scoreboard API over `ScoreboardStateService`.
- Connect frontend control route to backend state.
- Sync display route from the same backend state.
- Generate result and basic box score from backend state.
- Run mobile/tablet/TV visual QA, backend/frontend tests, then a dry-run game.
