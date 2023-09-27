from dotenv import load_dotenv
load_dotenv()
import os
from mysql.connector import connect, Error
from fastapi import HTTPException
import uuid
import json



class TeraDBManager:

    def create_db_connection(self):
        try:
            connection = connect(
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
        except Error as e:
            print('Connection to DB failed.', e)
            return None
        


#This file contains code to connect to the DB and maybe some other related stuff. 
    def post_data(self, cursor, insert_query, data, table_name):
        ids = {}

        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        table_row_count = cursor.fetchone()[0]

        if table_row_count > 0:
            print(f"Data has already been inserted into the {table_name} table")
            return
        else:
            row_counter = 1
            for index, rows in enumerate(data, start=1):
                
                if table_name == 'TeraPlayers':
                    player_id = str(uuid.uuid4())
                    row_values = (player_id, *tuple(rows.values()), "FK Tera")
                    ids[rows['FullName']] = player_id

                if table_name == 'ThirdLeagueStandings':
                    team_id = str(uuid.uuid4())[:8]   
                    row_values = (team_id ,*tuple(rows.values()))
                    ids[rows['Komanda']] = team_id
                
                if table_name == 'TeraMatch':
                    #For this table, data is a list
                    
                    match_id = str(uuid.uuid4())[:16]
                    static_match_details = tuple(rows)[:len(rows)-2]
                    if isinstance(rows[4], list):
                        stats = json.dumps({'Stats': rows[4]})
                    else:
                        stats = None
                    stadium_id = tuple(rows)[len(rows)-1]
                    row_values = (match_id, *static_match_details, stats, stadium_id)
                    ids[index] = match_id
                cursor.execute(insert_query, row_values)
                print(f"Row {row_counter} has been inserted into {table_name}")
                row_counter += 1
            return ids
    
    
    def update_data(self, cursor, update_query, data, table_name, unique_ids):
        
        row_counter = 1
        for rows in data: 
            
            
            if not update_query.startswith("UPDATE"):
                print('Wrong SQL query')
                return
                
            if table_name == 'TeraPlayers':
                id = unique_ids[rows['FullName']]
                row_values = tuple(rows.values())
                
            if table_name == 'ThirdLeagueStandings':
                id = unique_ids[rows['Komanda']]
                row_values = tuple(rows.values())
            
            if table_name == 'TeraMatch':
                id = unique_ids[str(row_counter)]
                if isinstance(rows[4], list):
                    stats = json.dumps({'Stats': rows[4]})
                else:
                    stats = None
                rows[4] = stats    
                row_values = tuple(rows)

            params = (*row_values, id)
            cursor.execute(update_query, params)
            print(f"Row {row_counter} has been updated")
            row_counter += 1
    


class DBProcessor:

    def __init__(self):
        self.db_connection_manager = TeraDBManager()

    def process_data(self, data, query_function, query, table_name, id=None):
        db_connection = self.db_connection_manager.create_db_connection()
        cursor = db_connection.cursor()
        
        try:
            if id is None:
                output = query_function(cursor, query, data, table_name)
            else:
                output = query_function(cursor, query, data, table_name, id)
            
            db_connection.commit()
            return output
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            cursor.close()
            db_connection.close()
            
