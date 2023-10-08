from dotenv import load_dotenv
load_dotenv()
import os
from mysql.connector import connect, Error
from fastapi import HTTPException
import uuid
import json
from Schema.schema import IdContainer
import datetime
from Queries.sql_queries import Stadiums, TeraTeamSQLQueries


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
                    row_values = (player_id, *tuple(rows.values()), "9530fd95")
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
                        stats = json.dumps({'Stats': rows[5]})
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
        if table_name == 'TeraPlayers':
            cursor.execute(f"SELECT FullName FROM {table_name}")
            names = cursor.fetchall()
            
        row_counter = 1
        for rows in data: 
            if not update_query.startswith("UPDATE"):
                print('Wrong SQL query')
                return
                
            if table_name == 'TeraPlayers':
                full_name = rows['FullName']
                player_present = next((name for name in names if name[0] == full_name), None)
                
                if player_present:
                    id = unique_ids[rows['FullName']]
                    row_values = tuple(rows.values())
                    
                else:
                    id = str(uuid.uuid4())
                    IdContainer.PLAYERS_IDS[rows['FullName']] = id
                    row_values = (id, *tuple(rows.values()), "9530fd95")
                    cursor.execute(TeraTeamSQLQueries.INSERT_PLAYERS_DATA, row_values)
                    print(f"New player {rows['FullName']} has been added")
                    row_counter += 1
                    continue
                
            if table_name == 'ThirdLeagueStandings':
                id = unique_ids[rows['Komanda']]
                row_values = tuple(rows.values())
            
            if table_name == 'TeraMatch':
                id = unique_ids[str(row_counter)]
                if isinstance(rows[5], list):
                    stats = json.dumps({'Stats': rows[5]})
                else:
                    stats = None
                rows[5] = stats    
                row_values = tuple(rows)

            params = (*row_values, id)
            cursor.execute(update_query, params)
            print(f"Row {row_counter} has been updated")
            row_counter += 1

    
    def get_third_league_standings(self, cursor, select_query):
        
        cursor.execute(select_query)
        retrieved_rows = cursor.fetchall()
        data_names = ['Place', 'Team', 'GamesPlayed', 'Won', 'Drawn', 'Lost', 'GoalsFor', 'GoalsAgainst', 'GoalDifference', 'Points']
        rows = []
        for row in retrieved_rows:
            values_list = list(row)
            processed_row = dict(zip(data_names, values_list))
            rows.append(processed_row)
        return rows
    
    
    def get_players_by_position(self, cursor, select_query, param):

        cursor.execute(select_query, param)
        retrieved_data = cursor.fetchall()
        data_names = ['FullName', 'DateOfBirth', 'Position', 'Goals', 'Assists', 'GC', 'RC']
        rows = [] 
        for row in retrieved_data:
            row = list(row)
            date_element  = row[1].split('[')[0].strip()
            date_obj = datetime.datetime.strptime(date_element, "%Y-%m-%d")
            row[1] = date_obj.strftime("%Y-%m-%d")
            processed_row = dict(zip(data_names, row))
            rows.append(processed_row)
        return rows

    
    def get_match(self, cursor, select_query, current_time, number=None):
        if number is None or number <= 0:
            number = 1
        params = (current_time, number)
        cursor.execute(select_query, params)
        retrieved_data = cursor.fetchall()
        
        formatted_data = []
        for row in retrieved_data:
            new_dict = {}
            
            for index, value in enumerate(row, start=1):
                if index == 1:
                    value_processor = MatchDataStringProcessor(value)
                    processed_value = value_processor.get_processed_value()
                    new_dict['TeamHome'] = processed_value
                    
                elif index == 2:
                    value_processor = MatchDataStringProcessor(value)
                    processed_value = value_processor.get_processed_value()
                    new_dict['TeamAway'] = processed_value
                    
                elif index == 3:
                    new_dict['League'] = value
                    
                elif index == 4:
                    new_dict['DateTime'] = value.strftime("%Y-%m-%d %H:%M")
                
                elif index == 5:
                    if value is None:
                        new_dict['Score'] = None
                    else:    
                        new_dict['Score'] = value

                elif index == 6:
                    if value is None:
                        new_dict['Stats'] = None
                    else:
                        list_of_values = json.loads(value)
                        match_events = []
                        for dict_element in list_of_values['Stats']:
                            stats = {}
                            value_processor = MatchDataStringProcessor(dict_element['TeamId'])
                            stats['Team'] = value_processor.get_processed_value()    
                            stats['Minute'] = dict_element['Minute']
                            stats['Event'] = dict_element['Event']
                            stats['PlayerName'] = dict_element['PlayerName']
                            if 'AssistedBy' in dict_element:
                                stats['AssistedBy'] = dict_element['AssistedBy']
                            match_events.append(stats)
                        new_dict['Stats'] = match_events
                elif index == 7:
                    if value is None:
                        new_dict['StadiumData'] = None
                    else:
                        param = (value,)
                        cursor.execute(Stadiums.SELECT_STADIUM, param)
                        stadium_data = cursor.fetchall()
                        stadium_dict = {}
                        for data in stadium_data:
                            stadium_dict['Stadium'] = data[0]
                            stadium_dict['Lat'] = data[1]
                            stadium_dict['Long'] = data[2]
                        new_dict['StadiumData'] = stadium_dict 
                    
            formatted_data.append(new_dict)
        return formatted_data


class MatchDataStringProcessor:

    def __init__(self, value):
        self.value = value

    def get_processed_value(self):
        value = self.value

        if isinstance(value, str): 
            if value in IdContainer.TEAM_IDS.values():
                for key, val in IdContainer.TEAM_IDS.items():
                    if val == value:
                        return key
            else: 
                raise{f"TeamId: {value} has not been identified"}
        

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
    
    def retrieve_data(self, query_function, select_query, *args):
        db_connection = self.db_connection_manager.create_db_connection()
        cursor = db_connection.cursor()

        try:
            output = query_function(cursor, select_query, *args)
            db_connection.commit()
            return output
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            cursor.close()
            db_connection.close()