from typing import Any


class LLMAnalyzer:
    """LLM-based analysis service for tennis predictions."""
    
    async def analyze_match(
        self,
        player_a: dict[str, Any],
        player_b: dict[str, Any],
        head_to_head: list[dict],
        sentiment_a: dict[str, Any],
        sentiment_b: dict[str, Any]
    ) -> str:
        """Generate AI analysis of upcoming match."""
        # TODO: Integrate with OpenAI/Claude API
        # For now, return template-based analysis
        
        analysis_parts = []
        
        # Form analysis
        form_a = player_a.get("form_score", 50)
        form_b = player_b.get("form_score", 50)
        
        if form_a > form_b + 10:
            analysis_parts.append(f"{player_a.get('name', 'Player A')} в отличной форме с показателем {form_a}/100.")
        elif form_b > form_a + 10:
            analysis_parts.append(f"{player_b.get('name', 'Player B')} в отличной форме с показателем {form_b}/100.")
        else:
            analysis_parts.append("Оба игрока находятся в схожей форме.")
        
        # Sentiment analysis
        if sentiment_a.get("label") == "positive":
            analysis_parts.append("Настроение вокруг Player A положительное.")
        if sentiment_b.get("label") == "positive":
            analysis_parts.append("Настроение вокруг Player B положительное.")
        
        # Head-to-head
        if head_to_head:
            a_wins = sum(1 for m in head_to_head if m.get("winner") == "a")
            b_wins = len(head_to_head) - a_wins
            analysis_parts.append(f"Личные встречи: {a_wins}-{b_wins}.")
        
        return " ".join(analysis_parts)
    
    async def generate_prediction_summary(
        self,
        prediction: dict[str, Any],
        analysis: str
    ) -> str:
        """Generate a concise prediction summary."""
        prob_a = prediction.get("player_a_win_prob", 0.5) * 100
        confidence = prediction.get("confidence", 0.5) * 100
        
        return (
            f"📊 Предсказание:\n"
            f"• Вероятность победы Player A: {prob_a:.0f}%\n"
            f"• Уверенность: {confidence:.0f}%\n\n"
            f"🤖 Анализ:\n{analysis}"
        )