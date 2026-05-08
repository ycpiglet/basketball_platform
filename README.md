# Amateur Basketball Integrated Platform and Smart Scoreboard

A web-based O2O platform for amateur basketball operations. The product combines scoreboard control, digital scorekeeping, team and player databases, league and tournament management, community features, pickup game and guest matching, scorekeeper/referee recruiting, gym reservation, PDF document automation, and a future payment/credit economy.

This repository is intended to be developed with AI coding agents such as Codex. The product requirements are already defined in the two source documents below. Treat them as the project source of truth.

## Source of Truth

- `requirements_en.md` - Primary implementation reference for AI coding agents.
- `requirements_ko.md` - Original Korean requirements and intent reference.
- `AGENTS.md` - Operational instructions for Codex and other coding agents.

If the English and Korean requirements differ, preserve the more specific requirement and ask the product owner before deleting or narrowing scope.

## Product Goal

Build a reliable field tool that amateur basketball scorekeepers, team managers, tournament organizers, players, and community users can actually use during real games.

The first priority is not visual decoration. The first priority is reliable game operation, clean data management, safe permissions, clear logging, and simple touch-friendly UI.

## Development Phases

### Phase 1: Open Beta / MVP

Phase 1 is a free MVP focused on immediate field usability.

Required MVP scope:

- Scoreboard control panel
- Digital score sheet
- Game status display route for a TV or external monitor
- Game result and box score views
- Team, player, league, tournament, and game result CRUD
- Notices, FAQ, Q&A, manual, discussion board, comments
- Team roster, attendance check, practice participation votes, uniform/equipment surveys
- PDF template download, PDF export, and basic PDF parsing
- Role-based access control for guest, user, team manager, and system administrator
- Mobile-first responsive design with large touch targets
- Strong logging, validation, error handling, and tests

### Phase 2: Commercial Expansion

Phase 2 must not block the MVP. Implement only when explicitly requested.

Planned Phase 2 scope:

- Gym reservation, reservation calendar, electronic agreement, payment, and refund policy
- Payment gateway integration for participation fees, gym fees, and credit recharge
- Wallet UI, points, credits, settlement flow
- Advertising banners on high-traffic pages
- Mobile phone, email, bank account, and card verification
- Kakao AlimTalk, SMS, and email notifications
- Gym reviews, participant manner evaluation, and manner score
- Escrow-like protection, no-show prevention, and refund rules

## Target Architecture

```text
[User Device]
  |- Mobile Browser
  |- Tablet Browser
  |- PC Browser
  |- Display Browser / HDMI TV

        HTTPS

[Frontend: Vue.js + TypeScript]
  |- Vercel Hosting
  |- Responsive UI
  |- Scoreboard Control Panel
  |- Dedicated Display Route
  |- Community / Dashboard / Admin UI

        REST / WebSocket

[Backend: FastAPI]
  |- Auth / RBAC
  |- Game State API
  |- Score Event API
  |- Team / Player / League API
  |- PDF Parsing / Export API
  |- Payment / Credit API
  |- Notification API
  |- Hardware Packet API

[Database Layer]
  |- PostgreSQL + SQLAlchemy
  |- MongoDB
```

## Required Stack

### Frontend

- Vue.js
- TypeScript
- Vue Composition API preferred
- Mobile-first responsive UI
- Router-level permission guards
- Vercel deployment
- Dedicated scoreboard display route

### Backend

- Python
- FastAPI
- Pydantic validation
- SQLAlchemy for relational data
- Docker packaging
- Nginx reverse proxy for deployment
- REST APIs and WebSocket where real-time synchronization is required

### Data

- PostgreSQL for users, roles, teams, players, leagues, tournaments, games, applications, payments, credits, and relational core data
- MongoDB for game event logs, play-by-play data, box score snapshots, community activity, comments, chat-like records, and flexible document metadata

### Documents

- PDF parsing through Python libraries such as PyMuPDF or pdfplumber
- PDF export for game results, team rosters, player profiles, tournament data, and standard forms
- Missing parsed values must be marked as `N/A` and sent to a manual review screen before publishing

### Third-party Integrations

Phase 2 candidates:

- Payment gateway such as Toss Payments or PortOne
- Kakao AlimTalk / SMS / email notifications
- External advertising platform
- Authentication and verification providers

## Repository Structure

The repository now contains an initial Phase 1 skeleton. Phase 2 feature directories and provider implementations should be added only after explicit approval.

```text
.
|- README.md
|- AGENTS.md
|- requirements_en.md
|- requirements_ko.md
|- .env.example
|- docker-compose.yml
|- frontend/
|  |- package.json
|  |- vite.config.ts
|  |- vitest.config.ts
|  |- eslint.config.js
|  |- .env.example
|  |- src/
|  |  |- app/
|  |  |- routes/
|  |  |- features/
|  |  |  |- scoreboard/
|  |  |  |- records/
|  |  |  |- games/
|  |  |  |- teams/
|  |  |  |- players/
|  |  |  |- leagues/
|  |  |  |- tournaments/
|  |  |  |- community/
|  |  |  |- intranet/
|  |  |  |- documents/
|  |  |- shared/
|  |  |- tests/
|- backend/
|  |- pyproject.toml
|  |- .env.example
|  |- app/
|  |  |- main.py
|  |  |- api/
|  |  |- core/
|  |  |- models/
|  |  |- schemas/
|  |  |- services/
|  |  |- repositories/
|  |  |- integrations/
|  |- tests/
|- docs/
|  |- architecture/initial_project_plan.md
|  |- operations/local_development.md
|- scripts/
```

