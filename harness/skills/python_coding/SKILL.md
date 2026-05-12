---
name: python-coding
description: >
  Apply this skill whenever writing, reviewing, or refactoring Python code.
  Triggers on any Python implementation task: new modules, functions, classes,
  scripts, SDK integrations, or robot control code. Use this skill even for
  small snippets — quality standards apply at every scale.
---

# Python Coding Standard

## Domain Adaptation

Before writing code, identify the active domain and apply the corresponding priorities.
Principles are universal; emphasis and tradeoffs shift by domain.

| Domain | Primary concern | Validation posture | State model |
|---|---|---|---|
| **Robot / Embedded** | Physical safety, determinism | Strict raise on limit violation | Minimal, explicit |
| **Server / Backend** | Reliability, concurrent correctness | Raise on contract violation, log context | Stateless preferred |
| **Network / Protocol** | Fault tolerance, partial failure | Defensive — assume anything can fail | Session/connection aware |
| **IoT / Edge** | Resource constraints, recovery | Clamp + warn on soft limits | Persistent, resumable |
| **Data / ML pipeline** | Reproducibility, traceability | Schema validation at boundaries | Immutable inputs |
| **Frontend / CLI** | User-facing clarity | Catch and surface errors clearly | UI state explicit |

When the domain is ambiguous or crosses multiple areas, apply the strictest relevant posture.

---

## Principles (Priority Order)

1. **Correctness** — verified behavior, not assumed
2. **Readability / Intuitiveness** — understood at a glance, without comments
3. **Reproducibility** — same input → same output, no hidden state or call-order dependency
4. **Maintainability** — modifiable without breaking other parts
5. **Flexibility / Extensibility** — new requirements require addition, not rewriting

---

## Code Structure

### Naming

| Convention | Example | Used for |
|---|---|---|
| `snake_case` | `retry_count`, `packet_size` | variables, functions |
| `PascalCase` | `ConnectionPool`, `JointController` | classes |
| `UPPER_SNAKE_CASE` | `MAX_RETRIES`, `DEFAULT_TIMEOUT` | module-level constants |
| `is_` / `has_` / `can_` prefix | `is_connected`, `has_pending` | boolean variables and functions |

Domain-standard abbreviations are acceptable without expansion (`dof`, `pid`, `imu`, `ttl`, `mtu`, `orm`, `api`).

### Functions

- **Single responsibility**: one function does one thing. If you need "and" to describe what it does, split it.
- **Length**: no fixed line limit. The practical test — can the entire function be read without scrolling? If not, consider extracting a sub-function, but only when the extracted piece has a clear, nameable responsibility. Over-decomposition (splitting until everything is trivially small) increases navigation burden without benefit.
- All parameters and return values must have type hints.
- Default arguments must be immutable — use `None` as sentinel, never `[]` or `{}`.

```python
# Wrong
def process(items, config={}):
    ...

# Correct
def process(items: list[str], config: dict | None = None) -> list[str]:
    if config is None:
        config = {}
    ...
```

### Classes

- Use `@dataclass` for pure data containers (no significant behavior).
- Use regular classes when behavior (methods) is primary.
- Avoid complex logic in `__init__`. Use `@classmethod` factory methods for non-trivial construction.

### Reproducibility Rules

- No module-level mutable state that persists between calls
- No call-order dependencies (A must be called before B without documentation)
- Seed random generators explicitly when reproducibility matters
- Isolate time-dependent calls (`datetime.now()`, `time.time()`) behind injectable parameters for testability
- External I/O (files, network, DB) must be explicit in function signatures — no hidden globals

---

## Input / Output Validation

The validation posture depends on the consequence of a bad value getting through:

**Raise** when a bad value causes irreversible damage (hardware, data corruption, security):
```python
# Robot: out-of-range angle damages hardware
# Server: invalid user ID corrupts DB record
# Network: malformed packet breaks protocol state
if not (MIN <= value <= MAX):
    raise ValueError(f"value={value!r} out of [{MIN}, {MAX}]")
```

**Clamp + warn** when a bad value is recoverable and the user should be notified:
```python
# Tuning parameter: speed, volume, opacity
if not (0.0 <= ratio <= 1.0):
    logger.warning("ratio=%.3f clamped to [0.0, 1.0]", ratio)
    ratio = max(0.0, min(1.0, ratio))
```

**Catch and surface** for user-facing code (CLI, API responses):
```python
# Don't let internal exceptions leak to the user
except ValueError as e:
    return {"error": str(e), "field": "ratio"}, 400
```

Always include the offending value and valid range in the error message.

---

## Constants and Default Arguments

Every constant and non-obvious default must document:
1. **What it means** (physical, logical, or protocol significance)
2. **Why this specific value** was chosen
3. **How to tune it** and what breaks at the extremes

```python
# Maximum retry attempts for gRPC/HTTP commands.
# Increase for unreliable networks; 0 disables retries entirely.
# Above 5 causes noticeable latency on hard failures.
MAX_RETRIES: int = 3

# Connection timeout in seconds.
# Increase if target host is slow to respond (embedded devices, remote servers).
# Decrease in latency-sensitive loops — but below 0.5 causes false timeouts on load.
TIMEOUT_SEC: float = 5.0
```

---

## Error Handling

- Catch specific exceptions only — never bare `except:`.
- Use `logger.exception()` inside `except` blocks — it automatically includes the full traceback.
- Use `raise X from e` to preserve the original cause when re-raising as a different type.
- Error messages must answer: what was attempted, what values were involved, what failed.

