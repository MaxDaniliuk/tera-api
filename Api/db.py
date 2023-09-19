from dotenv import load_dotenv
load_dotenv()
import os
from mysql.connector import connect, Error


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
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        table_row_count = cursor.fetchone()[0]
        if table_row_count > 0:
            print(f"Data has already been inserted into the {table_name} table")
            return
        else:
            row_counter = 0
            for dict_row in data:
                 
                row_counter += 1
                row_values = tuple(dict_row.values())
                cursor.execute(insert_query, row_values)
                print(f"Row {row_counter} has been inserted into {table_name}")
                
        

    
    def update_data(self, cursor, query, data, table_name):
        
        if table_name == 'TeraPlayers':
            player_id = 1

        row_counter = 0
        for dict_row in data: 
            row_counter += 1
            row_values = tuple(dict_row.values())
            if not query.startswith("UPDATE"):
                print('Wrong SQL query')
                return
            if table_name == 'TeraPlayers':
                params = (*row_values, player_id)
                player_id += 1
            if table_name == 'ThirdLeagueStandings':
                id_column = dict_row['Komanda']
                params = (*row_values, id_column)

            cursor.execute(query, params)
            print(f"Row {row_counter} has been updated")
    

    
            
            