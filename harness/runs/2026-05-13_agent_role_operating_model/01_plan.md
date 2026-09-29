---
id: 2026_05_13_agent_role_operating_model_plan
title: Agent Role Operating Model Plan
type: run
category: harness
status: complete
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: engineering_manager
tags:
  - run
  - plan
  - agent_roles
related_runs:
  - harness/runs/2026-05-13_agent_role_operating_model/
---

# 01 Plan

## Goal

- Consolidate 12 requested human-like roles into the smallest clear operating
  team, add matching role files and `SKILL.md` files, and wire the model into
  plan-work-review-compound records.

## Acceptance Criteria

- Role count and consolidation rationale are explicit.
- Each operating role has a `harness/agents/*.md` file.
- Each operating role has a matching `harness/skills/*/SKILL.md`.
- Hierarchy, reporting, escalation, and "do not guess" rules are documented.
- QA Debugger responsibilities include adversarial testing and regression-case
  capture.
- Security Release Engineer responsibilities include CI/CD, permission, privacy,
  and release gates.
- Summary and compound records point future agents to the operating model.

## Applicable Skills

- Engineering Manager: applies to role consolidation and hierarchy.
- Technical Writer: applies to run records and compound/status updates.
- Python coding: N/A.

## Reuse Plan

- Compound records read:
  - `harness/compound/patterns/2026-05-12_plan_work_review_compound_pattern.md`
  - `harness/compound/state/2026-05-12_project_context_compound.md`
- Existing code/docs to reuse:
  - `harness/agents/README.md`
  - `harness/skills/README.md`
  - Existing Planner/Generator/Evaluator/Coordinator files
- Sandbox experiments to consult: None.
- Work not to recreate: Product requirements or runtime implementation.

## Tasks

| Status | Owner | Task | Notes |
|---|---|---|---|
| Complete | Engineering Manager | Consolidate requested roles into operating model | 12 requested roles became 7 operating agents. |
| Complete | Technical Writer | Add agent files and role skill files | Added under `harness/agents/` and `harness/skills/`. |
| Complete | Technical Writer | Update workflow, compound, and status docs | Linked operating model from indexes. |
| Complete | Evaluator | Verify docs and file references | Documentation checks only. |

## Test Plan

- Automated: Not applicable; no runtime code changed.
- Manual:
  - Confirm expected agent and skill files exist.
  - Search for role names and operating model links.
  - Review `git diff --check` for whitespace issues.
- Not applicable:
  - Backend `pytest`, frontend tests, and CI/CD execution.

## Risks

- Future agents may confuse operating roles with workflow lanes. Mitigation:
  `harness/agents/README.md` now distinguishes both.
- Consolidated roles may need splitting later. Mitigation: compound record says
  not to split without explicit product-owner request.
