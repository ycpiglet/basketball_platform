---
id: 2026_05_12_amateur_club_field_pilot_spec
title: Amateur Club Field Pilot Specification
type: requirements
category: field_pilot
status: draft
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - field_pilot
  - scoreboard
  - digital_scorekeeping
  - display_route
  - feedback
related_runs:
  - harness/runs/2026-05-12_amateur_club_field_pilot_spec/
  - harness/runs/2026-05-12_sandbox_compound_framework/
related_tests:
  - harness/test_cases/v_model/acceptance_test/tc_acceptance_amateur_club_field_pilot.md
---

# Amateur Club Field Pilot Specification

Date: 2026-05-12

Status: Draft for Phase 1 field pilot planning

Related run: `harness/runs/2026-05-12_amateur_club_field_pilot_spec/`

## 1. Purpose

The immediate goal is to create a small, usable prototype that can be applied to
a real amateur basketball club and used to collect feedback from scorekeepers,
team managers, players, and observers.

This document does not replace `requirements_en.md` or `requirements_ko.md`.
It narrows Phase 1 into a practical field pilot path.

## 2. Product Goal For The Pilot

Run one real or practice amateur basketball game using the web app for:

- Scoreboard control
- Digital scorekeeping
- External display through a browser route
- Basic game result review
- Feedback collection after use

The pilot is successful when a non-developer scorekeeper can operate a game with
limited guidance and the team can identify concrete usability, reliability, and
data-quality issues.

## 3. Phase Classification

- Phase: Phase 1 / MVP
- Explicitly out of scope:
  - Production payment, credit, wallet, ads, settlement, and reservation payment
  - Kakao AlimTalk, SMS, email notification integrations
  - Production hardware control through RS-485/RF devices
  - Production-grade authentication beyond the minimum needed for a controlled
    pilot

## 4. Current Repository Stage

Current stage: pre-alpha skeleton.

What exists:

- Vue + TypeScript frontend shell with MVP placeholder routes.
- FastAPI backend shell with API router structure, config, logging, exception
  handling, RBAC helper, models, schemas, and tests.
- Deterministic in-memory scoreboard state service draft.
- Harness documentation structure for planner, generator, evaluator,
  coordinator, skills, runs, validation, issues, debugging, tests, and status.

What is not ready:

- Real API endpoints for live scoreboard state changes.
- Frontend connection to backend game state.
- Persistent game storage.
- Production authentication and ownership enforcement.
- WebSocket or polling-based live display synchronization.
- Field-ready error/retry UX.
- Deployment runbook for a pilot environment.

## 5. Pilot Users And Roles

| Role | Pilot Responsibility | Product Permission Model |
|---|---|---|
| Scorekeeper | Operates score, timer, fouls, period, and finalization | Team Manager or controlled pilot operator |
| Team manager | Sets up teams, roster, and game metadata | Team Manager |
| Player | Reviews roster and result | User |
| Observer / audience | Views scoreboard display | Guest |
| System administrator | Creates pilot data, monitors issues, exports results | System Administrator |

Privacy rule: sensitive member information must be masked by default unless the
user role explicitly allows access. The pilot should avoid collecting sensitive
payment, address, bank, or card data.

## 6. Pilot Functional Scope

### 6.1 Must Have

- Create or load one demo/pilot game.
- Configure home and away teams.
- Add 1, 2, and 3 point scores.
- Correct score with an auditable reason.
- Add team fouls.
- Add player fouls.
- Start and stop the game clock.
- Set period/quarter and remaining time.
- Use timeout.
- Finalize game.
- Show scoreboard display route without admin controls.
- Show game result summary and basic box score.
- Record event log for every score, timer, foul, timeout, period, and final
  action.
- Provide basic validation and clear error messages.
- Run on mobile/tablet for control and on a large TV/monitor for display.

### 6.2 Should Have

- Simple roster setup for both teams.
- Box score totals per player.
- Undo/correction workflow that records why the correction happened.
- Manual feedback form or issue collection template after each pilot game.
- Exportable game result summary.

### 6.3 Could Have

- QR code or share link for result viewing.
- Basic PDF export for result printing.
- Manual import from a standard score sheet template.

## 7. Data And Persistence Strategy

For the first field pilot, prefer the smallest persistence model that can avoid
losing game data:

1. Backend API owns game state changes.
2. PostgreSQL stores game, teams, players, participants, and final result
   records when implemented.
3. MongoDB stores high-volume or flexible event logs when implemented.
4. If full persistence is not ready, use a clearly marked pilot-only in-memory
   store with manual export before shutdown.

Do not duplicate authoritative state across stores without a documented
synchronization rule.

