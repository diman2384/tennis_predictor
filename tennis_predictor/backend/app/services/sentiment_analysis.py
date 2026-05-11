from typing import Any


class SentimentAnalyzer:
    """Sentiment analysis service for tennis players."""
    
    async def analyze_social_media(self, player_name: str) -> dict[str, Any]:
        """Analyze player's social media sentiment."""
        # TODO: Integrate with Twitter/Instagram API
        # For now, return mock data
        return {
            "score": 0.65,  # -1 to 1
            "positive_count": 12,
            "negative_count": 3,
            "neutral_count": 5,
            "recent_posts": [
                {"text": "Great performance today!", "sentiment": "positive"},
                {"text": "Looking forward to next match", "sentiment": "positive"},
            ]
        }
    
    async def analyze_news(self, player_name: str) -> dict[str, Any]:
        """Analyze news articles about player."""
        # TODO: Integrate with NewsAPI
        return {
            "score": 0.45,  # -1 to 1
            "positive_count": 8,
            "negative_count": 2,
            "neutral_count": 10,
            "articles": [
                {"title": "Player wins tournament", "sentiment": "positive"},
                {"title": "Minor injury concern", "sentiment": "negative"},
            ]
        }
    
    async def get_overall_sentiment(self, player_name: str) -> dict[str, Any]:
        """Get combined sentiment score."""
        social = await self.analyze_social_media(player_name)
        news = await self.analyze_news(player_name)
        
        overall = (social["score"] * 0.6 + news["score"] * 0.4)
        
        if overall > 0.3:
            label = "positive"
        elif overall < -0.3:
            label = "negative"
        else:
            label = "neutral"
        
        return {
            "overall_score": round(overall, 3),
            "social_score": social["score"],
            "news_score": news["score"],
            "label": label,
            "positive_count": social["positive_count"] + news["positive_count"],
            "negative_count": social["negative_count"] + news["negative_count"],
            "neutral_count": social["neutral_count"] + news["neutral_count"],
        }