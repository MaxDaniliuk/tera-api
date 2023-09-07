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
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        passwd=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
        autocommit=True,
        charset='utf8mb4',  
        collation='utf8mb4_unicode_ci',  
        ssl_verify_identity=True,
        ssl_ca="/etc/ssl/cert.pem"
    )
    return connection


def create_standings_table():
    connection = create_db_connection()
    cursor = connection.cursor()

    try:
        table_name = "StandingsTable"
        column_definitions = [
            "id INT AUTO_INCREMENT PRIMARY KEY",
            "Vieta VARCHAR(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Komanda VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Logo VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Rungtynes VARCHAR(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Pergales VARCHAR(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Lygiosios VARCHAR(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Pralaimejimai VARCHAR(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Imusta VARCHAR(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Praleista VARCHAR(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Skirtumas VARCHAR(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Taskai VARCHAR(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            ]
        

        # Check if the table exists, and create it if it doesn't
        if not table_exists(cursor, table_name):

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

@app.put("/", status_code=201)
async def process_posted_data(data: CustomData):
    structred_data = data.standings
    
    try:
        #Create the table if it doesn't exist
        create_standings_table()

        connection = create_db_connection()
        cursor = connection.cursor()

        row_count = 0

        #Code block for insertin 
        '''for dict_of_data in structred_data:
            insert_query = "INSERT INTO StandingsTable (Vieta, Komanda, Logo, Rungtynes, Pergales, Lygiosios, Pralaimejimai, Imusta, Praleista, Skirtumas, Taskai) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            row_values = tuple( dict_of_data.values())
            cursor.execute(insert_query, row_values)
            row_count += 1
            print(f"row {row_count} has been added")'''
        
        update_query = """
            UPDATE StandingsTable
            SET Vieta = %s, Komanda = %s, Logo = %s, Rungtynes = %s, Pergales = %s,
                Lygiosios = %s, Pralaimejimai = %s, Imusta = %s, Praleista = %s,
                Skirtumas = %s, Taskai = %s
        """
        for dict_of_data in structred_data:
            row_values = tuple(dict_of_data.values())
            cursor.execute(update_query, row_values)
            row_count += 1
            print(f"row {row_count} has been updated")

        connection.commit()
        
        return {"message": "Data has been inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        connection.close()
