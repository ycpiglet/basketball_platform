# 00 Context

## Request

- User request: Create a specification for applying the project to a real
  amateur basketball club, document required work and procedures, and reorganize
  the current project history, issues, debugging, testing, validation, and next
  planning into the harness structure.
- Date: 2026-05-12
- Owner/coordinator: Codex

## Requirement Trace

- Requirement source:
  - `requirements_en.md`
  - `requirements_ko.md`
  - `README.md`
  - `AGENTS.md`
- Requirement section or domain:
  - Phase 1 / MVP field operation
  - Scoreboard control
  - Digital scorekeeping
  - Scoreboard display route
  - Result and box score
  - Logging, validation, error handling, testing, and responsive UI
- Phase: Phase 1 / MVP
- Out of scope:
  - Phase 2 payment, credit, wallet, ads, notification, and reservation payment
  - Production hardware control
  - Production authentication beyond controlled pilot guardrails

## Applicable Skills

- Python coding: No Python code was changed. The skill will apply to the next
  backend implementation task.

## Affected Layers

- Frontend: Planning only.
- Backend: Planning only.
- Database: Planning only.
- Document processing: Planning only.
- Integration: Planning only.
- Tests: Acceptance test documentation added.
- Docs: New field pilot requirements and archive summary added.

## Permission And Privacy

- Roles involved:
  - Guest
  - User
  - Team Manager
  - System Administrator
- Ownership rules:
  - Score-changing pilot actions should require an operator/team-manager/admin
    role.
  - Display/result viewing may be public or guest-visible.
- Sensitive fields:
  - Phone number, address, account/payment data, and private team member data
    should not be collected for the first pilot.
- API-level enforcement needed:
  - Required when FP-001 and FP-007 are implemented.

## Logging And Error Handling

- Runtime logs required later:
  - Score changes
  - Timer changes
  - Team/player fouls
  - Timeouts
  - Quarter/period changes
  - Score corrections
  - Game finalization
- Error states to handle later:
  - Invalid score value
  - Negative clock/score values
  - Finalized game mutation
  - Unauthorized state change
  - Display sync failure
  - Normal API failure in frontend
- Values that must never be logged:
  - Passwords, tokens, private keys, full payment credentials, and unnecessary
    personal data.

