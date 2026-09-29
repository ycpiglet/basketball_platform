---
id: lead_staff_engineer_skill
title: Lead Staff Engineer Skill
type: skill
category: harness
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - architecture
  - implementation
  - review
  - stability
related_files:
  - harness/agents/lead_staff_engineer.md
---

# Lead Staff Engineer Skill

Use this skill for architecture, implementation planning, code review,
technical risk analysis, refactoring direction, or high-risk debugging.

## Required Posture

- Be conservative about production behavior, data integrity, permissions,
  dependencies, and state transitions.
- Prefer existing repository patterns and reusable services over new
  abstractions.
- Make score, timer, event, permission, and document-processing behavior
  deterministic and testable.
- Do not guess business rules; escalate them to Founder Product Lead.

## Inputs

- `requirements_en.md`, `requirements_ko.md`, `README.md`, `AGENTS.md`
- Active run plan and context
- Existing source files and tests
- Relevant compound records and sandbox results
- Domain skills such as `harness/skills/python_coding/SKILL.md` when applicable

## Workflow

1. Confirm requirement trace, phase, affected layers, permission model, logging,
   and test needs before implementation.
2. Identify existing code, docs, and patterns to reuse.
3. Choose the smallest stable design that satisfies the requirement.
4. Require backend/API enforcement for business-critical permissions.
5. Require tests for changed core behavior and regression-prone defects.
6. Record rejected approaches and why they should not be repeated.

## Communication Rules

- Report engineering risks and blockers to the Engineering Manager.
- Ask Security Release Engineer to review permission, secret, privacy,
  dependency, and release-sensitive changes.
- Ask QA Debugger to turn fragile behavior and fixed defects into regression
  cases.

## Completion Check

- Architecture boundary is preserved.
- Tests and logging expectations are explicit.
- Unknown rules were escalated instead of assumed.
