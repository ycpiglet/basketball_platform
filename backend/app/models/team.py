from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from app.db.base import Base, SoftDeleteMixin, TimestampMixin, UuidPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.game import Game
    from app.models.team_membership import TeamMembership
    from app.models.user import User


class Team(UuidPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin, Base):
    """Team profile managed by a team manager; roster membership is modeled separately."""

    __tablename__ = "teams"

    name: Mapped[str] = mapped_column(String(160), nullable=False, index=True)
    short_name: Mapped[str | None] = mapped_column(String(40), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    owner_user_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
        comment="Initial ownership hook for Team Manager permissions; production auth is deferred.",
    )

    owner: Mapped[User | None] = relationship(back_populates="owned_teams")
    memberships: Mapped[list[TeamMembership]] = relationship(back_populates="team")
    home_games: Mapped[list[Game]] = relationship(
        back_populates="home_team",
        foreign_keys="Game.home_team_id",
    )
    away_games: Mapped[list[Game]] = relationship(
        back_populates="away_team",
        foreign_keys="Game.away_team_id",
    )
