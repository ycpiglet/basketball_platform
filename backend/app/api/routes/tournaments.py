from app.api.routes.placeholder_factory import build_placeholder_router

router = build_placeholder_router(
    prefix="/tournaments",
    tag="tournaments",
    resource="tournaments",
    message="Tournament CRUD, brackets, game lists, and result workflows will be added here.",
)
