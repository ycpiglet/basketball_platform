# 01 Plan

## Goal

- Make `harness/` the single coordination workspace for multi-agent engineering
  records.
- Define planner, generator, evaluator, and coordinator responsibilities.
- Add stable run templates for planning, work logs, issue logs, debugging,
  testing, evaluation, deployment, and final summaries.
- Update top-level project docs so future agents can discover the workflow.

## Acceptance Criteria

- `harness/README.md` explains scope, naming, and minimum agent loop.
- `harness/agents/` defines role responsibilities.
- `harness/runs/_template/` contains numbered, resumable files.
- `harness/test_cases/` and `harness/validation/` document verification
  organization.
- `README.md`, `AGENTS.md`, and `summary/status.md` point to the harness.

## Tasks

| Status | Owner | Task | Notes |
|---|---|---|---|
| Done | Planner | Map existing folders to the required workflow | Kept Phase 1 scope. |
| Done | Generator | Add harness docs and templates | Docs-only changes. |
| Done | Generator | Update README, AGENTS, and status index | No code paths changed. |
| Done | Evaluator | Run structural verification | `git diff --check` passed. |

## Test Plan

- Automated: `git diff --check`.
- Manual: inspect file layout and key docs.
- Not applicable: backend/frontend test runners, because no executable product
  code changed.

## Risks

- Too many run files can become overhead for very small tasks. Mitigation:
  leave sections as `N/A` for small tasks but keep file names stable.

