---
id: engineering_manager_skill
title: Engineering Manager Skill
type: skill
category: harness
status: active
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
tags:
  - coordination
  - delivery
  - escalation
  - handoff
related_files:
  - harness/agents/engineering_manager.md
---

# Engineering Manager Skill

Use this skill when coordinating multi-agent work, assigning owners, managing
handoffs, escalating blockers, or keeping plan-work-review-compound aligned.

## Required Posture

- Maintain clear hierarchy without hiding dissenting technical, QA, or security
  findings.
- Keep work moving, but do not let speed bypass plan, review, test, or compound
  records.
- Convert ambiguity into explicit questions and owners.

## Inputs

- User request and latest user correction
- `summary/status.md`
- Active run folder
- Agent role files under `harness/agents/`
- Relevant skills under `harness/skills/`

## Workflow

1. Open or confirm the active run folder.
2. Assign an owner for planning, implementation, QA, security/release, design,
   and documentation when those areas are affected.
3. Keep `01_plan.md` task ownership current.
4. Route blockers to the correct decision owner:
   - Product scope: Founder Product Lead.
   - Architecture: Lead Staff Engineer.
   - UX/accessibility: Senior Designer.
   - Defects/regression: QA Debugger.
   - Security/release: Security Release Engineer.
   - Records/handoff: Technical Writer.
5. Ensure every owner records findings in the correct run file.

## Communication Rules

- Require concise status reports with file paths, test evidence, and blockers.
- Do not accept "probably" as a decision. Ask for confirmation or record the
  assumption as unresolved.
- Escalate repeated issues to compound records.

## Completion Check

- Owners and handoffs are visible.
- Blockers have decision owners.
- Run records are sufficient for another agent to resume.
