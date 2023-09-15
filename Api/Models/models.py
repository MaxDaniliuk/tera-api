from pydantic import BaseModel
from typing import Optional ,Any


class CustomData(BaseModel):
    standings: list[dict[str, Any]]

#Create a DB structure where logo is optional, and ID... 
class Player(BaseModel):
    pass


class Team(BaseModel):
    Komanda: str
    Logo: Optional[str]


class ThirdLeagueStandings(BaseModel):
    Vieta: str 
    Komanda: str
    Logo: Optional[str]
    Rungtynes: str
    Pergales: str
    Lygiosios: str
    Pralaimejimai: str
    Imusta: str
    Praleista: str
    Skirtumas: str
    Taskai: str

