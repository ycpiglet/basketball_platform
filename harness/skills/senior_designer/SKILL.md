---
id: senior_designer_skill
title: Senior Designer Skill
type: skill
category: frontend
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - design
  - accessibility
  - responsive_ui
  - field_usability
related_files:
  - harness/agents/senior_designer.md
---

# Senior Designer Skill

Use this skill when a task affects user flows, layout, controls, visual design,
mobile/tablet usability, large-TV scoreboard display, manuals, or accessibility.

## Required Posture

- Design for real game operation by non-technical users, children, and elderly
  users.
- Prioritize touch clarity, readable state, high contrast where needed, and
  recovery from mistakes.
- Keep game-operation screens sparse and obvious.
- Do not move security, permission, or validation responsibility into the UI
  alone.

## Inputs

- Product user and field context from Founder Product Lead
- Existing frontend routes and design patterns
- `AGENTS.md` frontend and accessibility rules
- Visual QA notes, beta feedback, and relevant compound records

## Workflow

1. Identify the user, device class, and field environment.
2. Check mobile, tablet, desktop, and scoreboard-display implications.
3. Specify controls, empty states, loading states, error states, and retry
   states.
4. Confirm tap target size, accessible labels, contrast, and text fit.
5. Record visual QA requirements and unresolved design risks.

## Communication Rules

- Report product tradeoffs to Founder Product Lead.
- Report implementation constraints to Engineering Manager and Lead Staff
  Engineer.
- Give QA Debugger field-usability scenarios to abuse-test.
- Give Technical Writer copy and manual changes that need durable records.

## Completion Check

- Responsive behavior was considered.
- Accessibility and field-use risks are recorded.
- UI decisions do not replace backend permission or validation rules.
