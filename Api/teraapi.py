from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Any
from dotenv import load_dotenv
load_dotenv()
import os
#import MySQLdb 
import mysql.connector 


app = FastAPI()


def create_db_connection():
    connection = mysql.connector.connect(
    host= os.getenv("DB_HOST"),
    user=os.getenv("DB_USERNAME"),
    passwd= os.getenv("DB_PASSWORD"),
    db= os.getenv("DB_NAME"),
    autocommit = True,
    ssl_verify_identity = True,  # Enable SSL identity verification
    ssl_ca = "/etc/ssl/cert.pem",
    charset='utf8mb4',  # Set the character set to utf8mb4
    collation='utf8mb4_unicode_ci'
    )
    return connection




def create_standings_table():
    try:
        connection = create_db_connection()
        cursor = connection.cursor()

        table_name = "Standings_table"

        

        # Check if the table exists, and create it if it doesn't
        if not table_exists(cursor, table_name):

            column_definitions = [
            "id INT AUTO_INCREMENT PRIMARY KEY",
            "column1 VARCHAR(2)",
            "column2 VARCHAR(25)",
            "column3 VARCHAR(25)",
            "column4 VARCHAR(2)",
            "column5 VARCHAR(2)",
            "column6 VARCHAR(2)",
            "column7 VARCHAR(2)",
            "column8 VARCHAR(3)",
            "column9 VARCHAR(3)",
            "column10 VARCHAR(4)",
            "column11 VARCHAR(3)"
            ]

            create_table_sql = f"CREATE TABLE {table_name} ({', '.join(column_definitions)})"
            cursor.execute(create_table_sql)
            print(f"Table {table_name} is Created in the Database")
        else:
            print(f"Table {table_name} already exists")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        connection.close()


#Check if the table exists in the database
def table_exists(cursor, table_name):
    try:
        cursor.execute("SHOW TABLES LIKE %s", (table_name,))
        return cursor.fetchone() is not None
    except Exception as e:
        # Handle any exceptions related to database access
        print(f"Error checking table existence: {str(e)}")
        return False
    
class CustomData(BaseModel):
    standings: list[dict[str, Any]]


#Change to get data from the DB
@app.get("/")
async def root():
    return {"message": "Working"}

@app.post("/", status_code=201)
async def process_posted_data(data: CustomData):
    structred_data = data.standings
 
    try:
        #Create the table if it doesn't exist
        create_standings_table()

        connection = create_db_connection()
        cursor = connection.cursor()

        row_count = 0
        for dict_of_data in structred_data:
            
            insert_query = "INSERT INTO Standings_table (Vieta, Komanda, Logo, Rungtynės, Pergalės, Lygiosios, Pralaimėjimai, Įmušta, Praleista, Skirtumas, Taškai) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            row_values = tuple(dict_of_data.values())
            cursor.execute(insert_query, row_values)
            row_count += 1
            print(f"row {row_count} has been added")
            
        connection.commit()

        return {"message": "Data has been inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        connection.close()
