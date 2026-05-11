# MVP Scoreboard State Model

The initial scoreboard state model lives in `backend/app/services/scoreboard_state.py`. It is a pure Python service so the rules can be tested without the Vue UI, FastAPI routes, database persistence, WebSocket transport, or hardware integrations.

## Included State

- Home score and away score
- Quarter number
- Game clock status and remaining seconds
- Team fouls by side
- Timeout counts by side
- Player points
- Player fouls
- Game status
- In-memory game event log entries with monotonically increasing sequence numbers

## State-changing Operations

The MVP service currently supports:

- Add 1, 2, or 3 points to a team and player
- Correct a team score with a required reason
- Add a team foul
- Add a player foul, which also increments the matching team foul count
- Use a timeout while counts remain
- Start and stop the clock
- Set the active quarter and reset/adjust remaining clock seconds
- End/finalize the game

Every state-changing method validates its input, appends a `ScoreboardEventLogEntry`, and emits a structured log through `log_structured_event`.

## Validation Rules

- Scoring updates must be exactly 1, 2, or 3 points.
- Corrected scores cannot be negative and require a non-empty reason.
- Quarter must be 1 or greater.
- Clock remaining seconds cannot be negative.
- Timeout counts cannot go below zero.
- Finalized games cannot be changed.
- Player IDs are required for player-level score and foul events.

## Hardware Independence

This service intentionally does not know about RS-485, RF, packet formats, HDMI display, or any other hardware integration. Future hardware adapters should consume validated scoreboard state/events through a separate integration boundary.
