from app.api.routes.placeholder_factory import build_placeholder_router

router = build_placeholder_router(
    prefix="/players",
    tag="players",
    resource="players",
    message="Player CRUD and privacy-safe profile responses will be added here.",
)
