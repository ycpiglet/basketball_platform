from app.api.routes.placeholder_factory import build_placeholder_router

router = build_placeholder_router(
    prefix="/leagues",
    tag="leagues",
    resource="leagues",
    message="League CRUD, schedules, standings, and public result APIs will be added here.",
)
