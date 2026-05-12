# 03 Issue Log

| ID | Severity | Status | Area | Summary | Owner | Next Step |
|---|---|---|---|---|---|---|
| FP-001 | High | Open | Backend | Backend API routes are mostly placeholders and cannot yet operate a live pilot game. | Backend | Implement pilot scoreboard state API over `ScoreboardStateService`. |
| FP-002 | High | Open | Frontend / Backend | Frontend scoreboard control and display routes are not connected to backend state. | Frontend / Backend | Build one connected vertical slice. |
| FP-003 | High | Open | Backend test environment | Backend tests fail locally under Python 3.10 and missing dependencies. | Backend / DevOps | Use Python 3.11+ and install backend dev dependencies. |
| FP-004 | Medium | Open | Persistence | Game state persistence is not ready. | Backend / Database | Add pilot store or mandatory export fallback. |
| FP-005 | Medium | Open | Permissions | Production auth is not implemented; pilot role enforcement needs backend guardrails before exposure. | Backend | Add controlled pilot role checks to state-changing endpoints. |

## Scope Questions

- Should the first pilot use a real roster or anonymized/demo player names?
- Should first pilot persistence be PostgreSQL-backed or explicitly marked
  pilot-only in-memory state with export?
- Is one club practice game enough for the first feedback cycle, or should two
  sessions be planned from the start?

## Blockers

- Backend test environment mismatch must be fixed before reliable backend
  implementation verification.
- A field pilot should not happen until control, display, event log, and result
  view share the same backend state.

