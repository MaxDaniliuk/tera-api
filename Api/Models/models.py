from pydantic import BaseModel
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
    Stats: list[dict[str, Any]] | None
    StadiumId: str | None

class TeraMatch(BaseModel):
   matchStats: list[TeraMatchData]
    