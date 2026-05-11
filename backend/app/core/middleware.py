import logging
import time
from collections.abc import Awaitable, Callable
from http import HTTPStatus
from uuid import uuid4

from fastapi import Request, Response
from fastapi.responses import JSONResponse

from app.core.logging import log_structured_event

logger = logging.getLogger(__name__)


async def request_context_middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    """Attach a request id, log request completion, and catch unhandled exceptions."""

    request_id = request.headers.get("x-request-id") or str(uuid4())
    request.state.request_id = request_id
    started_at = time.perf_counter()

    try:
        response = await call_next(request)
    except Exception as exc:  # noqa: BLE001 - intentional global safety net for API responses.
        duration_ms = round((time.perf_counter() - started_at) * 1000, 2)
        log_structured_event(
            logger,
            action="http_request_unhandled_exception",
            result="error",
            level=logging.ERROR,
            request_id=request_id,
            method=request.method,
            path=request.url.path,
            duration_ms=duration_ms,
            error_code="internal_server_error",
            error_type=type(exc).__name__,
        )
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "error": {
                    "code": "internal_server_error",
                    "message": "Unexpected server error.",
                    "request_id": request_id,
                    "fields": [],
                }
            },
            headers={"X-Request-ID": request_id},
        )

    duration_ms = round((time.perf_counter() - started_at) * 1000, 2)
    response.headers["X-Request-ID"] = request_id
    log_structured_event(
        logger,
        action="http_request_completed",
        result="success" if response.status_code < 500 else "error",
        request_id=request_id,
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        duration_ms=duration_ms,
    )
    return response
