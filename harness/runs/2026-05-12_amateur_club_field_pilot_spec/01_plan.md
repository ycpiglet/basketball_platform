# 01 Plan

## Goal

- Define the first practical deployment goal: a real amateur club field pilot.
- Convert the broad Phase 1 MVP into a concrete pilot specification.
- Preserve original requirements instead of overwriting them.
- Record current work, known issues, debugging, tests, validation, and next
  planning in the harness structure.

## Acceptance Criteria

- A dated field pilot specification exists under `docs/requirements/`.
- A dated summary of original source requirements exists under
  `docs/requirements/archive/`.
- Harness records describe the goal, plan, work, issues, debugging, tests,
  validation, deployment readiness, and next step.
- `summary/status.md` explains how future agents should use the new documents.
- Existing source requirements are preserved.

## Applicable Skills

- Python coding: N/A for docs-only work.

## Tasks

| Status | Owner | Task | Notes |
|---|---|---|---|
| Done | Planner | Classify field pilot as Phase 1 / MVP | Commercial Phase 2 excluded. |
| Done | Planner | Define pilot work packages and procedures | Added field pilot spec. |
| Done | Planner | Add requirements preservation rule | Added requirements README and archive summary. |
| Done | Generator | Add acceptance test and validation trace | Added acceptance test case and matrix rows. |
| Done | Generator | Record known backend test environment issue | Added issue and debugging notes. |
| Done | Evaluator | Verify Markdown and final status links | `git diff --check` passed; status inspected. |

## Test Plan

- Automated:
  - `git diff --check`
- Manual:
  - Confirm field pilot spec exists.
  - Confirm requirements archive summary exists.
  - Confirm status points to new spec and run.
  - Confirm validation matrices reference the acceptance test.
- Not applicable:
  - Backend and frontend executable tests for this docs-only change.

## Risks

- A pilot spec can be mistaken for a replacement of the full requirements.
  Mitigation: source preservation rule and archive summary explicitly state
  that root requirements remain authoritative.
- The current product is not ready for field use. Mitigation: spec labels the
  current stage as pre-alpha skeleton and defines the next vertical slice.
