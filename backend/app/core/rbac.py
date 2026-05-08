from enum import StrEnum


class Role(StrEnum):
    GUEST = "guest"
    USER = "user"
    TEAM_MANAGER = "team_manager"
    SYSTEM_ADMIN = "system_admin"


_ROLE_RANK: dict[Role, int] = {
    Role.GUEST: 0,
    Role.USER: 1,
    Role.TEAM_MANAGER: 2,
    Role.SYSTEM_ADMIN: 3,
}


def has_minimum_role(current_role: Role, required_role: Role) -> bool:
    """Return whether the current role satisfies a minimum role requirement."""

    return _ROLE_RANK[current_role] >= _ROLE_RANK[required_role]
