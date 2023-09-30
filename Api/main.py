from fastapi import FastAPI
from Queries.sql_queries import StandingsSQLQueries, TeraTeamSQLQueries, TeraMatchSQLQueries
from Schema.schema import IdContainer
from db import DBProcessor
from Models.models import ThirdLeagueStandings, TeraPlayers, TeraMatch
#from . import models, schemas


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

    operation_output = db_processor.process_data(
        structred_data, 
        db_processor.db_connection_manager.post_data, 
        insert_query, 
        "ThirdLeagueStandings"
        )
    
    if operation_output is not None and isinstance(operation_output, dict):
    
        teams_ids = operation_output

        return {"Message": "Table ThirdLeagueStandings filled successfully", "TeamsIds": teams_ids}
    else: 
        teams_ids = None
        return 
    
@app.put("/db/thirdleaguestandings", status_code=201)
async def process_posted_data(data: ThirdLeagueStandings):
    structred_data = data.standings
    update_query = StandingsSQLQueries.UPDATE_STANDINGS_DATA
    teams_ids = IdContainer.TEAM_IDS
    
    db_processor.process_data(
        structred_data, 
        db_processor.db_connection_manager.update_data, 
        update_query,
        "ThirdLeagueStandings",
        teams_ids 
        )


@app.put("/db/put/teraplayers", status_code=201)
async def update_players(players_data: TeraPlayers):
    players_stats = players_data.players_data
    update_query = TeraTeamSQLQueries.UPDATE_PLAYERS_DATA
    player_id = IdContainer.PLAYERS_IDS

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


@app.post("/db/post/teramatch", status_code=201)
async def process_tera_matches(tera_matches: TeraMatch):
    match_details = tera_matches.matchStats
    insert_query_matches = TeraMatchSQLQueries.INSERT_TERA_MATCH
    
    match_stats_collection = []
    for match_data in match_details:
        processed_data = []
        processed_data.append(match_data.TeamHome)
        processed_data.append(match_data.TeamAway)
        processed_data.append(match_data.League)
        processed_data.append(match_data.DateTime)
        processed_data.append(match_data.Stats)
        processed_data.append(match_data.StadiumId)
        match_stats_collection.append(processed_data)
    
    operation_output = db_processor.process_data(
        match_stats_collection, 
        db_processor.db_connection_manager.post_data, 
        insert_query_matches, 
        "TeraMatch"
        )  

    if operation_output is not None and isinstance(operation_output, dict):
    
        matches_ids = operation_output

        return {"Message": "Table TeraMatch posted successfully", "MatchIds": matches_ids}
    else: 
        matches_ids = None
        return

@app.put("/db/put/teramatch", status_code=201)
async def update_tera_match(tera_matches: TeraMatch):
    match_details = tera_matches.matchStats
    #Change to update query 
    update_query_matches = TeraMatchSQLQueries.UPDATE_TERA_MATCH
    tera_match_ids = IdContainer.Match_IDs
    
    match_stats_collection = []
    for match_data in match_details:
        processed_data = []
        processed_data.append(match_data.TeamHome)
        processed_data.append(match_data.TeamAway)
        processed_data.append(match_data.League)
        processed_data.append(match_data.DateTime)
        processed_data.append(match_data.Stats)
        processed_data.append(match_data.StadiumId)
        match_stats_collection.append(processed_data)
    
    db_processor.process_data(
        match_stats_collection, 
        db_processor.db_connection_manager.update_data, 
        update_query_matches, 
        "TeraMatch",
        tera_match_ids
        )  
    

@app.get("/data/{table_name}")
async def get_data(table_name: str):
    pass