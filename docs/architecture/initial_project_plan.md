# Initial Project Assessment and Skeleton Plan

## Requirement alignment

- Relevant requirement domains: Phase 1 game operation, scoreboard display, digital scorekeeping, relational CRUD foundations, RBAC, logging, validation, error handling, and tests.
- Phase: Phase 1 / MVP only.
- Affected layers: frontend, backend, database configuration, docs, and test setup.
- Permission model: guest, user, team manager, and system administrator roles. This skeleton includes only role constants and development guards; production authentication is intentionally not implemented.
- Logging and testing: backend structured logging helper, backend RBAC tests, and frontend RBAC tests are included as initial infrastructure.

## Project goal

Build a web-based amateur basketball operations ecosystem that can be used during real games, beginning with reliable scoreboard control, digital scorekeeping, public display, and core data management. The product should later support broader community, intranet, document automation, O2O reservation, payments, credits, ads, notification, and hardware integrations without letting those later features block the MVP.

## MVP scope

Phase 1 prioritizes:

- Scoreboard control panel.
- Dedicated public scoreboard display route for HDMI/TV usage.
- Digital score sheet and deterministic event flow foundation.
- Game result and box score view foundation.
- Team, player, league, tournament, and game result CRUD foundation.
- Community basics, team intranet basics, and document automation foundations.
- RBAC for guest, user, team manager, and system administrator.
- Mobile-first, touch-friendly UI.
- Logging, validation, error handling, and tests.

## Phase 2 scope to defer

Phase 2 should be implemented only after explicit product approval and validation of real demand:

- Gym reservation payment, participation fee payment, credits, wallet, points, settlement, and refunds.
- Ads and monetization features.
- Phone, email, bank account, and card verification.
- Kakao AlimTalk, SMS, and email notifications.
- Reviews, manner score, escrow-like policies, and no-show policies.
- RS-485/RF production scoreboard hardware control.

## Major technical constraints

- Frontend must use Vue.js, TypeScript, Vue Composition API, and mobile-first responsive design.
- Backend must use Python, FastAPI, Pydantic validation, SQLAlchemy for PostgreSQL, Docker packaging, and a deployment path compatible with Nginx reverse proxy.
- PostgreSQL is the authoritative store for relational core data.
- MongoDB is intended for high-volume or flexible records such as game event logs, play-by-play, comments, document metadata, and snapshots.
- Business-critical permission logic must live in backend services, not only in frontend route guards.
- Score and event aggregation must be deterministic and testable, with auditable corrections instead of silent history deletion.
- PDF parsing must use `N/A` for missing or uncertain values and route parsed data through manual review before publishing.

## Inconsistencies, missing decisions, and risks

1. **Phase boundaries need sharper tagging.** Requirements list gyms, reservations, matching, payments, credits, ads, reviews, and notifications in broad product routes, but MVP instructions say not to implement commercial behavior yet. Each backlog item should be tagged Phase 1, Phase 1 stub, or Phase 2 before implementation.
2. **Authentication provider is undecided.** The docs require RBAC and production-grade backend authorization but do not choose session cookies, JWT, OAuth, social login, or a managed auth provider. This skeleton avoids production auth until that decision is made.
3. **Real-time synchronization protocol is undecided.** Requirements allow WebSocket or equivalent, but the message contract, conflict handling, reconnection behavior, and offline correction flow remain unspecified.
4. **PostgreSQL versus MongoDB authority needs event-state rules.** Requirements correctly split relational and event data, but the synchronization rule between game state, immutable events, snapshots, and box scores must be documented before game APIs are finalized.
5. **PDF template formats are undefined.** The docs require parsing known templates first, but the actual templates, field names, confidence thresholds, and review workflow need product samples.
6. **Hardware packet details are intentionally provisional.** The packet concept is useful for future design, but production RS-485/RF control must wait for actual protocol validation.
7. **Privacy policy details are incomplete.** Sensitive data masking is required, but field-level response rules and retention rules need a privacy matrix before user/profile APIs are implemented.
8. **Deployment topology is broad.** Vercel, Docker, Nginx, PostgreSQL, and MongoDB are named, but the exact environments, secrets management, migrations, backups, and observability stack are not yet decided.

## Practical repository structure

```text
.
├── frontend/                  # Vue + TypeScript app for Vercel
│   ├── src/app/               # app bootstrap and top-level views
│   ├── src/routes/            # Vue Router and route metadata guards
│   ├── src/features/          # MVP feature slices: scoreboard, records, teams, etc.
│   ├── src/shared/            # shared auth helpers, types, styles, API utilities
│   └── src/tests/             # frontend unit tests
├── backend/                   # FastAPI app
│   ├── app/api/               # API routers only
│   ├── app/core/              # settings, logging, RBAC, security foundation
│   ├── app/schemas/           # Pydantic request/response schemas
│   ├── app/services/          # business rules and deterministic game logic
│   ├── app/repositories/      # SQLAlchemy/MongoDB data access
│   ├── app/models/            # SQLAlchemy models
│   ├── app/integrations/      # replaceable external provider boundaries
│   └── tests/                 # backend tests
├── docs/                      # architecture and operations notes
├── scripts/                   # future local automation scripts
└── docker-compose.yml         # local PostgreSQL and MongoDB only
```

## Next recommended task

Define the Phase 1 game event model and state-transition rules before building CRUD endpoints. The next safe implementation step is a backend service that accepts validated score/timer/foul events, produces deterministic game state, logs state changes, and has unit tests for corrections and box score aggregation.
