# 00 Context

## Request

- User request: Confirm the root `SKILL.md` Python coding rules, decide when and
  how they should be used, and move the file to a better location.
- Date: 2026-05-12
- Owner/coordinator: Codex

## Requirement Trace

- Requirement source: `AGENTS.md` sections 5, 18, 19, 20, and 21.
- Requirement section or domain: Agent workflow, code quality, repository
  hygiene, and harness engineering records.
- Phase: Phase 1 / MVP support.
- Out of scope: executable Python code changes, product permission changes,
  runtime logging changes, Phase 2 implementation.

## Applicable Skills

- Python coding: The root `SKILL.md` itself was reviewed and relocated to
  `harness/skills/python_coding/SKILL.md`. No Python code was edited.

## Affected Layers

- Frontend: Not affected.
- Backend: Not affected.
- Database: Not affected.
- Document processing: Not affected.
- Integration: Not affected.
- Tests: Documentation-only verification.
- Docs: Harness, README, AGENTS, and run templates.

## Permission And Privacy

- Roles involved: Engineering agents only.
- Ownership rules: Product permission behavior is unchanged.
- Sensitive fields: No sensitive user data added.
- API-level enforcement needed: N/A.

## Logging And Error Handling

- Runtime logs required: N/A.
- Error states to handle: N/A.
- Values that must never be logged: Passwords, tokens, private keys, full payment
  credentials, and unnecessary personal data.

