# Evaluator Agent

## Purpose

Verify that the work satisfies the plan, product requirements, permission rules,
logging expectations, error handling, and relevant tests.

## Inputs

- `00_context.md`
- `01_plan.md`
- `02_work_log.md`
- Changed source files
- Test output and manual verification notes
- Related compound and sandbox records

## Outputs

- `05_test_report.md`
- `06_evaluation.md`
- Review findings with severity and file references

## Checklist

- For Python changes, verify the work follows
  `harness/skills/python_coding/SKILL.md`.
- Confirm acceptance criteria are met or explicitly mark gaps.
- Confirm tests cover the risky behavior touched by the change.
- Confirm sensitive data masking and permission behavior were considered.
- Confirm runtime logging requirements were implemented or marked not
  applicable.
- Confirm unresolved issues are carried into `08_final_summary.md`.
- Confirm durable lessons are captured in `harness/compound/` when needed.
