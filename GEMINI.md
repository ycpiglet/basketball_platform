# GEMINI.md - Basketball Platform Project Guidelines

This document serves as the single source of truth for project-wide architecture, conventions, and workflows. Adhere to these standards to ensure consistency and quality across the codebase.

## 1. Project Overview
A web-based O2O platform for amateur basketball operations, including real-time scoreboard control, digital scorekeeping, and team/player management.

- **Phase 1 (MVP):** Scoreboard, Digital Score Sheet, Team/Player CRUD, Basic Community, PDF Export.
- **Phase 2 (Commercial):** Gym Reservations, Payments, Credits, Advanced AI PDF Parsing, Hardware Integration.

## 2. Core Architecture
- **Frontend:** Vue.js (TypeScript) + Vite. Hosted on Vercel.
- **Backend:** Python (FastAPI) + Pydantic. Dockerized.
- **Primary Database:** PostgreSQL (SQLAlchemy) for relational core data (Users, Teams, Players).
- **Event/Log Store:** MongoDB for game events, play-by-play, and high-volume snapshots.
- **Security:** Role-Based Access Control (RBAC) enforced at both Frontend (router) and Backend (API) levels.

## 3. Directory Structure
```text
.
├── frontend/                  # Vue + TypeScript
│   ├── src/app/               # Bootstrap and top-level views
│   ├── src/features/          # Feature slices (scoreboard, records, etc.)
│   ├── src/shared/            # Auth, types, styles, utilities
│   └── src/tests/             # Vitest unit/integration tests
├── backend/                   # FastAPI
│   ├── app/api/               # Routers and endpoints
│   ├── app/core/              # Config, logging, RBAC, security
│   ├── app/models/            # SQLAlchemy models
│   ├── app/schemas/           # Pydantic request/response models
│   ├── app/services/          # Business logic and deterministic game state
│   └── tests/                 # Pytest suite
└── docs/                      # Architecture and operational documentation
```

## 4. Engineering Conventions

### 4.1 General
- **Contextual Precedence:** Instructions in this file and sub-directory `GEMINI.md` files take absolute precedence.
- **Language:** English for code (naming, comments, commits), but support for Korean/English in UI.
- **Mobile-First:** All UI must be touch-friendly and responsive.

### 4.2 Backend (Python/FastAPI)
- **Validation:** Use Pydantic for all request/response schemas.
- **RBAC:** Always check permissions in the service or dependency layer, not just the endpoint.
- **Logging:** Use structured logging for all state-changing operations (requester, time, before/after states).
- **Error Handling:** Return standardized JSON error responses.

### 4.3 Frontend (Vue/TS)
- **Composition API:** Always prefer the Script Setup `<script setup>` syntax.
- **State Management:** Use Pinia for global state; keep local state within components.
- **Type Safety:** Use TypeScript strictly; avoid `any`. Define shared types in `src/shared/types`.
- **Styling:** Vanilla CSS is preferred. Ensure high contrast for scoreboard views (e.g., black background, bright text).

### 4.4 Data & Logic
- **Deterministic Events:** Game scores and statistics must be derived from an immutable stream of events.
- **PDF Processing:** Results from AI parsing must be marked as `N/A` if uncertain and require manual review before persistence.

## 5. Development Workflow
1. **Research:** Map codebase using `grep_search` and `glob`.
2. **Strategy:** Propose a plan before implementation.
3. **Execution:**
   - **Plan:** Define approach and testing strategy.
   - **Act:** Surgical changes. Add/update tests.
   - **Validate:** Run `pytest` or `npm run test` and linters (`ruff`, `eslint`).

## 6. Testing Standards
- **Bug Fixes:** Empirically reproduce the failure with a test case before applying the fix.
- **New Features:** Mandatory unit/integration tests for core logic (e.g., score calculation, RBAC).
- **Validation:** Changes are only "Done" when behavioral correctness is verified through tests.
