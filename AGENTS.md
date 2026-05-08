# AGENTS.md

This file gives Codex and other AI coding agents project-specific instructions. Read it before making changes.

## 1. Source of Truth

Use these files as the product requirements:

1. `requirements_en.md` - primary implementation reference.
2. `requirements_ko.md` - original Korean intent reference.
3. `README.md` - repository overview and operating guide.

If requirements conflict, do not silently choose the smaller scope. Preserve the more specific requirement and ask the product owner before removing, narrowing, or reclassifying any requirement.

## 2. Product Mental Model

This is not just a scoreboard UI. It is an amateur basketball operations ecosystem.

Core domains:

- Game operation
- Smart scoreboard
- Digital scorekeeping
- Team, player, league, tournament, and gym data management
- Community and matching
- Team intranet
- PDF document automation
- Hardware/display integration
- Future payment, credit, point, ad, and reservation system

The highest priority is reliable field operation for real amateur basketball games.

## 3. Phase Discipline

Default to Phase 1 / MVP unless the user explicitly asks for Phase 2.

### Phase 1 / MVP

Implement first:

- Scoreboard control panel
- Digital score sheet
- Dedicated scoreboard display route
- Game result and box score view
- Team, player, league, tournament, and game result CRUD
- Community basics: notices, discussion board, comments, Q&A, FAQ, manual
- Team intranet basics: roster, attendance, voting, surveys
- PDF template download, PDF export, basic PDF parsing
- Guest, user, team manager, system administrator roles
- Logging, validation, error handling, tests, and responsive UI

### Phase 2 / Commercial Expansion

Do not implement unless explicitly requested:

- Gym reservation payment
- Participation fee payment
- Credit recharge and wallet
- Points and settlement
- Ads
- Phone, email, bank account, and card verification
- Kakao AlimTalk, SMS, and email notifications
- Reviews, manner score, escrow-like policies, no-show policies

Design Phase 2 interfaces as replaceable stubs only when needed to avoid blocking MVP architecture.

## 4. Required Tech Stack

Frontend:

- Vue.js
- TypeScript
- Vue Composition API preferred
- Mobile-first responsive UI
- Vercel deployment target

Backend:

- Python
- FastAPI
- Pydantic validation
- SQLAlchemy for PostgreSQL models
- Docker packaging
- Nginx reverse proxy deployment target

Data:

- PostgreSQL for relational core data
- MongoDB for logs, play-by-play records, flexible event snapshots, comments, and document metadata

Document processing:

- Use Python PDF libraries such as PyMuPDF or pdfplumber when implementing parsing.
- Missing or uncertain parsed values must become `N/A` and must be routed to manual review before publishing.

Real-time behavior:

- Use WebSocket or an equivalent real-time mechanism for game state synchronization when appropriate.
- Keep scoreboard control, record sheet, display route, and backend game state consistent.

## 5. Work Planning Rule

Before changing code, identify:

1. The relevant requirement section or domain.
2. Whether the task belongs to Phase 1 or Phase 2.
3. The affected layer: frontend, backend, database, document processing, integration, test, or docs.
4. The permission model involved.
5. The logging and test requirements.

When reporting work, include:

- What changed
- Why it changed
- Files changed
- Tests run
- Known limitations
- Next safe step when useful

## 6. Architecture Rules

- Keep frontend and backend separated.
- Do not place business-critical permission logic only in the frontend.
- Put business rules in backend services, not directly inside route handlers.
- Use repositories or data-access layers for database operations when the backend is large enough.
- Keep score calculation and event aggregation deterministic and testable.
- Prefer immutable event logs for game actions. If correction is needed, add correction events or auditable updates instead of silently deleting history.
- Keep hardware packet generation modular and isolated from normal scoreboard UI logic.
- Keep payment, credit, notification, and ad integrations behind provider interfaces so providers can be replaced.

## 7. Frontend Rules

- Prioritize mobile and tablet touch use.
- Use large tap targets for game control and scorekeeping screens.
- Scoreboard display route must be readable from a distance on a large TV.
- Do not show admin controls on public display routes.
- Apply router-level role guards, but never treat them as the only security layer.
- Separate components by responsibility.
- For dense admin pages, provide search, filter, sort, pagination, and clear empty states.
- Provide clear loading, success, error, and retry states.
- Use accessible labels for controls and icons.

## 8. Backend Rules

- Validate every request with schemas.
- Check authentication, role, ownership, and state-transition validity for every state-changing endpoint.
- Return clear errors without leaking secrets or sensitive personal data.
- Use transactions for multi-step state changes.
- Use database locking or equivalent consistency controls for future payment, credit, and wallet flows.
- Add structured logs before and after important state changes.
- Do not store raw secrets, tokens, or payment credentials in application tables.

## 9. Database Rules

PostgreSQL should hold relational core data such as:

- Users
- Roles
- Teams
- Players
- Team memberships
- Leagues
- Tournaments
- Games
- Game participants
- Applications
- Gyms
- Reservations
- Payments and credits when Phase 2 is implemented

MongoDB should hold flexible or high-volume records such as:

