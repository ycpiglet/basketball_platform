# 01 Plan

## Goal

- Move the root `SKILL.md` into the harness area as a project-local reusable
  skill.
- Document the trigger: use it for Python implementation, review, refactor,
  backend tests, scripts, document processing, and integrations.
- Update role docs and run templates so planner, generator, and evaluator know
  when to apply it.

## Acceptance Criteria

- Root `SKILL.md` is no longer the canonical location.
- Canonical skill path is `harness/skills/python_coding/SKILL.md`.
- `README.md`, `AGENTS.md`, and `harness/README.md` reference the skill.
- Planner/generator/evaluator guidance references the skill.
- Run templates include applicable skill tracking.

## Applicable Skills

- Python coding: Reviewed as input. No executable Python changes were made.

## Tasks

| Status | Owner | Task | Notes |
|---|---|---|---|
| Done | Planner | Classify the file as a project-local Python coding skill | Phase 1 docs/harness scope. |
| Done | Generator | Move the file under `harness/skills/python_coding/` | Preserved `SKILL.md` filename. |
| Done | Generator | Update root and harness documentation | Added trigger and usage rules. |
| Done | Evaluator | Verify layout and diff hygiene | `git diff --check` passed. |

## Test Plan

- Automated: `git diff --check`.
- Manual: confirm root `SKILL.md` is gone and canonical file exists under
  `harness/skills/python_coding/SKILL.md`.
- Not applicable: backend/frontend test runners because no executable code
  changed.

## Risks

- Repository-local skills are not automatically installed into global Codex
  skill discovery. Mitigation: `AGENTS.md` explicitly requires agents to read
  the project-local skill when Python work applies.
