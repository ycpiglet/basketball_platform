---
id: 2026_05_13_cloud_observability_e2e_integrations_issue_log
title: Cloud Observability E2E Integrations Issue Log
type: run
category: deployment
status: complete
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: engineering_manager
tags:
  - issue_log
  - integrations
related_runs:
  - harness/runs/2026-05-13_cloud_observability_e2e_integrations/
---

# 03 Issue Log

| Status | Severity | Owner | Issue | Resolution |
|---|---|---|---|---|
| Closed | Low | QA Debugger | Vitest collected Playwright E2E specs. | Excluded `e2e/**` in `vitest.config.ts`. |
| Closed | Low | Lead Staff Engineer | Supabase/Sentry library types blocked `vue-tsc`. | Added `skipLibCheck` and Rollup dev dependency. |
| Closed | Low | QA Debugger | Old Vite server returned `Outdated Optimize Dep`. | Started a fresh Vite server on port 5174 for E2E verification. |
| Closed | Low | QA Debugger | Playwright locator was strict because the clock appeared twice. | Scoped assertion with `.first()`. |
