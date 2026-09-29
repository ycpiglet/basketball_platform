---
id: 2026_05_13_cloud_observability_e2e_integrations_plan
title: Cloud Observability E2E Integrations Plan
type: run
category: deployment
status: complete
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: lead_staff_engineer
tags:
  - plan
  - vercel
  - supabase
  - sentry
  - playwright
related_runs:
  - harness/runs/2026-05-13_cloud_observability_e2e_integrations/
---

# 01 Plan

## Goal

- Add cloud integration scaffolding for Vercel, Supabase, Sentry, and Playwright
  without requiring secrets in the repository.

## Tasks

| Status | Owner | Task | Notes |
|---|---|---|---|
| Complete | Lead Staff Engineer | Add frontend Sentry and Supabase integration modules | Optional when env vars are unset. |
| Complete | Lead Staff Engineer | Add backend Sentry initialization | Optional when `SENTRY_DSN` is unset. |
| Complete | QA Debugger | Add Playwright config and scoreboard smoke tests | Desktop and mobile projects. |
| Complete | Security Release Engineer | Add env examples without secrets | Service role key documented as backend-only. |
| Complete | Technical Writer | Add operations docs | `docs/operations/cloud_integrations.md`. |

## Test Plan

- Frontend: `npm run test`, `npm run lint`, `npm run build`, `npm run e2e`.
- Backend: Docker Python 3.11 `pytest` and `ruff check .`.
- Repository: `git diff --check`.
