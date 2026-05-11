from app.api.routes.placeholder_factory import build_placeholder_router

router = build_placeholder_router(
    prefix="/games",
    tag="games",
    resource="games",
    message="Game setup, live state, result, and box score APIs will be added here.",
)
