---
id: 2026_05_13_agent_role_operating_model_context
title: Agent Role Operating Model Context
type: run
category: harness
status: complete
created: 2026-05-13
updated: 2026-05-13
phase: phase1_mvp
owner: engineering_manager
tags:
  - run
  - context
  - agent_roles
  - operating_model
related_runs:
  - harness/runs/2026-05-13_agent_role_operating_model/
related_files:
  - AGENTS.md
  - harness/agents/README.md
  - harness/skills/README.md
---

# 00 Context

## Request

- User request: Add CEO/Founder, Senior Designer, Staff Engineer, Debugger, QA
  Lead, Engineering Manager, Product Manager/Project Manager, Beta Tester/User,
  CI/CD Engineer, Technical Writer, Security Engineer, and Lead Engineer agents;
  consolidate overlapping roles; define hierarchy, reporting, records,
  communication, regression capture, and role skills.
- Date: 2026-05-13
- Owner/coordinator: Engineering Manager with Technical Writer records.

## Requirement Trace

- Requirement source: `AGENTS.md` section 21, `README.md` harness engineering
  records, and `requirements_en.md` section 0.1 AI development principles.
- Requirement section or domain: Harness engineering records and AI agent
  operating process.
- Phase: Phase 1 / MVP.
- Out of scope: Runtime product features, Phase 2 payments/credits/ads, app
  authentication changes, production CI configuration changes.

## Applicable Skills

- Technical Writer: Yes.
- Engineering Manager: Yes.
- Founder Product Lead: Yes.
- Lead Staff Engineer: Yes.
- Senior Designer: Yes.
- QA Debugger: Yes.
- Security Release Engineer: Yes.
- Python coding: No.

## Reuse And Compound Check

- Relevant compound records:
  - `harness/compound/patterns/2026-05-12_plan_work_review_compound_pattern.md`
  - `harness/compound/state/2026-05-12_project_context_compound.md`
- Existing services/docs/templates to reuse:
  - `harness/agents/README.md`
  - Existing Planner/Generator/Evaluator/Coordinator workflow role files
  - `harness/runs/_template/`
- Known mistakes to avoid:
  - Duplicating roles with unclear ownership.
  - Letting confirmed defects remain only in conversation.
  - Guessing when a requirement or decision owner is unclear.
- Sandbox needed: No.

## Affected Layers

- Frontend: No runtime change.
- Backend: No runtime change.
- Database: No change.
- Document processing: No change.
- Integration: No runtime change.
- Tests: Documentation verification only.
- Docs: `AGENTS.md`, `README.md`, `harness/agents`, `harness/skills`,
  `harness/workflows`, `harness/compound`, `summary/status.md`.

## Permission And Privacy

- Roles involved: Engineering process roles only.
- Ownership rules: Product scope questions route to Founder Product Lead;
  technical decisions to Lead Staff Engineer; release/security to Security
  Release Engineer; records to Technical Writer.
- Sensitive fields: Not touched.
- API-level enforcement needed: Not applicable.

## Logging And Error Handling

- Runtime logs required: Not applicable.
- Error states to handle: Ambiguous role ownership and unresolved questions must
  be recorded and escalated.
- Values that must never be logged: Secrets, private data, tokens, payment
  credentials.
