from sqlalchemy import inspect

from app.models import Base, Game, GameEvent, TeamMembership, User, UserRole


def test_phase_1_model_tables_are_registered() -> None:
    assert set(Base.metadata.tables) >= {
        "users",
        "teams",
        "players",
        "leagues",
        "tournaments",
        "games",
        "game_events",
        "team_memberships",
    }


def test_user_model_has_rbac_and_audit_columns() -> None:
    columns = {column.name for column in User.__table__.columns}

    assert {
        "id",
        "email",
        "display_name",
        "role",
        "is_active",
        "created_at",
        "updated_at",
    } <= columns
    assert User.__table__.c.role.default.arg == UserRole.USER


def test_game_event_model_keeps_deterministic_event_order_and_corrections() -> None:
    columns = {column.name for column in GameEvent.__table__.columns}
    constraints = {constraint.name for constraint in GameEvent.__table__.constraints}

    assert {"game_id", "sequence", "event_type", "correction_of_event_id", "payload"} <= columns
    assert "uq_game_events_game_sequence" in constraints


def test_core_relationships_are_declared() -> None:
    game_relationships = {relationship.key for relationship in inspect(Game).relationships}
    membership_relationships = {
        relationship.key for relationship in inspect(TeamMembership).relationships
    }

    assert {"home_team", "away_team", "events", "league", "tournament"} <= game_relationships
    assert {"team", "player", "approved_by"} <= membership_relationships
