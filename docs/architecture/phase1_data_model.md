# Phase 1 MVP Data Model

This document explains the initial PostgreSQL/SQLAlchemy data model for the Phase 1 MVP. It is intentionally limited to operational basketball data and basic RBAC hooks. It does **not** add payment, credit, wallet, gym rental payment, advertising, notification, review, or production authentication models.

## Tables

| Table | Purpose |
|---|---|
| `users` | Account shell with `email`, `display_name`, `role`, and `is_active`. This is only an RBAC-ready profile model; production authentication is not implemented yet. |
| `teams` | Team profile with optional `owner_user_id` for future team-manager ownership checks. |
| `players` | Basketball participant profile. A player can optionally link to a user account but can exist before signup. |
| `team_memberships` | Roster relationship between teams and players, including role, status, approval hook, `joined_at`, and `ended_at`. |
| `leagues` | League/season container for schedules, tournaments, games, standings, and public results. |
| `tournaments` | Tournament container, optionally linked to a league. |
| `games` | Scheduled/live/final game row with team links, optional league/tournament links, status, period, score, and team foul summaries. |
| `game_events` | Immutable relational event envelope for scorekeeping, fouls, timer changes, corrections, and finalization. |

## Relationship Summary

- `User` owns zero or more `Team` rows through `teams.owner_user_id`.
- `User` can optionally link to one `Player` profile through `players.user_id`.
- `Team` and `Player` are connected through `TeamMembership`.
- `League` has many `Tournament` rows and many `Game` rows.
- `Tournament` belongs to an optional `League` and has many `Game` rows.
- `Game` belongs to optional home/away `Team` rows, an optional `League`, and an optional `Tournament`.
- `GameEvent` belongs to one `Game`, can optionally reference a `Player`, the involved `Team`, the `User` who recorded it, and another `GameEvent` when it is a correction.

## Audit and Soft Delete Policy

All core mutable entities include `created_at` and `updated_at`.

Soft delete is included only for user-visible mutable entities that can be referenced by historical records: `users`, `teams`, `players`, `leagues`, `tournaments`, and `games`. This preserves game history and roster references when records are hidden from normal views.

`team_memberships` does not use soft delete because `status` and `ended_at` preserve roster history more clearly.

`game_events` does not use soft delete because events should form an immutable audit trail. Corrections should be represented by a new correction event that references the original event through `correction_of_event_id`.

## RBAC and Authentication Assumptions

The model includes only basic RBAC-related fields:

- `users.role`
- `users.is_active`
- `teams.owner_user_id`
- `team_memberships.role`
- `team_memberships.approved_by_user_id`

No password hash, session, OAuth identity, phone verification, email verification, bank account verification, card verification, or production authentication tables are added in this phase.

## PostgreSQL vs MongoDB Assumption

The current user request explicitly asks for SQLAlchemy models for `game_events`, so the MVP model stores a minimal deterministic event envelope in PostgreSQL. Large flexible event snapshots, play-by-play projections, comments, and document metadata can be added to MongoDB later only after a synchronization rule is documented.

## Migration Readiness

Alembic scaffolding is included under `backend/alembic/` and points at `app.models.Base.metadata` for autogeneration.

From `backend/`, the intended migration commands are:

```bash
alembic revision --autogenerate -m "create phase 1 core tables"
alembic upgrade head
```

No migration revision is generated yet because the project has not connected to a live development database in this task.
