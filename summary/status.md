---
id: project_status
title: Project Status
type: status
category: harness
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - status
  - current_state
  - field_pilot
  - compound
related_runs:
  - harness/runs/2026-05-12_frontend_public_prototype_ui_migration/
related_files:
  - docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md
  - harness/compound/index.md
---

# Project Status

## Latest Harness Run

- `harness/runs/2026-05-12_frontend_public_prototype_ui_migration/`

## Current Direction

- Phase 1 / MVP remains the default implementation scope.
- Current immediate goal: prepare a small field pilot for a real amateur
  basketball club or practice game.
- Current implementation stage: pre-alpha frontend demo. The Vue UI now follows
  the `public/index.html` field-pilot direction, but it is still demo-state only
  and not connected to backend game state.
- Harness engineering records should live under `harness/`.
- Use `harness/runs/YYYY-MM-DD_short_slug/` for task-specific multi-agent
  work.
- Use `harness/sandbox/` for isolated experiments and promotion reviews.
- Use `harness/compound/` for synthesized lessons, current state, reusable
  patterns, and mistakes to avoid.
- Use `harness/skills/python_coding/SKILL.md` for Python implementation,
  review, refactor, backend test, script, PDF parsing, and integration work.
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

- Coordinator: run setup, handoff alignment, final summary.
- Planner: requirement trace, plan, acceptance criteria.
- Generator: implementation, work log, debugging notes.
- Evaluator: tests, review, verification decision.

## Open Items

- Implement field pilot vertical slice:
  - Backend pilot scoreboard API
  - Replace frontend demo state with backend state
  - Display route sync from backend state
  - Result and box score generated from backend state
  - Tests and dry-run checklist
- Run mobile/tablet/TV visual QA for the redesigned frontend.
- Decide whether root `public/index.html` should be tracked as a prototype
  reference or moved under docs.
- Fix backend test environment:
  - Use Python 3.11+
  - Install backend dev dependencies
  - Re-run `pytest` and `ruff check .`
- Keep compound records updated when backend environment, pilot scope, or
  implementation strategy changes.
- Link future run summaries from this file.
- Decide whether empty local root folders `issues/` and `logs/` should be
  removed or kept as scratch space.
- Decide later whether the Python coding skill should also be installed into
  global/local Codex skill discovery outside this repository.
