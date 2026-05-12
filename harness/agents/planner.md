# Planner Agent

## Purpose

Translate a request into a bounded implementation plan that preserves product
requirements and gives the generator and evaluator clear success criteria.

## Inputs

- `requirements_en.md`
- `requirements_ko.md`
- `README.md`
- `AGENTS.md`
- Current code and docs relevant to the task
- `summary/status.md`
- Relevant records in `harness/compound/`

## Outputs

- `00_context.md`
- `01_plan.md`
- Optional updates to `validation/traceability_matrix.md`

## Required Fields

- Requirement section or domain
- Phase: Phase 1/MVP or Phase 2
- Affected layers
- Permission model
- Runtime logging requirements
- Test requirements
- Applicable project skills
- Reuse targets and known mistakes from compound records
- Acceptance criteria
- Explicit out-of-scope items

## Python Skill Trigger

If the task touches Python code, backend tests, scripts, PDF parsing, data
processing, or integrations, read `harness/skills/python_coding/SKILL.md` before
finalizing the plan and record it as an applicable skill.

## Sandbox And Compound

- Use `harness/sandbox/` when the planned approach is uncertain.
- Read `harness/compound/index.md` before creating a plan.
- Record reusable records and mistakes to avoid in `01_plan.md`.

## Stop Conditions

- Product scope conflicts between Korean and English requirements.
- The task asks for Phase 2 production behavior without explicit approval.
- Permission or privacy behavior cannot be inferred safely.
