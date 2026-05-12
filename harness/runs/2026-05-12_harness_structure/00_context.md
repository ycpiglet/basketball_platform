# 00 Context

## Request

- User request: Improve the harness engineering directory structure and file
  names so planner, generator, evaluator, and related roles can keep shared
  context through planning, work logs, issues, debugging, testing, validation,
  and deployment notes.
- Date: 2026-05-12
- Owner/coordinator: Codex

## Requirement Trace

- Requirement source: `AGENTS.md` section 5, 11, 13, 19, and 20.
- Requirement section or domain: Phase 1 engineering workflow, documentation,
  logging discipline, testing discipline, and repository hygiene.
- Phase: Phase 1 / MVP support.
- Out of scope: product authentication, payment, credit, ad, notification,
  reservation payment, and hardware control implementation.

## Affected Layers

- Frontend: Not affected.
- Backend: Not affected.
- Database: Not affected.
- Document processing: Not affected.
- Integration: Not affected.
- Tests: Test case documentation structure added.
- Docs: Harness, README, AGENTS, and project status documentation updated.

## Permission And Privacy

- Roles involved: Engineering agents only. Product roles are not changed.
- Ownership rules: Product permission behavior remains enforced in application
  code, not harness notes.
- Sensitive fields: No sensitive user data added.
- API-level enforcement needed: N/A.

## Logging And Error Handling

- Runtime logs required: N/A for docs-only structure work.
- Error states to handle: N/A.
- Values that must never be logged: Passwords, tokens, private keys, full payment
  credentials, and unnecessary personal data.

