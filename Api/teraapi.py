import dotenv
import MySQLdb
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Any


class CustomData(BaseModel):
    standings: list[dict[str, Any]]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Receive"}

@app.post("/", status_code=201)
async def process_posted_data(data: CustomData):
    structred_data = data.standings
    return {"message": "/data, hey post response"}
