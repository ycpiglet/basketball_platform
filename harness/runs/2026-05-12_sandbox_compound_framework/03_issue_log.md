---
id: 2026_05_12_sandbox_compound_framework_issue_log
title: Sandbox Compound Framework Issue Log
type: run
category: harness
status: complete
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - run
  - issue_log
  - sandbox
  - compound
related_runs:
  - harness/runs/2026-05-12_sandbox_compound_framework/
---

# 03 Issue Log

| ID | Severity | Status | Area | Summary | Owner | Next Step |
|---|---|---|---|---|---|---|
| SC-001 | Medium | Open | Metadata | Older harness files do not all have YAML frontmatter. | Coordinator | Backfill only when those files are edited or become active context. |
| SC-002 | Low | Open | Process | Compound records can become stale if not updated after substantial runs. | Coordinator | Update compound before `summary/status.md` in closeout. |

## Scope Questions

- Should repo-local compound records later be exported into external agent
  memory? Deferred.

## Blockers

- None for docs-only framework implementation.

