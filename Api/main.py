from fastapi import FastAPI, HTTPException
from Queries.sql_queries import StandingsSQLQueries
from Queries.sql_queries import TeraTeamSQLQueries
from db import TeraDBManager
from Models.models import StandingsData, TeamData, DBProcessor


app = FastAPI()

db_processor = DBProcessor()

@app.get("/test")
async def root():
    return {"message": "Get's working"}

#ROUTES... 

@app.post("/db/standingsdata", status_code=201)
async def process_posted_data(data: StandingsData):
    structred_data = data.standings
    insert_query = StandingsSQLQueries.INSERT_STANDINGS_DATA

    db_processor.process_data(
        structred_data, 
        db_processor.db_connection_manager.post_data, 
        insert_query, 
        "ThirdLeagueStandings"
        )
    

@app.put("/db/standingsdata", status_code=201)
async def process_posted_data(data: StandingsData):
    structred_data = data.standings
    update_query = StandingsSQLQueries.UPDATE_STANDINGS_DATA
    
    db_processor.process_data(
        structred_data, 
        db_processor.db_connection_manager.update_data, 
        update_query,
        "ThirdLeagueStandings" 
        )


@app.post("/db/teamdata", status_code=201)
async def process_posted_data(data: TeamData):
    structred_data = data.team
    insert_query = TeraTeamSQLQueries.INSERT_TEAM_DATA

    db_processor.process_data(
        structred_data, 
        db_processor.db_connection_manager.post_data, 
        insert_query, 
        "TeraPlayers"
    )


@app.put("/db/teamdata", status_code=201)
async def process_posted_data(data: TeamData):
    structred_data = data.team
    update_query = TeraTeamSQLQueries.UPDATE_TEAM_DATA

    db_processor.process_data(
        structred_data, 
        db_processor.db_connection_manager.update_data, 
        update_query,
        "TeraPlayers" 
        )


        