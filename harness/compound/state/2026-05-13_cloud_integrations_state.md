---
id: 2026_05_13_cloud_integrations_state
title: Cloud Integrations State
type: compound
category: deployment
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - vercel
  - supabase
  - sentry
  - playwright
  - deployment
related_runs:
  - harness/runs/2026-05-13_cloud_observability_e2e_integrations/
related_files:
  - docs/operations/cloud_integrations.md
  - frontend/playwright.config.ts
  - frontend/src/shared/integrations/sentry.ts
  - backend/app/core/sentry.py
---

# Cloud Integrations State

## Synthesis

The repository now has Phase 1 scaffolding for Vercel deployment, optional
Supabase browser/client environment, optional Sentry frontend/backend
observability, and Playwright E2E smoke tests.

## Reuse

- Use `docs/operations/cloud_integrations.md` before configuring cloud project
  environment variables.
- Use `npm run e2e` for Playwright smoke tests.
- Use Sentry only when DSNs are configured.

## Avoid

- Do not commit Sentry auth tokens, DSNs, Supabase service role keys, or Vercel
  tokens.
- Do not expose `SUPABASE_SERVICE_ROLE_KEY` to frontend/Vercel public env.
- Do not assume Supabase persistence exists for scoreboard until the store is
  replaced.

## Next Actions

- Fill cloud environment variables in Vercel and backend hosting.
- Decide backend hosting target for FastAPI.
- Replace in-memory scoreboard store with persistent storage when ready.
