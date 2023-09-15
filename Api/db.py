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

    def execute_third_league_standings_query(self, cursor, query, data):
         
        row_counter = 0
        for dict_row in data: 
            row_counter += 1
            row_values = tuple(dict_row.values())
            if query.startswith("INSERT"):
                cursor.execute(query, row_values)
                print(f"Row {row_counter} has been inserted")
            if query.startswith("UPDATE"):
                id_column = dict_row['Komanda']
                params = (*row_values, id_column)
                cursor.execute(query, params)
                print(f"Row {row_counter} has been updated")
            
            