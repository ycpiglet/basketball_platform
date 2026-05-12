# Task Lifecycle

Use this workflow for any task that needs more than a quick single-file change.

## 1. Intake

- Read `summary/status.md`.
- Read relevant compound records from `harness/compound/index.md`.
- Create `harness/runs/YYYY-MM-DD_short_slug/`.
- Copy files from `harness/runs/_template/`.
- Fill `00_context.md` before implementation.

## 2. Planning

- Fill `01_plan.md`.
- Mark Phase 1/MVP or Phase 2.
- Capture permission, logging, validation, and test expectations.
- Record which compound records and existing assets will be reused.

## 2.5 Sandbox

Use `harness/sandbox/` before implementation when the approach is uncertain,
risky, or likely to be discarded.

- Record the hypothesis and attempts.
- Keep failed experiments; mark them rejected or deferred.
- Promote only after the sandbox promotion review is satisfied.

## 3. Generation

- Implement narrowly against the plan.
- Record changed files and command output summaries in `02_work_log.md`.
- Record blockers in `03_issue_log.md`.
- Record root-cause notes in `04_debug_log.md`.
- Record what was reused, adapted, rejected, or avoided.

## 4. Evaluation

- Run the repository's existing test commands.
- Record automated and manual checks in `05_test_report.md`.
- Record review findings and pass/fail decision in `06_evaluation.md`.
- Identify durable lessons for `harness/compound/`.

## 5. Compound

- Create or update compound records for durable lessons, current state, reusable
  patterns, or repeated issues.
- Include YAML frontmatter.
- State what to reuse, what to avoid, and what to do next.
- Mark obsolete compound records as `superseded`; do not delete them.

## 6. Deployment Readiness

- Fill `07_deployment.md` only when deployment or release preparation is in
  scope.
- Keep secrets and environment values out of harness files.

## 7. Closeout

- Fill `08_final_summary.md`.
- Update `summary/status.md` with the latest run and unresolved follow-ups.
