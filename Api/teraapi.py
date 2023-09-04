from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Any
from dotenv import load_dotenv
load_dotenv()
import os
#import MySQLdb
import mysql.connector

def create_db_connection():
    connection = mysql.connector.connect(
    host= os.getenv("DB_HOST"),
    user=os.getenv("DB_USERNAME"),
    passwd= os.getenv("DB_PASSWORD"),
    db= os.getenv("DB_NAME"),
    autocommit = True,
    ssl_verify_identity = True,  # Enable SSL identity verification
    ssl_ca = "/etc/ssl/cert.pem"
    )
    return connection

class CustomData(BaseModel):
    standings: list[dict[str, Any]]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Receive"}

@app.post("/", status_code=201)
async def process_posted_data(data: CustomData):
    structred_data = data.standings
    return {"Post has been successful!"}
