# Agent Roles

Use these role files to keep planner, generator, evaluator, and coordinator work
separate. One person or model can play multiple roles, but each role must leave
its own record in the run folder.

| Role | Primary Output | Must Not Own Alone |
|---|---|---|
| Coordinator | Run setup, handoff alignment, final summary | Product scope changes |
| Planner | Requirement trace, plan, acceptance criteria | Unreviewed implementation |
| Generator | Code/docs changes, work log, debug notes | Final acceptance decision |
| Evaluator | Test report, review findings, verification result | Hidden scope reduction |

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
