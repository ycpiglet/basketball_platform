# Test Cases

This folder organizes planned and manual test cases. Executable tests still
belong in the framework-native locations:

- Backend: `backend/tests/`
- Frontend: `frontend/src/tests/`

## Structure

```text
test_cases/
|- functional_test/
|  |- smoke_test/
|  |- sanity_test/
|  |- regression_test/
|- non_functional_test/
|  |- availability_test/
|  |- performance_test/
|  |  |- load_test/
|  |  |- stress_test/
|  |- security_test/
|- v_model/
|  |- unit_test/
|  |- integration_test/
|  |- system_test/
|  |- acceptance_test/
```

## Test Case Naming

```text
tc_<domain>_<behavior>.md
```

Examples:

- `tc_scoreboard_score_increment.md`
- `tc_records_player_foul_limit.md`
- `tc_permissions_team_manager_roster_scope.md`

