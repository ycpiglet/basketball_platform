---
id: 2026_05_13_cloud_observability_e2e_integrations_test_report
title: Cloud Observability E2E Integrations Test Report
type: run
category: deployment
status: complete
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: qa_debugger
tags:
  - test_report
  - playwright
related_runs:
  - harness/runs/2026-05-13_cloud_observability_e2e_integrations/
---

# 05 Test Report

## Automated

- Frontend `npm run test`: 3 files, 10 tests passed.
- Frontend `npm run lint`: passed.
- Frontend `npm run build`: passed.
- Frontend Playwright E2E: 4 passed.
- Backend Docker Python 3.11 `pytest`: 28 passed.
- Backend Docker Python 3.11 `ruff check .`: passed.
- `git diff --check`: passed.

## Notes

- Playwright needed an escalated run in this environment because Chromium could
  not launch inside the sandbox.
