---
id: 2026_05_13_agent_operating_model
title: Agent Operating Model
type: compound
category: harness
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - agent_roles
  - operating_model
  - hierarchy
  - plan_work_review
  - regression
related_runs:
  - harness/runs/2026-05-13_agent_role_operating_model/
related_files:
  - harness/agents/README.md
  - harness/skills/README.md
search_terms:
  - agent operating model
  - minimized role set
  - qa debugger regression
  - security release gate
---

# Agent Operating Model

## Synthesis

The requested CEO, design, engineering, debugging, QA, management, product,
beta, CI/CD, writing, security, and lead roles are consolidated into seven
operating agents:

1. Founder Product Lead
2. Engineering Manager
3. Lead Staff Engineer
4. Senior Designer
5. QA Debugger
6. Security Release Engineer
7. Technical Writer

Planner, Generator, Evaluator, and Coordinator remain workflow lanes inside the
plan-work-review-compound loop.

## Reuse

- Use `harness/agents/README.md` for hierarchy and role routing.
- Use each role's matching `harness/skills/*/SKILL.md` before that role makes a
  decision, review, report, or handoff.
- Route product scope questions to Founder Product Lead.
- Route delivery and owner conflicts to Engineering Manager.
- Route architecture questions to Lead Staff Engineer.
- Route usability and accessibility questions to Senior Designer.
- Route defects, unusual beta behavior, and regression capture to QA Debugger.
- Route permission, privacy, CI/CD, and release risk to Security Release
  Engineer.
- Route durable records, handoffs, and compound synthesis to Technical Writer.

## Avoid

- Do not create separate agents for roles already consolidated here unless the
  product owner explicitly asks to split responsibility.
- Do not let product urgency bypass QA, security, privacy, or release gates.
- Do not leave confirmed bugs only in chat or run logs; convert them into
  regression cases.
- Do not guess when requirements, ownership, or behavior are unclear. Record the
  question and ask the decision owner.

## Next Actions

- Use this operating model in future substantial runs.
- Add concrete regression test cases whenever QA Debugger finds new failure
  modes.
- Keep `summary/status.md` aligned when the active role model changes.
