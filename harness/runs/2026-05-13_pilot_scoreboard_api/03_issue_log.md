---
id: 2026_05_13_pilot_scoreboard_api_issue_log
title: Pilot Scoreboard API Issue Log
type: run
category: backend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: engineering_manager
tags:
  - run
  - issue_log
  - scoreboard
related_runs:
  - harness/runs/2026-05-13_pilot_scoreboard_api/
related_issues:
  - harness/issue_log/2026-05-12_backend_test_environment.md
---

# 03 Issue Log

## Issues

| Status | Severity | Owner | Issue | Resolution |
|---|---|---|---|---|
| Mitigated | High | Backend / DevOps | Python 3.11 is not available on PATH, blocking host backend test execution. | Used `python:3.11-slim` Docker container to run backend tests. Host setup is still a follow-up. |
| Mitigated | Medium | Backend / DevOps | `ruff` is not installed in the active host environment. | Used `ruff` inside the Python 3.11 Docker verification container. Host setup is still a follow-up. |

## Open Questions

- None for FP-001. Production authentication remains explicitly out of scope.
