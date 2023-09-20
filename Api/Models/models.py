from pydantic import BaseModel
from typing import Any


class ThirdLeagueStandings(BaseModel):
    standings: list[dict[str, Any]]


class TeraPlayers(BaseModel):
    players_data: list[dict[str, Any]]