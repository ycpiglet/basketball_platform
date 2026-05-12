---
id: compound_readme
title: Compound Knowledge Layer
type: compound
category: harness
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - compound
  - synthesis
  - plan_work_review
  - reusable_knowledge
  - frontmatter
related_runs:
  - harness/runs/2026-05-12_sandbox_compound_framework/
---

# Compound Knowledge Layer

Compound records synthesize what the project has learned across runs, issues,
debugging notes, tests, decisions, and sandbox experiments.

The goal is to stop repeating the same mistakes, stop recreating deleted work,
reuse what already works, and give the next agent an accurate starting point.

## When To Create A Compound Record

Create or update a compound record when:

- A run closes with reusable lessons.
- A bug was debugged and the root cause should not be rediscovered.
- Several files describe the same issue and need one summary.
- An approach was tried and rejected.
- A pattern should be reused in future work.
- The current project state needs a concise handoff summary.

## Rules

- Every compound record must have YAML frontmatter.
- Link to source runs, issues, debug notes, tests, and docs.
- State `reuse`, `avoid`, and `next_actions` explicitly.
- Do not use compound records to override product requirements.
- If a compound record becomes obsolete, mark it `superseded`; do not delete it.

## Categories

| Folder | Purpose |
|---|---|
| `state/` | Current state summaries and project handoff context. |
| `patterns/` | Reusable ways of working or implementation patterns. |
| `lessons/` | Debugging lessons, known failure modes, and resolved mistakes. |
| `decisions/` | Synthesized decisions that summarize multiple sources. |

