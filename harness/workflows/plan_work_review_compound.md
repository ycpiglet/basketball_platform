---
id: plan_work_review_compound_workflow
title: Plan Work Review Compound Workflow
type: compound
category: harness
status: active
created: 2026-05-12
updated: 2026-05-12
phase: phase1_mvp
tags:
  - workflow
  - plan_work_review
  - sandbox
  - compound
related_runs:
  - harness/runs/2026-05-12_sandbox_compound_framework/
---

# Plan Work Review Compound Workflow

Use this workflow for substantial tasks.

## 1. Plan

- Read `summary/status.md`.
- Read relevant compound records from `harness/compound/index.md`.
- Read applicable skills from `harness/skills/`.
- Create or update a run folder under `harness/runs/`.
- Record requirement trace, phase, permissions, logging, tests, and reuse
  targets.
- Engineering Manager assigns affected operating roles and records who owns
  product, architecture, design, QA/debug, security/release, and documentation
  decisions.
- Founder Product Lead confirms product scope when requirements conflict or
  behavior is ambiguous.

## 2. Sandbox When Uncertain

- If the approach is uncertain or risky, create a sandbox experiment.
- Record attempts and outcomes.
- Promote only after `03_promotion_review.md` is satisfied.

## 3. Work

- Implement narrowly against the plan.
- Reuse existing services, docs, templates, and patterns where possible.
- Record changed files and command summaries in the run.
- Lead Staff Engineer keeps implementation conservative and records technical
  decisions or rejected approaches.
- Senior Designer reviews field usability when UI behavior changes.

## 4. Review

- Run existing test commands.
- Record pass/fail results and residual risk.
- Identify repeated issues, failed assumptions, and reusable decisions.
- QA Debugger tries normal, boundary, negative, interrupted, repeated, and
  beta-user paths. Confirmed bugs must become regression cases.
- Security Release Engineer reviews permission, privacy, CI/CD, dependency, and
  release-gate risks when relevant.

## 5. Compound

- Create or update a compound record for durable lessons.
- Include YAML frontmatter.
- State `reuse`, `avoid`, and `next_actions`.
- Mark obsolete records as `superseded`; do not delete them.
- Technical Writer keeps compound records short, searchable, and linked to the
  run evidence.

## 6. Status

- Update `summary/status.md` only with the current direction, latest run,
  active derived requirements, important compound records, and open items.
