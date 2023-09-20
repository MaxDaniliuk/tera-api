from fastapi import FastAPI
from Queries.sql_queries import StandingsSQLQueries, TeraTeamSQLQueries
from Schema.schema import PLAYERS_IDS
from db import DBProcessor
from Models.models import ThirdLeagueStandings, TeraPlayers



app = FastAPI()

db_processor = DBProcessor()

@app.get("/test")
async def root():
    return {"message": "Get's working"}

#ROUTES... 

@app.post("/db/thirdleaguestandings", status_code=201)
async def process_posted_data(data: ThirdLeagueStandings):
    structred_data = data.standings
    insert_query = StandingsSQLQueries.INSERT_STANDINGS_DATA

    db_processor.process_data(
        structred_data, 
        db_processor.db_connection_manager.post_data, 
        insert_query, 
        "ThirdLeagueStandings"
        )
    

@app.put("/db/thirdleaguestandings", status_code=201)
async def process_posted_data(data: ThirdLeagueStandings):
    structred_data = data.standings
    update_query = StandingsSQLQueries.UPDATE_STANDINGS_DATA
    
    db_processor.process_data(
        structred_data, 
        db_processor.db_connection_manager.update_data, 
        update_query,
        "ThirdLeagueStandings" 
        )




@app.put("/db/put/teraplayers", status_code=201)
async def update_players(players_data: TeraPlayers):
    players_stats = players_data.players_data
    update_query = TeraTeamSQLQueries.UPDATE_PLAYERS_DATA
    player_id = PLAYERS_IDS

    db_processor.process_data(
        players_stats, 
        db_processor.db_connection_manager.update_data, 
        update_query,
        "TeraPlayers",
        player_id 
        )

@app.post("/db/post/teraplayers", status_code=201)
async def process_players(players_data: TeraPlayers):
    players_stats = players_data.players_data
    insert_query =  TeraTeamSQLQueries.INSERT_PLAYERS_DATA

    operation_output = db_processor.process_data(
        players_stats, 
        db_processor.db_connection_manager.post_data, 
        insert_query, 
        "TeraPlayers"
        )
    
    if operation_output is not None and isinstance(operation_output, dict):
    
        players_ids = operation_output

        return {"Message": "Table TeraPlayers filled successfully", "PlayersIds": players_ids}
    else: 
        players_ids = None
        return 

    
    

        