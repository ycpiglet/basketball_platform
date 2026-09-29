---
id: 2026_05_13_pilot_scoreboard_api_test_report
title: Pilot Scoreboard API Test Report
type: run
category: backend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: qa_debugger
tags:
  - run
  - test_report
  - scoreboard
related_runs:
  - harness/runs/2026-05-13_pilot_scoreboard_api/
---

# 05 Test Report

## Automated

- Pass: `python -m compileall backend/app backend/tests`
- Pass: `git diff --check`
- Pass: Docker Python 3.11 targeted API test run:
  - `pytest tests/test_scoreboard_api.py`
  - Result: 9 passed.
- Pass: Docker Python 3.11 full backend verification:
  - `pytest`
  - Result: 28 passed.
  - `ruff check .`
  - Result: all checks passed.

## Environment Notes

- Host `python` and `python3` remain Python 3.10.12.
- Host `python3.11` is not on PATH.
- Host `ruff` is not installed.
- Verification used `python:3.11-slim` Docker image with the backend directory
  mounted read-only.

## Manual

- Manual review confirms:
  - State-changing scoreboard endpoints use backend role guardrails.
  - Guest/public reads are available for display/result routes.
  - No payment, credit, notification, ad, hardware, or production-auth behavior
    was added.
  - No sensitive personal/payment fields were introduced.

## Regression Cases

- Added `backend/tests/test_scoreboard_api.py` covering:
  - Public create/read flow.
  - Operator role guardrails.
  - Invalid role header.
  - Score event and player total aggregation.
  - Invalid score validation.
  - Non-blank correction reason.
  - Team foul, player foul, timeout, quarter, and clock transitions.
  - Finalized game mutation rejection.
  - Missing game not-found response.
