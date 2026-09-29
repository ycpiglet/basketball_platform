# Project Skills

Project skills are reusable agent instructions that refine how work should be
done in this repository. They do not replace `AGENTS.md`, `requirements_en.md`,
`requirements_ko.md`, or `README.md`.

## Available Skills

| Skill | Path | When To Use |
|---|---|---|
| Founder Product Lead | `harness/skills/founder_product_lead/SKILL.md` | Product direction, prioritization, phase classification, requirement conflict resolution, or user-owner confirmation. |
| Engineering Manager | `harness/skills/engineering_manager/SKILL.md` | Multi-agent coordination, owner assignment, blocker escalation, handoffs, or plan-work-review-compound alignment. |
| Lead Staff Engineer | `harness/skills/lead_staff_engineer/SKILL.md` | Architecture, implementation planning, code review, technical risk analysis, or high-risk debugging. |
| Senior Designer | `harness/skills/senior_designer/SKILL.md` | User flows, layout, controls, responsive behavior, scoreboard display, manuals, or accessibility. |
| QA Debugger | `harness/skills/qa_debugger/SKILL.md` | Test design, bug reproduction, adversarial beta-user testing, debugging, or regression-case capture. |
| Security Release Engineer | `harness/skills/security_release_engineer/SKILL.md` | Authentication, authorization, sensitive data, secrets, dependencies, CI/CD, release readiness, or operational rollback. |
| Technical Writer | `harness/skills/technical_writer/SKILL.md` | Run records, handoffs, status summaries, compound records, manuals, release notes, test-case indexes, or decision logs. |
| Python coding | `harness/skills/python_coding/SKILL.md` | Any Python implementation, review, refactor, backend test, script, data processing, PDF parsing, or integration work. |

## Usage Rules

- Read the relevant skill before planning or editing files in that skill's
  domain.
- Record applicable skills in `harness/runs/<run>/00_context.md` and
  `01_plan.md`.
- If a skill conflicts with product requirements or `AGENTS.md`, follow the
  more specific product/project rule and note the conflict in the run issue log.
- Skills define engineering posture and code quality expectations; they do not
  authorize Phase 2 scope or product behavior by themselves.
