---
id: 2026_05_12_sandbox_compound_framework_plan
title: Sandbox Compound Framework Plan
type: run
category: harness
status: complete
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - run
  - plan
  - sandbox
  - compound
related_runs:
  - harness/runs/2026-05-12_sandbox_compound_framework/
---

# 01 Plan

## Goal

- Add sandbox as the place for isolated experiments and promotion reviews.
- Add compound as the durable synthesis layer across runs, issues, debugging,
  tests, decisions, and sandbox results.
- Add YAML frontmatter schema for searchability.
- Update run templates and workflow docs so future work uses this structure by
  default.
- Create initial compound records from current project history.

## Acceptance Criteria

- `harness/sandbox/` exists with README and templates.
- `harness/compound/` exists with README, index, template, and current records.
- `harness/metadata_schema.md` defines frontmatter.
- New run templates include frontmatter and compound/reuse sections.
- `summary/status.md`, `README.md`, and `AGENTS.md` explain how to use sandbox
  and compound.
- Current known issues and field-pilot context are synthesized into compound
  records.

## Applicable Skills

- Python coding: N/A.

## Reuse Plan

- Compound records read:
  - Created during this run from existing field pilot and backend environment
    records.
- Existing code/docs to reuse:
  - Existing run templates, task lifecycle, status, issue/debug records.
- Sandbox experiments to consult:
  - None.
- Work not to recreate:
  - Existing field pilot spec and backend environment issue records.

## Tasks

| Status | Owner | Task | Notes |
|---|---|---|---|
| Done | Planner | Define sandbox vs compound responsibilities | Sandbox isolates attempts; compound preserves durable lessons. |
| Done | Generator | Add metadata schema | YAML frontmatter fields and search examples. |
| Done | Generator | Add sandbox docs/templates | Experiment brief, attempt log, result, promotion review. |
| Done | Generator | Add compound docs/templates/index | State, lesson, pattern records. |
| Done | Generator | Update run templates and workflows | Added frontmatter, reuse, and compound sections. |
| Done | Generator | Update status/README/AGENTS | New usage guidance. |
| Done | Evaluator | Verify file layout and diff hygiene | `git diff --check` passed; sandbox/compound files listed. |

## Test Plan

- Automated:
  - `git diff --check`
- Manual:
  - Confirm sandbox and compound files exist.
  - Confirm frontmatter exists in new templates and key records.
  - Confirm status points to latest run and compound index.
- Not applicable:
  - Backend/frontend test runners; no executable product code changed.

## Risks

- Too much metadata can become noise. Mitigation: schema has required fields and
  optional fields; compound records should stay concise.
- Compound can drift from source truth. Mitigation: compound records must link
  evidence and cannot override product requirements.
