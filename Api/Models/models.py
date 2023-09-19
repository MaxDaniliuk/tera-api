from pydantic import BaseModel
from typing import Optional ,Any
from fastapi import HTTPException
from db import TeraDBManager


class StandingsData(BaseModel):
    standings: list[dict[str, Any]]

class TeamData(BaseModel):
    team: list[dict[str, Any]]



#Create a DB structure where logo is optional, and ID... 



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

class DBProcessor:

    def __init__(self):
        self.db_connection_manager = TeraDBManager()

    def process_data(self, data, query_function, query, table_name):
        db_connection = self.db_connection_manager.create_db_connection()
        cursor = db_connection.cursor()

        try:
            
            query_function(cursor, query, data, table_name)
            db_connection.commit()

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            cursor.close()
            db_connection.close()