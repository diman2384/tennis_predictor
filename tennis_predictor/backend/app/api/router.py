from fastapi import APIRouter
from app.api.routes import auth, matches, predictions, players

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(matches.router, prefix="/matches", tags=["matches"])
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])
api_router.include_router(players.router, prefix="/players", tags=["players"])