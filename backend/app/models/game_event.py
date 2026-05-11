from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any
from uuid import UUID

from sqlalchemy import JSON, DateTime, Enum, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from app.db.base import Base, TimestampMixin, UuidPrimaryKeyMixin
from app.models.enums import GameEventType

if TYPE_CHECKING:
    from app.models.game import Game
    from app.models.player import Player
    from app.models.user import User


class GameEvent(UuidPrimaryKeyMixin, TimestampMixin, Base):
    """Immutable relational game-event envelope for deterministic scoring and corrections."""

    __tablename__ = "game_events"
    __table_args__ = (UniqueConstraint("game_id", "sequence", name="uq_game_events_game_sequence"),)

    game_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("games.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    sequence: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="Monotonic per-game event order used for deterministic replay.",
    )
    event_type: Mapped[GameEventType] = mapped_column(
        Enum(GameEventType, name="game_event_type"),
        nullable=False,
    )
    occurred_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        comment="When the court action occurred, not just when the row was inserted.",
    )
    period: Mapped[int | None] = mapped_column(Integer, nullable=True)
    clock_seconds_remaining: Mapped[int | None] = mapped_column(Integer, nullable=True)
    team_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("teams.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    player_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("players.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    recorded_by_user_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
        comment="Scorekeeper/admin who entered the event when known.",
    )
    points_delta: Mapped[int | None] = mapped_column(Integer, nullable=True)
    foul_delta: Mapped[int | None] = mapped_column(Integer, nullable=True)
    correction_of_event_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("game_events.id", ondelete="SET NULL"),
        nullable=True,
        comment="Correction events reference the original event instead of deleting history.",
    )
    payload: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
        comment=(
            "Small validated event metadata; large/flexible snapshots can move "
            "to MongoDB later."
        ),
    )
    source: Mapped[str | None] = mapped_column(String(40), nullable=True)

    game: Mapped[Game] = relationship(back_populates="events")
    player: Mapped[Player | None] = relationship(back_populates="game_events")
    recorded_by: Mapped[User | None] = relationship(back_populates="recorded_game_events")
    correction_of: Mapped[GameEvent | None] = relationship(remote_side="GameEvent.id")
