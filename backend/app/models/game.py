from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from app.db.base import Base, SoftDeleteMixin, TimestampMixin, UuidPrimaryKeyMixin
from app.models.enums import GameStatus

if TYPE_CHECKING:
    from app.models.game_event import GameEvent
    from app.models.league import League
    from app.models.team import Team
    from app.models.tournament import Tournament


class Game(UuidPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin, Base):
    """Scheduled or completed game with relational links and denormalized current score."""

    __tablename__ = "games"

    league_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("leagues.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    tournament_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("tournaments.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    home_team_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("teams.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    away_team_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("teams.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    venue_name: Mapped[str | None] = mapped_column(String(160), nullable=True)
    scheduled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[GameStatus] = mapped_column(
        Enum(GameStatus, name="game_status"),
        default=GameStatus.SCHEDULED,
        nullable=False,
    )
    period: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    home_score: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    away_score: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    home_team_fouls: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    away_team_fouls: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    league: Mapped[League | None] = relationship(back_populates="games")
    tournament: Mapped[Tournament | None] = relationship(back_populates="games")
    home_team: Mapped[Team | None] = relationship(
        back_populates="home_games",
        foreign_keys=[home_team_id],
    )
    away_team: Mapped[Team | None] = relationship(
        back_populates="away_games",
        foreign_keys=[away_team_id],
    )
    events: Mapped[list[GameEvent]] = relationship(
        back_populates="game",
        order_by="GameEvent.sequence",
    )
