---
id: 2026_05_13_frontend_scoreboard_api_connection_deployment
title: Frontend Scoreboard API Connection Deployment
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
  - harness/runs/2026-05-13_frontend_scoreboard_api_connection/
---

# 07 Deployment

Production deployment is not in scope for this run.

Local dev servers started for review:

- Backend API: `http://localhost:8000`
- Frontend Vite: `http://localhost:5173`

Backend runs through Docker `python:3.11-slim`; frontend runs through Vite.
