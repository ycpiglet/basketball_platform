from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from app.db.base import Base, SoftDeleteMixin, TimestampMixin, UuidPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.game import Game
    from app.models.league import League


class Tournament(UuidPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin, Base):
    """Tournament container for bracket/schedule management in Phase 1."""

    __tablename__ = "tournaments"

    league_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("leagues.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(160), nullable=False, index=True)
    format: Mapped[str | None] = mapped_column(String(80), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    starts_on: Mapped[date | None] = mapped_column(Date, nullable=True)
    ends_on: Mapped[date | None] = mapped_column(Date, nullable=True)

    league: Mapped[League | None] = relationship(back_populates="tournaments")
    games: Mapped[list[Game]] = relationship(back_populates="tournament")
