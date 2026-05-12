---
id: tc_acceptance_amateur_club_field_pilot
title: Amateur Club Field Pilot Acceptance Test
type: test_case
category: field_pilot
status: planned
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - acceptance_test
  - field_pilot
  - scoreboard
  - display_route
  - digital_scorekeeping
related_runs:
  - harness/runs/2026-05-12_amateur_club_field_pilot_spec/
related_files:
  - docs/requirements/2026-05-12_amateur_club_field_pilot_spec.md
---

# Acceptance Test: Amateur Club Field Pilot

## Goal

Verify that one real or practice amateur basketball game can be operated with
the prototype from setup through final result review.

## Preconditions

- Pilot game exists with home and away teams.
- Scorekeeper has an allowed operator role.
- Display route is open on a TV/monitor or second browser.
- Paper score sheet fallback is available.

## Scenario

1. Operator confirms teams, roster, period, and initial clock.
2. Operator starts the game clock.
3. Operator records 1, 2, and 3 point scoring events.
4. Operator records team fouls and player fouls.
5. Operator performs one score correction with a reason.
6. Display route reflects current score, time, period, and team fouls.
7. Operator finalizes the game.
8. Result view shows final score and player/team summaries.
9. Event log can explain score and foul totals.

## Expected Result

- Scorekeeper can complete the game without developer intervention.
- Display route remains readable and does not expose admin controls.
- State-changing actions are validated and logged.
- Final result is available for review.
- Feedback can be collected immediately after the game.

## Evidence To Capture

- Test date and venue
- Device/browser used for control
- Device/browser used for display
- Final score
- Number of corrections
- Issues observed
- Feedback summary
