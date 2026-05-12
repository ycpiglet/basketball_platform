# Harness Engineering Workspace

This directory keeps multi-agent work aligned across planning, implementation,
evaluation, debugging, testing, validation, and deployment notes.

## Scope

- Requirement domain: Phase 1 / MVP operating discipline, documentation, tests,
  and verification support.
- Affected layers: docs, tests, operations, and agent workflow records.
- Permission model: no product permission behavior is defined here. Any product
  permission change must still be implemented in backend/API code and tested.
- Logging model: this is an engineering record system, not runtime application
  logging. Runtime logs still belong in backend/frontend logging facilities.
- Test model: test cases and test reports here must point to the actual test
  runner output from `backend/tests`, `frontend/src/tests`, or manual checks.

## Directory Map

```text
harness/
|- README.md
|- agents/
|  |- README.md
|  |- coordinator.md
|  |- planner.md
|  |- generator.md
|  |- evaluator.md
|- workflows/
|  |- task_lifecycle.md
|  |- handoff_protocol.md
|  |- plan_work_review_compound.md
|- skills/
|  |- README.md
|  |- python_coding/
|  |  |- SKILL.md
|- sandbox/
|  |- README.md
|  |- _template/
|  |- experiments/
|- compound/
|  |- README.md
|  |- index.md
|  |- state/
|  |- patterns/
|  |- lessons/
|  |- decisions/
|- runs/
|  |- README.md
|  |- _template/
|  |  |- 00_context.md
|  |  |- 01_plan.md
|  |  |- 02_work_log.md
|  |  |- 03_issue_log.md
|  |  |- 04_debug_log.md
|  |  |- 05_test_report.md
|  |  |- 06_evaluation.md
|  |  |- 07_deployment.md
|  |  |- 08_final_summary.md
|- test_cases/
|- validation/
|- decisions/
|- issue_log/
|- debugging/
|- deployment/
|- metadata_schema.md
```

## Naming Rules

- Use lowercase snake_case for directories and files.
- Use `YYYY-MM-DD_short_slug` for run folders, for example
  `2026-05-12_scoreboard_state_sync`.
- Prefix ordered run files with two digits so every agent reads them in the same
  sequence.
- Keep files short enough to scan. Link to source files, test output, PRs, or
  issue IDs instead of pasting long logs.

## Minimum Agent Loop

1. Coordinator opens or updates a folder under `harness/runs/`.
2. Planner reads `summary/status.md`, checks relevant records in
   `harness/compound/`, checks `harness/skills/`, then fills `00_context.md` and
   `01_plan.md`.
3. If the approach is uncertain, use `harness/sandbox/` before product edits.
4. Generator records implementation notes in `02_work_log.md`, and any blocking
   issues in `03_issue_log.md` or `04_debug_log.md`.
5. Evaluator writes `05_test_report.md` and `06_evaluation.md`.
6. Coordinator creates or updates compound records for durable lessons.
7. Coordinator updates `08_final_summary.md` and `summary/status.md`.

## Sandbox And Compound

- `harness/sandbox/` isolates experiments, spikes, and risky attempts before
  they become product work.
- `harness/compound/` synthesizes lessons, current state, patterns, and
  decisions from multiple runs so future agents can reuse what worked and avoid
  repeated mistakes.
- New harness documents should include YAML frontmatter following
  `harness/metadata_schema.md`.

## Skills

Reusable project skills live under `harness/skills/`.

- Use `harness/skills/python_coding/SKILL.md` whenever writing, reviewing, or
  refactoring Python code, including FastAPI backend code, repositories,
  services, models, schemas, tests, scripts, document processing, and
  integrations.
- A skill is an execution rule for agents. It does not replace the product
  requirements, does not authorize Phase 2 scope, and does not move permission
  checks out of backend/API code.

## Source Of Truth

Harness notes do not replace product requirements. Always resolve product scope
against:

1. `requirements_en.md`
2. `requirements_ko.md`
3. `README.md`
4. `AGENTS.md`
