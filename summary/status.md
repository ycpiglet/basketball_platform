---
id: project_status
title: Project Status
type: status
category: harness
status: active
created: 2026-05-12
updated: 2026-05-13
phase: phase1_mvp
tags:
  - status
  - current_state
  - field_pilot
  - compound
related_runs:
  - harness/runs/2026-05-13_cloud_observability_e2e_integrations/
  - harness/runs/2026-05-13_frontend_scoreboard_api_connection/
  - harness/runs/2026-05-13_pilot_scoreboard_api/
  - harness/runs/2026-05-13_agent_role_operating_model/
  - harness/runs/2026-05-12_frontend_public_prototype_ui_migration/
related_files:
  - docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md
  - harness/compound/index.md
  - harness/agents/README.md
  - harness/skills/README.md
  - backend/app/api/routes/scoreboard.py
  - frontend/src/features/scoreboard/ScoreboardControlView.vue
  - frontend/src/features/scoreboard/ScoreboardDisplayView.vue
  - docs/operations/cloud_integrations.md
---

# Project Status

## Latest Harness Run

- `harness/runs/2026-05-13_cloud_observability_e2e_integrations/`

## Current Direction

- Phase 1 / MVP remains the default implementation scope.
- Current immediate goal: prepare a small field pilot for a real amateur
  basketball club or practice game.
- Current implementation stage: pre-alpha connected scoreboard slice. The
  backend has a Docker-verified FP-001 pilot scoreboard API, and the Vue
  scoreboard control/display routes now read and mutate that backend state.
- Harness engineering records should live under `harness/`.
- Use `harness/runs/YYYY-MM-DD_short_slug/` for task-specific multi-agent
  work.
- Use `harness/sandbox/` for isolated experiments and promotion reviews.
- Use `harness/compound/` for synthesized lessons, current state, reusable
  patterns, and mistakes to avoid.
- Use `harness/skills/python_coding/SKILL.md` for Python implementation,
  review, refactor, backend test, script, PDF parsing, and integration work.
- Use the seven-agent operating model in `harness/agents/README.md` and the
  matching role skills under `harness/skills/*/SKILL.md` for substantial
  multi-agent work.
- Use `harness/compound/patterns/2026-05-13_agent_operating_model.md` before
  assigning expanded operating roles or splitting responsibilities.
- Use `harness/compound/state/2026-05-13_pilot_scoreboard_api_state.md` before
  continuing scoreboard API work or connecting frontend routes to backend state.
- Use
  `harness/compound/state/2026-05-13_frontend_scoreboard_api_connection_state.md`
  before continuing frontend scoreboard control or display sync work.
- Use `harness/compound/state/2026-05-13_cloud_integrations_state.md` before
  changing Vercel, Supabase, Sentry, Playwright, or deployment observability.
- Use `harness/compound/patterns/2026-05-12_public_index_ui_reference_pattern.md`
  before changing the frontend UI.

## Current Requirements Documents

- Source of truth remains:
  - `requirements_en.md`
  - `requirements_ko.md`
  - `README.md`
  - `AGENTS.md`
- Field pilot derived requirement:
  - `docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md`
- Source requirement archive summary for the pilot:
  - `docs/requirements/archive/2026-05-12_requirements_source_summary_for_field_pilot.md`

## How To Use This Status

- Start with the latest harness run for current context.
- Then read `harness/compound/index.md`.
- Read `harness/compound/state/2026-05-12_project_context_compound.md` before
  planning a new implementation slice.
- Use the field pilot spec when planning the next implementation slice.
- Use `docs/requirements/README.md` before creating or changing requirements
  documents.
- Do not delete or overwrite old requirement documents. Add a dated archive
  summary when deriving a new requirements document.
- Carry open issues from this file into the next run's `03_issue_log.md`.
- At the end of a substantial run, create or update a compound record before
  updating this status.

## Active Agent Roles

- Founder Product Lead: CEO/Founder, Product Manager, and Project Manager scope
  decisions.
- Engineering Manager: hierarchy, assignment, escalation, and delivery
  coordination.
- Lead Staff Engineer: Lead Engineer and Staff Engineer architecture,
  implementation direction, and conservative review.
- Senior Designer: field usability, responsive UI, accessibility, and visual QA.
- QA Debugger: QA Lead, Debugger, and Beta Tester/User adversarial testing and
  regression capture.
- Security Release Engineer: Security Engineer and CI/CD Engineer release,
  permission, privacy, and operational gates.
- Technical Writer: handoffs, durable records, compound synthesis, and status
  updates.
- Workflow lanes remain: Planner, Generator, Evaluator, Coordinator.

## Open Items

- Implement field pilot vertical slice:
  - Backend pilot scoreboard API implemented and verified through Docker Python
    3.11.15
  - Frontend control route connected to backend state
  - Display route polling backend state
  - Result and box score generated from backend state
  - Tests and dry-run checklist
- Run mobile/tablet/TV visual QA for the redesigned frontend.
- Decide whether root `public/index.html` should be tracked as a prototype
  reference or moved under docs.
- Fix backend test environment:
  - Host still lacks Python 3.11+ and `ruff`
  - Decide whether Docker Python 3.11 verification is the standard path or
    install host Python 3.11+ and backend dev dependencies
- Configure real Vercel/Supabase/Sentry environment variables outside git before
  any public pilot deployment.
- Keep compound records updated when backend environment, pilot scope, or
  implementation strategy changes.
- Link future run summaries from this file.
- Use QA Debugger to convert newly discovered bugs into regression cases before
  future feature upgrades are considered complete.
- Decide whether empty local root folders `issues/` and `logs/` should be
  removed or kept as scratch space.
- Decide later whether the Python coding skill should also be installed into
  global/local Codex skill discovery outside this repository.