## 8. Pilot Workflow

### 8.1 Before Game Day

1. Select one club or practice game.
2. Confirm the venue has stable network and a TV/monitor with HDMI or browser
   access.
3. Prepare demo teams, players, and game rules.
4. Run backend and frontend smoke tests.
5. Run a dry-run game internally.
6. Prepare a rollback path: paper score sheet and manual scoreboard.
7. Prepare a feedback collection form.

### 8.2 On Game Day

1. Open control route on scorekeeper tablet or laptop.
2. Open display route on TV/monitor.
3. Confirm home/away teams, period length, timeout rules, and roster.
4. Operate the game through the app.
5. Record every bug, confusion point, latency issue, and manual workaround.
6. Export or save final game result.
7. Collect feedback from scorekeeper, manager, players, and observers.

### 8.3 After Game Day

1. Save game event log and final result.
2. Classify feedback into usability, data integrity, performance, permission,
   and missing feature categories.
3. Convert confirmed issues into `harness/issue_log/`.
4. Update `summary/status.md` with the latest pilot result.
5. Choose the next vertical slice based on the highest field risk.

## 9. Implementation Work Packages

| ID | Work Package | Layer | Acceptance Criteria |
|---|---|---|---|
| FP-001 | Pilot game state API | Backend | Score, foul, timer, timeout, quarter, finalization endpoints validate input and return structured errors. |
| FP-002 | Pilot state store | Backend / Database | Game state survives the pilot session or has a documented manual export fallback. |
| FP-003 | Scoreboard control UI | Frontend | Large tap targets, clear state, loading/error/retry states, mobile/tablet usable. |
| FP-004 | Display route sync | Frontend / Backend | Display route updates from backend state and exposes no admin controls. |
| FP-005 | Digital score sheet | Frontend / Backend | Player-level points and fouls update deterministic totals. |
| FP-006 | Result and box score view | Frontend / Backend | Final score, player points, fouls, and event summary are visible after game finalization. |
| FP-007 | Pilot RBAC guardrails | Frontend / Backend | Guests can view display/result only; score changes require operator/team-manager/admin role. |
| FP-008 | Runtime logs | Backend | Score, timer, foul, timeout, quarter, correction, and finalization actions emit structured logs. |
| FP-009 | Field feedback workflow | Docs / Operations | Feedback template and issue triage process are ready before game day. |
| FP-010 | Pilot deployment runbook | Operations | Start, verify, rollback, and post-game export steps are documented. |

## 10. Testing And Validation

Minimum automated tests before field use:

- Score updates for 1, 2, and 3 points.
- Invalid score values are rejected.
- Timer start/stop and remaining time validation.
- Team foul and player foul updates.
- Score correction requires reason and creates an auditable event.
- Finalized game rejects further state changes.
- Permission checks for score-changing endpoints.
- Sensitive fields are masked by default.
- API validation failures return structured errors.
- Frontend routes for control, display, live record, and result render.

Minimum manual checks before field use:

- Control screen works on a phone-sized viewport.
- Control screen works on a tablet/laptop.
- Display route is readable on the target TV/monitor.
- Display route has no admin controls.
- Operator can recover from a normal API failure without page crash.
- A full dry-run game can be completed from setup to result review.

## 11. Feedback Metrics

Collect:

- Scorekeeper task completion time.
- Number of correction events.
- Number of accidental taps or wrong entries.
- Confusing labels or controls.
- Display readability comments.
- Network or sync delays.
- Missing data needed after the game.
- Bugs that forced paper/manual fallback.

## 12. Known Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Backend is still mostly placeholder | Pilot cannot operate real game state | Build FP-001 to FP-006 as a thin vertical slice first. |
| Python runtime mismatch | Backend tests fail in Python 3.10 | Use Python 3.11+ and install backend dev dependencies. |
| No persistence | Game data can be lost | Add pilot state store or mandatory export before shutdown. |
| No production auth | Unauthorized state changes possible outside controlled pilot | Limit pilot access and add backend role checks before public exposure. |
| Display sync not implemented | TV scoreboard can drift from control panel | Implement polling or WebSocket sync for pilot. |
| Non-technical operation risk | Scorekeeper may be blocked during live game | Run dry-run and keep paper fallback. |

## 13. Next Planning Recommendation

Next implementation should focus on one vertical slice:

1. Backend pilot scoreboard API over the existing `ScoreboardStateService`.
2. Frontend control route connected to that API.
3. Display route reading the same backend state.
4. Result view generated from final state.
5. Tests and a dry-run script/checklist.

Do not start Phase 2 commercial features until the field pilot validates game
operation usability and data reliability.
