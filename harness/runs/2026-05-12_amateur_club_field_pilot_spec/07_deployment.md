# 07 Deployment

## Applicability

- Deployment in scope: Planning only
- Environment: Future small pilot environment
- Release owner: TBD

## Pre-Deployment Checks

- Backend tests pass under Python 3.11+.
- Frontend tests pass.
- Control, display, and result routes use the same backend game state.
- Display route exposes no admin controls.
- Paper score sheet fallback is available.
- Pilot feedback form is ready.

## Deployment Steps

1. Build frontend.
2. Start backend with pilot configuration.
3. Verify health endpoint.
4. Open control route on operator device.
5. Open display route on TV/monitor.
6. Run dry-run game before field use.

## Rollback Plan

- Stop using the app during the game.
- Continue with paper score sheet and manual scoreboard.
- Preserve any exported partial event logs.
- Record the failure in `harness/issue_log/`.

## Post-Deployment Verification

- Confirm final score and event log.
- Collect scorekeeper/team manager/player feedback.
- Update `summary/status.md`.
- Convert confirmed field issues into harness issue records.