```python
try:
    response = client.send(payload)
except TimeoutError as e:
    logger.exception("Request timed out: endpoint=%s, payload_size=%d", endpoint, len(payload))
    raise RuntimeError(f"Command to {endpoint!r} timed out after {TIMEOUT_SEC}s") from e
```

Use `assert` only for internal invariants — not for user-facing validation:

```python
# Internal guard (developer-facing): documents an assumption that must hold
assert len(buffer) % FRAME_SIZE == 0, f"Buffer misaligned: {len(buffer)} % {FRAME_SIZE} != 0"

# User-facing: explicit raise with a clear message
if len(buffer) % FRAME_SIZE != 0:
    raise ValueError(f"Buffer length {len(buffer)} is not a multiple of frame size {FRAME_SIZE}")
```

---

## Documentation

### Docstrings (Google style — required for all public functions and classes)

```python
def send_command(endpoint: str, payload: bytes, retries: int = MAX_RETRIES) -> Response:
    """Send a command to the target endpoint with retry logic.

    Args:
        endpoint: Target address (e.g., "192.168.0.1:50051" or "/api/v1/cmd").
        payload: Raw bytes to send. Must be non-empty.
        retries: Number of retry attempts on transient failure.
            Set to 0 to disable retries. See MAX_RETRIES for tuning guidance.

    Returns:
        Response object containing status code and body.

    Raises:
        ValueError: If payload is empty or endpoint is malformed.
        RuntimeError: If all retry attempts are exhausted.
    """
```

### Inline Comments

Only for non-obvious logic. Explain **why**, not **what**:

```python
# Wrong: data = data[:-1]  # remove last element
# Correct: data = data[:-1]  # strip trailing null byte added by legacy firmware
```

Design rationale — why this structure, algorithm, or library was chosen — belongs in the **response text**, not in code.

---

## Logging

Never use `print()` in production code. Use the `logging` module (or the project's `logger_setup.py` if available).

```python
from logger_setup import get_logger   # if logger_setup.py exists in project
# or
import logging
logger = logging.getLogger(__name__)  # standard fallback
```

### Log Level Guide

| Level | When to use |
|---|---|
| `DEBUG` | Internal state, loop values, verbose trace |
| `INFO` | Major state transitions, connection events, milestones |
| `WARNING` | Recoverable issues — values clamped, retries triggered, fallback used |
| `ERROR` | Operation failed, output affected — use `logger.exception()` in except blocks |
| `CRITICAL` | System cannot continue — hardware fault, unrecoverable state |

### Exception Logging Pattern

```python
try:
    result = execute(cmd)
except Exception:
    # logger.exception() captures traceback automatically — no need to pass `e`
    logger.exception("Execution failed: cmd=%s, state=%r", cmd, current_state)
    raise
```

### logger_setup.py Integration (if present in project)

```python
from logger_setup import setup_development, setup_production, setup_quiet, set_module_level

setup_development()              # DEBUG + color, no file
setup_production()               # INFO + file logging, no color
setup_quiet()                    # ERROR/CRITICAL only

set_module_level("rby1_sdk", "ERROR")   # silence a noisy library at runtime
```

Environment variable overrides (no code change needed):
```bash
LOG_LEVEL=DEBUG python main.py
LOG_FILE=true   python main.py    # → ./logs/robot_YYYYMMDD.log
LOG_COLOR=false python main.py
```

---

## Testing

Tests are the primary verification mechanism. They must be readable without looking at the implementation.

### Structure

```python
import pytest

class TestSendCommand:
    """Unit tests for send_command()."""

    def test_valid_request_returns_response(self):
        """Normal case: valid endpoint and payload returns a Response."""
        response = send_command("localhost:50051", b"ping")
        assert response.status == 200

    def test_empty_payload_raises(self):
        """Empty payload must raise ValueError with 'payload' in message."""
        with pytest.raises(ValueError, match="payload"):
            send_command("localhost:50051", b"")

    def test_retry_exhaustion_raises_runtime_error(self, mock_failing_client):
        """Exhausting all retries must raise RuntimeError, not the underlying error."""
        with pytest.raises(RuntimeError, match="exhausted"):
            send_command("bad-host:9999", b"data", retries=2)

    def test_warning_logged_on_retry(self, caplog, mock_flaky_client):
        """Each retry attempt must emit a WARNING log."""
        with caplog.at_level(logging.WARNING):
            send_command("flaky:50051", b"data", retries=2)
        assert caplog.text.count("retry") == 2
```

### Coverage Checklist (every function)

- [ ] Normal / happy path
- [ ] Boundary values (min, max, zero, empty)
- [ ] Invalid input — type or range violations
- [ ] Exception messages contain the relevant identifiers
- [ ] Warnings / side effects verified where applicable
- [ ] Domain-specific failure modes (network: timeout, disconnect; robot: limit breach; DB: constraint violation)

---

## Module Layout

```python
"""Module docstring: what this module does and its scope."""

# 1. Standard library
import logging
from dataclasses import dataclass
from pathlib import Path

# 2. Third-party
import numpy as np          # if applicable

# 3. Local
from logger_setup import get_logger
from .config import AppConfig

# 4. Constants (with rationale comments)
MAX_RETRIES: int = 3
TIMEOUT_SEC: float = 5.0

# 5. Logger
logger = get_logger(__name__)

# 6. Data classes / type definitions

# 7. Main classes / functions

# 8. Tests (or in separate test_<module>.py)
```

---

## Python Version

Target: **Python 3.10+**

Prefer modern syntax:
- `X | Y` over `Union[X, Y]` for type hints
- `match` statement for multi-branch dispatch
- `@dataclass` over manual `__init__` for data containers
- `pathlib.Path` over `os.path`
- f-string over `.format()` or `%`
