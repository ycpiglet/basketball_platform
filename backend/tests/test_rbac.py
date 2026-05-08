from app.core.rbac import Role, has_minimum_role


def test_system_admin_satisfies_team_manager_requirement() -> None:
    assert has_minimum_role(Role.SYSTEM_ADMIN, Role.TEAM_MANAGER)


def test_guest_does_not_satisfy_team_manager_requirement() -> None:
    assert not has_minimum_role(Role.GUEST, Role.TEAM_MANAGER)
