from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from app.db.base import Base, SoftDeleteMixin, TimestampMixin, UuidPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.game_event import GameEvent
    from app.models.team_membership import TeamMembership
    from app.models.user import User


class Player(UuidPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin, Base):
    """Basketball participant profile with an optional user-account link."""

    __tablename__ = "players"

    user_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        unique=True,
        nullable=True,
        comment="Optional account link; players may be rostered before they create user accounts.",
    )
    display_name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    jersey_number: Mapped[str | None] = mapped_column(String(10), nullable=True)
    position: Mapped[str | None] = mapped_column(String(20), nullable=True)
    birth_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
        comment="Sensitive by default; API responses must mask unless permission allows access.",
    )

    user: Mapped[User | None] = relationship(back_populates="player_profile")
    memberships: Mapped[list[TeamMembership]] = relationship(back_populates="player")
    game_events: Mapped[list[GameEvent]] = relationship(back_populates="player")
