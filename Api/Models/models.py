from pydantic import BaseModel
from enum import Enum
from typing import Any


class ThirdLeagueStandings(BaseModel):
    standings: list[dict[str, Any]]


class TeraPlayers(BaseModel):
    players_data: list[dict[str, Any]]


class TeraMatchData(BaseModel):
    TeamHome: str
    TeamAway: str
    League: str
    DateTime: str
    Score: str | None
    Stats: list[dict[str, Any]] | None
    StadiumId: str | None

class TeraMatch(BaseModel):
   matchStats: list[TeraMatchData]
    
class Position(str, Enum):
    goalkeepers = "goalkeepers"
    goalkeeper = "goalkeeper"
    defenders = "defenders"
    defender = "defender"
    midfielders = "midfielders"
    midfielder = "midfielder"
    forwards = "forwards"
    forward = "forward"