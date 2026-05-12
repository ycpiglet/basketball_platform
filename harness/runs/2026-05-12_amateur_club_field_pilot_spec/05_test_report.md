# 05 Test Report

## Automated Tests

| Command | Result | Notes |
|---|---|---|
| `npm run test -- --run` in `frontend/` | Passed | 2 files, 5 tests passed. |
| `pytest` in `backend/` | Failed | Collection failed due to Python 3.10 runtime and missing dependencies; recorded in issue/debug logs. |
| `git diff --check` | Passed | Markdown/docs patch hygiene only. |

## Manual Checks

| Scenario | Result | Evidence |
|---|---|---|
| Field pilot spec created | Passed | `docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md`. |
| Original requirements preserved | Passed | Root requirements unchanged; archive summary added. |
| Acceptance test case created | Passed | `harness/test_cases/v_model/acceptance_test/tc_acceptance_amateur_club_field_pilot.md`. |
| Issue and debug records added | Passed | `harness/issue_log/` and `harness/debugging/` entries. |
| Status points to latest run and field pilot spec | Passed | `summary/status.md`. |

## Coverage Notes

- Score updates: planned for pilot API and existing service tests, but backend
  tests currently blocked by environment.
- Timer transitions: planned.
- Player/team foul updates: planned.
- Box score aggregation: planned.
- Permission checks: planned for pilot API.
- Sensitive data masking: considered; first pilot should avoid sensitive data.
- PDF fallback to `N/A`: not part of first field pilot vertical slice.
- API validation failures: planned for pilot API.
- Frontend critical flow: existing route tests pass, but connected control flow
  is not implemented.

## Skipped Tests

| Test | Reason | Risk |
|---|---|---|
| Backend passing test suite | Environment mismatch and missing dependencies; failure recorded as issue FP-003. | High for backend implementation readiness. |
| Full field pilot acceptance test | Product is not connected enough yet. | Expected until vertical slice is implemented. |