## Core Domain Modules

### Game Operation

- Create game
- Configure home and away teams
- Configure quarter, timer, fouls, timeout rules
- Control score, timer, fouls, timeout, period, and game status
- Sync control panel, digital record sheet, display route, and backend state

### Digital Scorekeeping

- Record player-level actions such as two-point score, three-point score, free throw, foul, assist, rebound, steal, block, turnover, substitution, timeout, and period change
- Automatically update team score, team fouls, player stats, and box score
- Store immutable event logs where possible
- Support correction workflows without silently deleting history

### Scoreboard Display

- Provide a dedicated route optimized for a 75-inch TV or external monitor
- Use high contrast and very large typography
- Hide admin controls from the public display route
- Keep the layout simple enough to read from a distance

### Data Management

- Manage teams, players, leagues, tournaments, game results, gym information, and applications through CRUD
- Provide filtering, sorting, searching, and admin workflows
- Blur or hide sensitive player and team member data unless the user has permission

### Community and Matching

- Discussion board, comments, replies, attachments, likes, reports, notices, FAQ, Q&A, and manuals
- Pickup game and guest application workflow
- Referee and scorekeeper recruiting workflow

### Team Intranet

- Team roster
- Attendance checks
- Practice participation votes
- Tournament participation surveys
- Uniform and equipment surveys
- Export to PDF or spreadsheet-like formats when needed

### Documents

- Provide standard PDF templates
- Parse uploaded PDFs
- Export platform data to PDF
- Require manual review for uncertain parsing results

### Hardware Integration

- MVP approach: browser display through HDMI on a TV or monitor
- Extension approach: backend interface for RS-485 or RF scoreboard control
- Hardware packet code must be modular and replaceable because the final protocol may be discovered by reverse engineering

Example packet concept:

```text
[START][HOME_SCORE][AWAY_SCORE][REMAINING_TIME][PERIOD][TEAM_FOULS][END]
```

## Permission Model

Minimum roles:

- Guest: can view public information only
- User: can join community, apply for games, manage own profile
- Team Manager: can manage own team, roster, guest approvals, team intranet data
- System Administrator: can manage all service data, user roles, tournaments, notices, and moderation

Rules:

- Enforce permissions at both frontend router level and backend API level
- Never rely only on frontend guards
- Sensitive data must be masked by default
- Every state-changing API must check role, ownership, and input validity

## Logging and Error Handling

Log important state changes before and after execution.

Required logging targets:

- Game score changes
- Game timer changes
- Player event records
- Game result finalization
- User role changes
- Team roster changes
- CRUD create/update/delete operations
- PDF upload, parse, export, and failure events
- Payment, credit, refund, and rollback events when Phase 2 is explicitly implemented
- File upload and security rejection events
- Hardware packet generation and transmission attempts only when future hardware integration is explicitly implemented

Errors must not crash the app. Use clear user-facing messages and structured server logs.

## Testing Requirements

Add or update tests whenever implementing public logic.

Minimum test areas:

- Score calculation
- Team foul and player foul updates
- Box score aggregation
- Game event creation and correction
- RBAC rules
- Sensitive data masking
- PDF parsing fallback to `N/A`
- Payment rollback logic only when Phase 2 payment work is explicitly implemented
- Credit balance consistency only when Phase 2 credit work is explicitly implemented
- API validation failures
- Frontend component behavior for critical UI flows

## Local Development

See `docs/operations/local_development.md` for the detailed workflow.

Frontend commands:

```bash
cd frontend
npm install
npm run dev
npm run lint
npm run test
npm run build
```

Backend commands:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
pytest
ruff check .
```

Local database command:

```bash
docker compose up -d postgres mongodb
```

## Environment Variables

Use `.env.example` files. Never commit real secrets.

Initial variables are documented in `.env.example`, `frontend/.env.example`, and `backend/.env.example`.

Current Phase 1 skeleton variables include:

```text
APP_NAME=
APP_ENV=
API_V1_PREFIX=
CORS_ORIGINS=
DATABASE_URL=
MONGODB_URI=
LOG_LEVEL=
VITE_API_BASE_URL=
VITE_APP_ENV=
```

Do not add Phase 2 payment, notification, verification, ad, or hardware secrets until those integrations are actually implemented.

## Definition of Done

A feature is not complete unless it includes:

1. A reference to the relevant requirements section
2. Implementation that matches the requested phase
3. Input validation
4. Permission checks
5. Logging
6. Error handling
7. Tests for core behavior
8. Responsive UI checks when UI is involved
9. Documentation updates when behavior changes
10. Notes about edge cases or follow-up work

## Current Repository Status

The repository now has a Phase 1-oriented development skeleton:

1. Vue + TypeScript frontend scaffold with Vite, Vue Router, Vitest, ESLint, MVP route placeholders, mobile-first styles, and development-only RBAC guard.
2. FastAPI backend scaffold with health route, settings, CORS setup, structured logging helper, RBAC helper, pytest, and Ruff configuration.
3. Docker Compose for local PostgreSQL and MongoDB only.
4. Architecture and local development docs.

Not yet implemented: production authentication, persistence models, migrations, game event APIs, CRUD APIs, PDF parsing/export, payment, credit, gym reservation payment, notification providers, ads, and production hardware control.
