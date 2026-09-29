---
id: cloud_integrations
title: Cloud Integrations
type: run
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
---

# Cloud Integrations

This project is prepared for Vercel, Supabase, Sentry, and Playwright without
committing secrets.

## Vercel

The frontend Vercel config lives at `frontend/vercel.json` and rewrites SPA
routes to `index.html`.

Vercel project settings should use:

- Root directory: `frontend`
- Install command: `npm install`
- Build command: `npm run build`
- Output directory: `dist`

Required frontend environment variables:

- `VITE_API_BASE_URL`
- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`
- `VITE_SENTRY_DSN`
- `VITE_SENTRY_ENVIRONMENT`
- `VITE_SENTRY_RELEASE`
- `VITE_SENTRY_TRACES_SAMPLE_RATE`

Optional Sentry source map upload variables for Vercel builds:

- `SENTRY_AUTH_TOKEN`
- `SENTRY_ORG`
- `SENTRY_PROJECT`

Do not expose backend secrets in Vercel frontend variables.

## Supabase

Use Supabase Postgres as the deployed relational database by setting backend
`DATABASE_URL` to the Supabase pooled Postgres connection string.

Frontend Supabase browser access is optional and initialized only when both are
set:

- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`

Backend Supabase metadata placeholders:

- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_ROLE_KEY`

Never expose `SUPABASE_SERVICE_ROLE_KEY` to the frontend or Vercel public
variables.

## Sentry

Frontend Sentry initializes only when `VITE_SENTRY_DSN` is set.

Backend Sentry initializes only when `SENTRY_DSN` is set. Backend Sentry uses
FastAPI and logging integrations and disables default PII collection.

Keep sample rates conservative during the MVP:

- `VITE_SENTRY_TRACES_SAMPLE_RATE=0`
- `SENTRY_TRACES_SAMPLE_RATE=0`
- `SENTRY_PROFILES_SAMPLE_RATE=0`

Increase sampling only for short debugging windows.

## Playwright

Playwright config lives at `frontend/playwright.config.ts`.

Run E2E tests:

```bash
cd frontend
npm run e2e
```

If a dev server is already running:

```bash
PLAYWRIGHT_BASE_URL=http://127.0.0.1:5173 npm run e2e
```

The current smoke test mocks the scoreboard API so it can validate control and
display UI behavior without depending on a live backend.
