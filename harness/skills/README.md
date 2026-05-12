# Project Skills

Project skills are reusable agent instructions that refine how work should be
done in this repository. They do not replace `AGENTS.md`, `requirements_en.md`,
`requirements_ko.md`, or `README.md`.

## Available Skills

| Skill | Path | When To Use |
|---|---|---|
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

