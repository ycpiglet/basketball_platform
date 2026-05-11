import logging
from http import HTTPStatus

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.logging import log_structured_event

logger = logging.getLogger(__name__)


def _request_id(request: Request) -> str | None:
    return getattr(request.state, "request_id", None)


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    request_id = _request_id(request)
    log_structured_event(
        logger,
        action="http_exception",
        result="error",
        level=logging.WARNING,
        request_id=request_id,
        method=request.method,
        path=request.url.path,
        status_code=exc.status_code,
    )
    try:
        error_code = HTTPStatus(exc.status_code).phrase.lower().replace(" ", "_")
    except ValueError:
        error_code = "http_error"

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": error_code,
                "message": str(exc.detail),
                "request_id": request_id,
                "fields": [],
            }
        },
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    request_id = _request_id(request)
    fields = [".".join(str(part) for part in error["loc"]) for error in exc.errors()]
    log_structured_event(
        logger,
        action="request_validation_failed",
        result="error",
        level=logging.WARNING,
        request_id=request_id,
        method=request.method,
        path=request.url.path,
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        fields=fields,
    )
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "code": "validation_error",
                "message": "Request validation failed.",
                "request_id": request_id,
                "fields": fields,
            }
        },
    )
