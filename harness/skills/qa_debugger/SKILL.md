---
id: qa_debugger_skill
title: QA Debugger Skill
type: skill
category: harness
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - qa
  - debugging
  - regression
  - adversarial_testing
related_files:
  - harness/agents/qa_debugger.md
---

# QA Debugger Skill

Use this skill when designing tests, reviewing a change, reproducing bugs,
stress-testing assumptions, doing beta-user checks, or converting failures into
regression cases.

## Required Posture

- Intentionally try strange, hostile, repeated, out-of-order, and field-realistic
  actions.
- Treat every fixed bug as a future regression unless a test or test case records
  it.
- Separate observed facts from suspected causes.
- Do not close a defect just because it cannot be reproduced once.

## Inputs

- Acceptance criteria from `01_plan.md`
- Changed files and work log
- Existing automated tests and manual test cases
- `harness/test_cases/`
- Issue logs, debug logs, and beta feedback

## Workflow

1. Build normal, boundary, negative, interrupted, repeated, and role-based test
   scenarios.
2. Attempt to trigger failures through invalid input, rapid repeated actions,
   stale state, permission mismatch, network/API errors, viewport changes, and
   manual correction flows.
3. For every defect, record:
   - Steps to reproduce.
   - Expected result.
   - Actual result.
   - Environment and data used.
   - Severity.
   - Suspected owner.
   - Regression test location or planned test case.
4. Put root-cause investigation notes in `04_debug_log.md`.
5. Put test results in `05_test_report.md`.
6. Promote repeated or high-value lessons to `harness/compound/`.

## Communication Rules

- Report blocking defects to Engineering Manager immediately.
- Give Lead Staff Engineer reproduction evidence, not guesses.
- Escalate product ambiguity to Founder Product Lead.
- Ask Technical Writer to link durable test cases and lessons.

## Completion Check

- New or changed behavior has pass/fail evidence.
- Bugs have reproducible records or explicit non-repro status.
- Regression cases are recorded for future upgrades.
