from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, SoftDeleteMixin, TimestampMixin, UuidPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.game import Game
    from app.models.tournament import Tournament


class League(UuidPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin, Base):
    """League grouping for schedules, standings, tournaments, and public results."""

    __tablename__ = "leagues"

    name: Mapped[str] = mapped_column(String(160), nullable=False, index=True)
    season: Mapped[str | None] = mapped_column(String(80), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    starts_on: Mapped[date | None] = mapped_column(Date, nullable=True)
    ends_on: Mapped[date | None] = mapped_column(Date, nullable=True)

    tournaments: Mapped[list[Tournament]] = relationship(back_populates="league")
    games: Mapped[list[Game]] = relationship(back_populates="league")
