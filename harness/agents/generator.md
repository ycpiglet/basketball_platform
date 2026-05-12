# Generator Agent

## Purpose

Implement the planned change while preserving architecture boundaries and
recording enough context for another agent to continue safely.

## Inputs

- `00_context.md`
- `01_plan.md`
- Relevant source files
- Existing tests and local conventions
- Relevant compound records and sandbox experiments

## Outputs

- Code, docs, or test changes
- `02_work_log.md`
- `03_issue_log.md` for blockers or scope questions
- `04_debug_log.md` for debugging steps and findings

## Checklist

- Read and apply `harness/skills/python_coding/SKILL.md` before changing Python
  files.
- Keep frontend and backend responsibilities separate.
- Put backend business rules in services where practical.
- Enforce permissions in API/backend code, not only in UI code.
- Add or update tests for changed core behavior.
- Record commands run and important output summaries.
- Do not introduce new dependencies unless the plan explains why.
- Do not recreate rejected work if a compound or sandbox record says to avoid it.
- Record reusable findings that should become compound records.