- Game event logs
- Play-by-play records
- Box score snapshots
- Community comments or activity streams
- Uploaded document metadata
- Parse result snapshots

Do not duplicate authoritative state across databases unless a synchronization rule is documented.

## 10. Permission and Privacy Rules

Minimum roles:

- Guest
- User
- Team Manager
- System Administrator

Rules:

- Guests can view only public information.
- Users can manage their own profile, community activity, and applications.
- Team Managers can manage only their own team, roster, guests, and intranet data.
- System Administrators can manage global service data and moderation.
- Sensitive information must be masked by default unless permission allows access.
- Sensitive fields include phone number, address, private account data, payment state details, and private team member records.
- Enforce privacy at API response level, not only in the UI.

## 11. Logging Rules

Add structured logging for:

- Score changes
- Timer changes
- Player event records
- Game finalization
- Role changes
- Team roster changes
- CRUD create/update/delete actions
- PDF upload, parse, export, and failure events
- File upload validation failures
- Payment, credit, refund, and rollback events when Phase 2 is implemented
- Hardware packet generation and transmission attempts

Logs should include, when safe:

- request id
- user id
- role
- action
- target entity type
- target entity id
- before state summary
- after state summary
- result
- error code
- timestamp

Never log raw passwords, tokens, private keys, full payment credentials, or unnecessary personal data.

## 12. Error Handling Rules

- Use defensive programming for all user input.
- Do not allow frontend crashes on normal API failures.
- Provide global frontend error handling where the framework supports it.
- Backend APIs should return structured error responses.
- File parsing failures must not crash the service; route uncertain values to manual review.
- Payment and credit failures must roll back partially completed changes when Phase 2 is implemented.

## 13. Testing Rules

Add or update tests for core behavior.

Required test targets:

- Score updates
- Timer state transitions
- Team foul and player foul updates
- Box score aggregation
- Game event creation and correction
- Permission checks
- Sensitive data masking
- PDF parse fallback to `N/A`
- File upload validation
- API validation failures
- Credit and payment rollback logic when Phase 2 is implemented
- Critical frontend flows for control panel, record sheet, and display route

Use the repository's existing test runner. Do not introduce a new test framework without a clear reason.

## 14. UI and Accessibility Rules

- Design for non-technical users, children, and elderly users.
- Prefer obvious icons with text labels for important actions.
- Use large buttons on scorekeeping and control screens.
- Avoid dense text on game operation screens.
- Use high contrast for scoreboard display.
- Support light and dark themes when the UI foundation is ready.
- Plan for Korean and English localization.

## 15. Hardware and Display Rules

MVP display strategy:

- Use a dedicated browser route displayed through HDMI on a TV or monitor.
- Optimize for a 75-inch TV plus protective panel setup.

Future hardware strategy:

- Prepare a backend hardware packet interface for RS-485 or RF scoreboard devices only when explicitly requested.
- Keep packet encoding isolated in a module such as `hardware_packet` or `scoreboard_adapter`.
- Do not hard-code final packet formats as permanent truth. Protocol details may change after reverse engineering.

Packet concept:

```text
[START][HOME_SCORE][AWAY_SCORE][REMAINING_TIME][PERIOD][TEAM_FOULS][END]
```

## 16. Document Automation Rules

- Provide standard templates before expecting users to upload arbitrary documents.
- Parse known templates first.
- Extract fields such as date, location, team names, player names, score, fouls, fees, benefits, and organizer details when applicable.
- Use `N/A` for missing fields.
- Always provide a manual review screen before publishing parsed data.
- Export important data to PDF for printing and sharing.

## 17. Payment and Credit Rules

These are Phase 2 rules. Do not implement production payment behavior during MVP unless explicitly requested.

When implemented:

- Use transactions.
- Use rollback on failure.
- Prevent negative balances.
- Make credit usage idempotent.
- Use rate limits and daily caps to prevent point abuse.
- Keep payment provider code behind an integration interface.
- Never store full card numbers or raw payment credentials.

## 18. Code Quality Rules

- Prefer clear, maintainable code over clever code.
- Add comments for non-obvious business rules.
- Use explicit types in TypeScript and Python where practical.
- Keep functions small and testable.
- Avoid global mutable state for game logic.
- Avoid mixing UI rendering, API calls, and business logic in the same function.
- Do not add dependencies unless they solve a real problem.
- If adding a dependency, explain why and use the existing package manager.

## 19. Repository Hygiene

- Do not commit secrets.
- Keep `.env.example` updated when adding environment variables.
- Update README when setup commands or architecture change.
- Update requirements documents only when the user asks to change product scope.
- Keep generated files, build outputs, caches, and local database files out of version control.

## 20. Completion Checklist

A task is complete only when the relevant items are satisfied:

- Requirement section identified
- Correct phase respected
- Implementation added
- Permission rules applied
- Input validation added
- Logging added
- Error handling added
- Tests added or updated
- Responsive behavior considered for UI
- Sensitive data masking considered
- Documentation updated when needed
- Edge cases or known limitations reported
