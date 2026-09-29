---
id: 2026_05_13_cloud_observability_e2e_integrations_deployment
title: Cloud Observability E2E Integrations Deployment
type: run
category: deployment
status: complete
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: security_release_engineer
tags:
  - deployment
  - vercel
  - sentry
  - supabase
related_runs:
  - harness/runs/2026-05-13_cloud_observability_e2e_integrations/
---

# 07 Deployment

Vercel appears scaffolded through `frontend/vercel.json`, but no local `.vercel`
project link is present in the repository. Configure the existing Vercel project
with `frontend` as the root directory and add the environment variables listed
in `docs/operations/cloud_integrations.md`.
