---
id: 2026_05_13_pilot_scoreboard_api_debug_log
title: Pilot Scoreboard API Debug Log
type: run
category: backend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: qa_debugger
tags:
  - run
  - debug_log
  - scoreboard
related_runs:
  - harness/runs/2026-05-13_pilot_scoreboard_api/
---

# 04 Debug Log

## Environment Blocker

`pytest tests/test_scoreboard_api.py` from `backend/` failed during collection:

- Runtime: Python 3.10.12
- Failure: `ImportError: cannot import name 'StrEnum' from 'enum'`
- Root cause: backend declares Python `>=3.11`; Python 3.10 cannot import
  `enum.StrEnum`.

This is the same environment class recorded in
`harness/issue_log/2026-05-12_backend_test_environment.md`.

## Product Defects

- No confirmed product defect. The new API tests passed under Docker Python
  3.11.15.

## Resolution

Docker-based Python 3.11 verification completed after the environment blocker:

- Image: `python:3.11-slim`
- Python: 3.11.15
- Targeted API tests: 9 passed
- Full backend tests: 28 passed
- Ruff: all checks passed

Host Python 3.11 and host `ruff` remain unavailable, so local host setup is still
an operational follow-up.
