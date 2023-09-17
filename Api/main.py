from fastapi import FastAPI, HTTPException
from Queries.sql_queries import StandingsSQLQueries
from db import TeraDBManager
from Models.models import CustomData


app = FastAPI()


@app.get("/test")
async def root():
    return {"message": "Get's working"}

@app.post("/db/insert/data", status_code=201)
async def process_posted_data(data: CustomData):
    structred_data = data.standings
    db_manager = TeraDBManager()
    db_conection = db_manager.create_db_connection()
    cursor = db_conection.cursor()
    insert_query = StandingsSQLQueries.INSERT_STANDINGS_DATA

    try:
    
        db_manager.execute_third_league_standings_query(cursor,insert_query, structred_data)
        db_conection.commit()
        print("Data successfully posted to the DB")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db_conection.close()
        