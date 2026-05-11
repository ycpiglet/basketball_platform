from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from app.db.base import Base, TimestampMixin, UuidPrimaryKeyMixin
from app.models.enums import TeamMembershipRole, TeamMembershipStatus

if TYPE_CHECKING:
    from app.models.player import Player
    from app.models.team import Team
    from app.models.user import User


class TeamMembership(UuidPrimaryKeyMixin, TimestampMixin, Base):
    """Roster and team-management membership with status history instead of soft deletion."""

    __tablename__ = "team_memberships"
    __table_args__ = (
        UniqueConstraint("team_id", "player_id", name="uq_team_memberships_team_player"),
    )

    team_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("teams.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    player_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("players.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    role: Mapped[TeamMembershipRole] = mapped_column(
        Enum(TeamMembershipRole, name="team_membership_role"),
        default=TeamMembershipRole.PLAYER,
        nullable=False,
    )
    status: Mapped[TeamMembershipStatus] = mapped_column(
        Enum(TeamMembershipStatus, name="team_membership_status"),
        default=TeamMembershipStatus.ACTIVE,
        nullable=False,
    )
    approved_by_user_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        comment="Audit hook for future team-manager approval workflows.",
    )
    joined_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    ended_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        comment="Set when membership ends; preserves roster history without soft delete.",
    )

    team: Mapped[Team] = relationship(back_populates="memberships")
    player: Mapped[Player] = relationship(back_populates="memberships")
    approved_by: Mapped[User | None] = relationship(back_populates="approved_memberships")
