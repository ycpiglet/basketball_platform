from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, SoftDeleteMixin, TimestampMixin, UuidPrimaryKeyMixin
from app.models.enums import UserRole

if TYPE_CHECKING:
    from app.models.game_event import GameEvent
    from app.models.player import Player
    from app.models.team import Team
    from app.models.team_membership import TeamMembership


class User(UuidPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin, Base):
    """Application account shell with RBAC role only; production auth is intentionally deferred."""

    __tablename__ = "users"

    email: Mapped[str | None] = mapped_column(
        String(320),
        unique=True,
        nullable=True,
        index=True,
        comment="Nullable until the production authentication provider and signup flow are chosen.",
    )
    display_name: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"),
        default=UserRole.USER,
        nullable=False,
        comment="Basic RBAC role; not a complete authentication or authorization system.",
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    owned_teams: Mapped[list[Team]] = relationship(back_populates="owner")
    player_profile: Mapped[Player | None] = relationship(back_populates="user")
    approved_memberships: Mapped[list[TeamMembership]] = relationship(back_populates="approved_by")
    recorded_game_events: Mapped[list[GameEvent]] = relationship(back_populates="recorded_by")
