import logging
from typing import Any

from app.core.config import get_settings


def configure_logging() -> None:
    """Configure process-wide logging for development and tests."""

    logging.basicConfig(
        level=get_settings().log_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def log_structured_event(logger: logging.Logger, action: str, result: str, **fields: Any) -> None:
    """Log a structured event without leaking sensitive raw values."""

    safe_fields = {key: value for key, value in fields.items() if value is not None}
    logger.info("event", extra={"action": action, "result": result, **safe_fields})
