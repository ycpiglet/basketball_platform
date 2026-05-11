from app.api.routes.placeholder_factory import build_placeholder_router

router = build_placeholder_router(
    prefix="/users",
    tag="users",
    resource="users",
    message="User profile and role APIs will be added after the Phase 1 auth contract is defined.",
)
