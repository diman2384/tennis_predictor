from fastapi import APIRouter
from app.services.sentiment_analysis import SentimentAnalyzer

router = APIRouter()
sentiment_analyzer = SentimentAnalyzer()


@router.get("/{player_id}")
async def get_player(player_id: int):
    """Get player profile."""
    return {
        "id": player_id,
        "name": "Player Name",
        "country": "RUS",
        "ranking": 15,
        "age": 25,
        "plays": "right-handed"
    }


@router.get("/{player_id}/form")
async def get_player_form(player_id: int):
    """Get player current form."""
    return {
        "win_rate_10": 0.70,
        "win_rate_20": 0.65,
        "current_streak": 3,
        "aces_per_match": 8.5,
        "double_faults_per_match": 2.1,
        "form_score": 72,
        "last_matches": ["W", "W", "W", "L", "W"]
    }


@router.get("/{player_id}/sentiment")
async def get_player_sentiment(player_id: int):
    """Get player sentiment analysis."""
    return await sentiment_analyzer.get_overall_sentiment("Player Name")