import json
import logging
from collections.abc import Mapping
from datetime import UTC, datetime
from typing import Any

from app.core.config import get_settings

_RESERVED_LOG_RECORD_KEYS = {
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
}

SENSITIVE_FIELD_NAMES = {
    "password",
    "token",
    "access_token",
    "refresh_token",
    "authorization",
    "secret",
    "private_key",
    "card_number",
    "bank_account",
}


class JsonFormatter(logging.Formatter):
    """Format application logs as JSON so request and action fields stay queryable."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": datetime.fromtimestamp(record.created, tz=UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        for key, value in record.__dict__.items():
            if key not in _RESERVED_LOG_RECORD_KEYS and not key.startswith("_"):
                payload[key] = _mask_if_sensitive(key, value)

        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)

        return json.dumps(payload, ensure_ascii=False, default=str)


def configure_logging() -> None:
    """Configure process-wide structured logging for development, tests, and deployment."""

    root_logger = logging.getLogger()
    root_logger.setLevel(get_settings().log_level)

    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())

    root_logger.handlers.clear()
    root_logger.addHandler(handler)


def log_structured_event(
    logger: logging.Logger,
    action: str,
    result: str,
    level: int = logging.INFO,
    **fields: Any,
) -> None:
    """Log a structured event without leaking sensitive raw values."""

    safe_fields = {
        key: _mask_if_sensitive(key, value)
        for key, value in fields.items()
        if value is not None
    }
    logger.log(level, "event", extra={"action": action, "result": result, **safe_fields})


def _mask_if_sensitive(key: str, value: Any) -> Any:
    if key.lower() in SENSITIVE_FIELD_NAMES:
        return "***"

    if isinstance(value, Mapping):
        return {
            nested_key: _mask_if_sensitive(str(nested_key), nested_value)
            for nested_key, nested_value in value.items()
        }

    return value
