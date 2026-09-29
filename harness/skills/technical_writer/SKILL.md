---
id: technical_writer_skill
title: Technical Writer Skill
type: skill
category: harness
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - documentation
  - handoff
  - compound
  - knowledge_management
related_files:
  - harness/agents/technical_writer.md
---

# Technical Writer Skill

Use this skill when creating or updating run records, handoffs, status summaries,
compound records, manuals, release notes, test-case indexes, or decision logs.

## Required Posture

- Preserve source-of-truth requirements and link to them instead of rewriting
  product scope casually.
- Keep records short, searchable, and actionable.
- Record uncertainty as uncertainty; do not convert unknowns into facts.
- Prefer exact file paths and test evidence over broad summaries.

## Inputs

- Active run files
- Agent reports from all operating roles
- `harness/metadata_schema.md`
- `harness/compound/index.md`
- `summary/status.md`
- Relevant test cases, issue logs, debug logs, and decisions

## Workflow

1. Ensure new harness records include YAML frontmatter when appropriate.
2. Keep `00_context.md` through `08_final_summary.md` readable and current.
3. Promote durable lessons into `harness/compound/` with reuse, avoid, and next
   action sections.
4. Update `summary/status.md` only with direction-changing context, latest run,
   active roles, and open items.
5. Link test cases and issue records so future agents can reuse them.

## Communication Rules

- Ask each role for missing evidence instead of filling gaps with assumptions.
- Report record gaps to Engineering Manager.
- Ask Founder Product Lead to approve product-facing wording when scope changes.
- Ask Security Release Engineer before documenting secrets, private data, or
  sensitive operational details.

## Completion Check

- Changed files, tests, limitations, and next step are recorded.
- Compound and status records point future agents to reusable context.
- No unresolved question is hidden as if it were decided.
