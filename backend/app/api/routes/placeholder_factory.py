import logging

from fastapi import APIRouter, Request, status

from app.core.logging import log_structured_event
from app.schemas.placeholders import (
    PlaceholderInfoResponse,
    PlaceholderValidationRequest,
    PlaceholderValidationResponse,
)

logger = logging.getLogger(__name__)


def build_placeholder_router(prefix: str, tag: str, resource: str, message: str) -> APIRouter:
    """Create a Phase 1 placeholder router with a minimal validation example."""

    router = APIRouter(prefix=prefix, tags=[tag])

    @router.get("", response_model=PlaceholderInfoResponse)
    def get_placeholder() -> PlaceholderInfoResponse:
        return PlaceholderInfoResponse(resource=resource, message=message)

    @router.post(
        "/validation-preview",
        response_model=PlaceholderValidationResponse,
        status_code=status.HTTP_202_ACCEPTED,
    )
    def validate_placeholder_payload(
        payload: PlaceholderValidationRequest,
        request: Request,
    ) -> PlaceholderValidationResponse:
        log_structured_event(
            logger,
            action="placeholder_payload_validated",
            result="success",
            request_id=getattr(request.state, "request_id", None),
            target_entity_type=resource,
        )
        return PlaceholderValidationResponse(
            resource=resource,
            accepted=True,
            received_name=payload.name,
            notes=payload.notes,
        )

    return router
