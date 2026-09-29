# Agent Roles

Use these role files to keep product leadership, engineering execution, quality,
release, and records separate. One person or model can play multiple roles, but
each role must leave its own record in the run folder.

## Operating Role Set

The requested roles are consolidated into seven operating agents to reduce
handoff noise while preserving clear ownership.

| Operating Agent | Consolidates | Primary Output | Must Not Own Alone |
|---|---|---|---|
| Founder Product Lead | CEO/Founder, Product Manager, Project Manager | Product decisions, priority, phase boundaries | Security exceptions, release sign-off |
| Engineering Manager | Engineering Manager, delivery coordinator | Ownership, escalations, handoffs, delivery status | Product scope changes, technical acceptance |
| Lead Staff Engineer | Lead Engineer, Staff Engineer | Architecture, implementation direction, engineering review | Product tradeoffs, ignoring QA/security blockers |
| Senior Designer | Senior Designer, field usability reviewer | UX decisions, accessibility risks, responsive checks | Backend permission logic, security exceptions |
| QA Debugger | QA Lead, Debugger, Beta Tester/User | Test reports, bug records, regression cases | Product acceptance, production fixes alone |
| Security Release Engineer | Security Engineer, CI/CD Engineer | CI/release evidence, security/privacy review | Product approval, bypassing QA failures |
| Technical Writer | Technical Writer, knowledge manager | Handoffs, decisions, compound/status records | Requirement changes, QA/security sign-off |

## Workflow Lanes

Planner, Generator, Evaluator, and Coordinator remain workflow lanes. They are
not separate hierarchy owners; they describe which part of the plan-work-review
cycle is active.

| Workflow Lane | Primary Output | Must Not Own Alone |
|---|---|---|
| Coordinator | Run setup, handoff alignment, final summary | Product scope changes |
| Planner | Requirement trace, plan, acceptance criteria | Unreviewed implementation |
| Generator | Code/docs changes, work log, debug notes | Final acceptance decision |
| Evaluator | Test report, review findings, verification result | Hidden scope reduction |

## Reporting Line

```text
Product owner
  -> Founder Product Lead
      -> Engineering Manager
          -> Lead Staff Engineer
          -> Senior Designer
          -> QA Debugger
          -> Security Release Engineer
          -> Technical Writer
```

Blocking findings flow upward immediately. Product questions go to Founder
Product Lead. Technical questions go to Lead Staff Engineer. Security and release
questions go to Security Release Engineer. Record gaps go to Technical Writer.

## Shared Rules

- Start from `requirements_en.md`, then check Korean intent in
  `requirements_ko.md` when scope is ambiguous.
- Start continuation work from `summary/status.md`, then
  `harness/compound/index.md`.
- Check `harness/skills/` before planning or editing domain-specific work.
- Mark every task as Phase 1/MVP or Phase 2/commercial expansion.
- Capture affected layers, permission model, logging needs, and tests before
  implementation starts.
- Use `harness/sandbox/` for experiments and `harness/compound/` for durable
  lessons.
- Do not delete or narrow requirements silently.
- Prefer short summaries plus links to exact files and line numbers.
- If a role needs confirmation, it must record the question and ask the decision
  owner instead of guessing.
- Confirmed defects must become regression cases under `harness/test_cases/` or
  the repository's automated test folders.
- Repeated mistakes, rejected approaches, and reusable patterns must be promoted
  to `harness/compound/`.

## Role Skills

Each operating role has a matching skill:

- `harness/skills/founder_product_lead/SKILL.md`
- `harness/skills/engineering_manager/SKILL.md`
- `harness/skills/lead_staff_engineer/SKILL.md`
- `harness/skills/senior_designer/SKILL.md`
- `harness/skills/qa_debugger/SKILL.md`
- `harness/skills/security_release_engineer/SKILL.md`
- `harness/skills/technical_writer/SKILL.md`
