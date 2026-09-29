from collections.abc import Callable
from threading import RLock

from app.services.scoreboard_state import ScoreboardState, ScoreboardStateService


class ScoreboardGameNotFoundError(LookupError):
    """Raised when a requested pilot scoreboard game does not exist."""


class ScoreboardGameConflictError(ValueError):
    """Raised when a pilot scoreboard game id already exists."""


class InMemoryScoreboardStore:
    """Pilot-only in-memory scoreboard store.

    This is intentionally small and replaceable. It gives the field pilot one
    backend-owned game state without committing the MVP to a persistence design.
    """

    def __init__(self, service: ScoreboardStateService | None = None) -> None:
        self._service = service or ScoreboardStateService()
        self._games: dict[str, ScoreboardState] = {}
        self._lock = RLock()

    def create_game(self, game_id: str | None = None) -> ScoreboardState:
        """Create a new pilot game state."""

        with self._lock:
            state = self._service.create_game(game_id)
            if state.game_id in self._games:
                raise ScoreboardGameConflictError(
                    f"Scoreboard game already exists: {state.game_id}."
                )
            self._games[state.game_id] = state
            return state

    def get_game(self, game_id: str) -> ScoreboardState:
        """Return an existing pilot game state."""

        with self._lock:
            try:
                return self._games[game_id]
            except KeyError as exc:
                raise ScoreboardGameNotFoundError(f"Scoreboard game not found: {game_id}.") from exc

    def mutate_game(
        self,
        game_id: str,
        operation: Callable[[ScoreboardState], ScoreboardState],
    ) -> ScoreboardState:
        """Apply a state mutation while holding the pilot store lock."""

        with self._lock:
            state = self.get_game(game_id)
            return operation(state)

    def clear(self) -> None:
        """Clear all pilot games for tests or controlled local reset."""

        with self._lock:
            self._games.clear()
