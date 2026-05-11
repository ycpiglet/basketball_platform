from fastapi import APIRouter

from app.api.routes import games, health, leagues, players, scoreboard, teams, tournaments, users

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(users.router)
api_router.include_router(teams.router)
api_router.include_router(players.router)
api_router.include_router(games.router)
api_router.include_router(leagues.router)
api_router.include_router(tournaments.router)
api_router.include_router(scoreboard.router)
