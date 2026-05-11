from app.api.routes.placeholder_factory import build_placeholder_router

router = build_placeholder_router(
    prefix="/scoreboard",
    tag="scoreboard",
    resource="scoreboard",
    message="Scoreboard state, timer, foul, and display synchronization APIs will be added here.",
)
