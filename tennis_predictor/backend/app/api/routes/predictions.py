from fastapi import APIRouter
from pydantic import BaseModel
from app.services.predictor import TennisPredictor
from app.services.sentiment_analysis import SentimentAnalyzer
from app.services.llm_analyzer import LLMAnalyzer

router = APIRouter()
predictor = TennisPredictor()
sentiment_analyzer = SentimentAnalyzer()
llm_analyzer = LLMAnalyzer()


class MatchPredictionRequest(BaseModel):
    player_a_id: int
    player_b_id: int
    player_a_name: str = "Player A"
    player_b_name: str = "Player B"
    surface: str = "hard"


@router.post("/match")
async def predict_match(request: MatchPredictionRequest):
    """Get comprehensive match prediction with AI analysis."""
    # Placeholder stats - will be fetched from database/API
    player_a_stats = {
        "name": request.player_a_name,
        "form_score": 65,
        "aces_per_match": 8.5,
        "double_faults_per_match": 2.1,
        "serve_win_pct": 72,
        "return_win_pct": 35
    }
    
    player_b_stats = {
        "name": request.player_b_name,
        "form_score": 55,
        "aces_per_match": 6.2,
        "double_faults_per_match": 3.0,
        "serve_win_pct": 68,
        "return_win_pct": 32
    }
    
    head_to_head = []
    
    # Get predictions
    match_result = predictor.predict_match(
        player_a_stats=player_a_stats,
        player_b_stats=player_b_stats,
        surface=request.surface,
        head_to_head=head_to_head
    )
    
    total_games = predictor.predict_total_games(player_a_stats, player_b_stats)
    first_ace = predictor.predict_first_ace(player_a_stats, player_b_stats)
    
    # Get sentiment analysis
    sentiment_a = await sentiment_analyzer.get_overall_sentiment(request.player_a_name)
    sentiment_b = await sentiment_analyzer.get_overall_sentiment(request.player_b_name)
    
    # Get LLM analysis
    ai_analysis = await llm_analyzer.analyze_match(
        player_a=player_a_stats,
        player_b=player_b_stats,
        head_to_head=head_to_head,
        sentiment_a=sentiment_a,
        sentiment_b=sentiment_b
    )
    
    prediction_summary = await llm_analyzer.generate_prediction_summary(
        prediction=match_result,
        analysis=ai_analysis
    )
    
    return {
        "match_winner": match_result,
        "total_games": total_games,
        "first_ace": first_ace,
        "sentiment": {
            "player_a": sentiment_a,
            "player_b": sentiment_b
        },
        "ai_analysis": prediction_summary
    }