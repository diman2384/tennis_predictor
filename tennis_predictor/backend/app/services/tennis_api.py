from abc import ABC, abstractmethod
from typing import Any


class TennisAPIClient(ABC):
    """Abstract base class for Tennis API clients."""
    
    @abstractmethod
    async def get_player(self, player_id: int) -> dict[str, Any]:
        """Get player profile."""
        pass
    
    @abstractmethod
    async def get_player_matches(self, player_id: int, limit: int = 100) -> list[dict[str, Any]]:
        """Get player match history."""
        pass
    
    @abstractmethod
    async def get_upcoming_matches(self) -> list[dict[str, Any]]:
        """Get upcoming matches."""
        pass
    
    @abstractmethod
    async def get_head_to_head(self, player1_id: int, player2_id: int) -> list[dict[str, Any]]:
        """Get head-to-head record between two players."""
        pass