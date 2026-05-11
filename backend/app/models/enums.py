from enum import StrEnum


class UserRole(StrEnum):
    GUEST = "guest"
    USER = "user"
    TEAM_MANAGER = "team_manager"
    SYSTEM_ADMIN = "system_admin"


class TeamMembershipRole(StrEnum):
    PLAYER = "player"
    CAPTAIN = "captain"
    MANAGER = "manager"
    GUEST = "guest"


class TeamMembershipStatus(StrEnum):
    INVITED = "invited"
    ACTIVE = "active"
    INACTIVE = "inactive"
    REMOVED = "removed"


class GameStatus(StrEnum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    FINAL = "final"
    CANCELLED = "cancelled"


class GameEventType(StrEnum):
    SCORE = "score"
    FOUL = "foul"
    TIMER = "timer"
    TIMEOUT = "timeout"
    SUBSTITUTION = "substitution"
    PERIOD = "period"
    CORRECTION = "correction"
    FINALIZATION = "finalization"
