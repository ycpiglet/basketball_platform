# 08 Final Summary

## Outcome

- Root `SKILL.md` was confirmed and moved to
  `harness/skills/python_coding/SKILL.md`.
- Documentation now says to apply the Python coding skill before writing,
  reviewing, or refactoring Python code.

## Files Changed

- `AGENTS.md`
- `README.md`
- `harness/README.md`
- `harness/agents/**`
- `harness/runs/_template/**`
- `harness/skills/**`
- `harness/runs/2026-05-12_python_coding_skill_location/**`

## Tests Run

- `git diff --check`
- `test ! -e SKILL.md && test -f harness/skills/python_coding/SKILL.md`
- `rg --files -g 'SKILL.md'`

## Known Limitations

- The skill is repository-local and documented for agents, not installed into
  global Codex skill discovery.

## Open Issues

- PCS-001: Decide later whether the Python coding skill should also be installed
  as a global/local Codex skill outside this repository.

## Next Safe Step

- For the next Python backend task, start the run by recording
  `harness/skills/python_coding/SKILL.md` in `00_context.md` and `01_plan.md`.
