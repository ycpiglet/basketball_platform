from app.api.routes.placeholder_factory import build_placeholder_router

router = build_placeholder_router(
    prefix="/teams",
    tag="teams",
    resource="teams",
    message="Team CRUD, roster, and team-manager ownership checks will be added here.",
)
