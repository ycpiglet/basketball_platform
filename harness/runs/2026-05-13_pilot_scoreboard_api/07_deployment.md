---
id: 2026_05_13_pilot_scoreboard_api_deployment
title: Pilot Scoreboard API Deployment
type: run
category: deployment
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: security_release_engineer
tags:
  - run
  - deployment
  - scoreboard
related_runs:
  - harness/runs/2026-05-13_pilot_scoreboard_api/
---

# 07 Deployment

Not in scope for this run. No production deployment or database migration should
be performed.

## Release Gate

- Backend tests and ruff passed under Docker Python 3.11.15.
- Host-local release tooling remains incomplete until Python 3.11+ and backend
  dev dependencies are installed on the host or documented as Docker-only.
- Header-based pilot role guardrails are not production authentication.
