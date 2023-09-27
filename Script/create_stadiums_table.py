
from dotenv import load_dotenv
load_dotenv()
import os
from mysql.connector import connect, Error

stadiums = ['Širvintų stadionas', 'BFA arena', 'Nemenčinė', 
            'Kariškių stadionas', 'Senvagės stadionas', 
            'Pilaitės stadionas', None, 'Trakų naujas']

stadiums_data = [
    {'StadiumId': 'c4f769b4-fc8', 'StadiumName': 'Širvintų stadionas', 'Lat': float(55.03827114402019), 'Long': float(24.960980954892985)}, 
    {'StadiumId': '8a0360fb-21d', 'StadiumName': 'BFA arena', 'Lat': float(54.6944144193766), 'Long': float(25.209020567036593)}, 
    {'StadiumId': '9a6c5ffb-780', 'StadiumName': 'Nemenčinė', 'Lat': float(54.841837179704406), 'Long': float(25.47772244659796)},
    {'StadiumId': 'ace9be40-309', 'StadiumName': 'Kariškių stadionas', 'Lat': float(54.7595831280542), 'Long': float(25.263255354074374)},
    {'StadiumId': 'ad814714-28c', 'StadiumName': 'Senvagės stadionas', 'Lat': float(54.71194295496112), 'Long': float(25.280352064666687)},
    {'StadiumId': 'edbbfae3-496', 'StadiumName': 'Pilaitės stadionas', 'Lat': float(54.702563502123674), 'Long': float(25.181203172945107)},
    {'StadiumId': '7a641419-67c', 'StadiumName': 'Trakų naujas', 'Lat': float(54.64002966254929), 'Long': float(24.937232050323594)}
    ]
STADIUM_IDS = {}

for stadium_id in stadiums_data:
    STADIUM_IDS[stadium_id['StadiumName']] = stadium_id['StadiumId']

print(STADIUM_IDS)

def main():

    def create_db_connection():
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
            
    connection = create_db_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO Stadiums (StadiumId, StadiumName, Lat, Long) VALUES (%s, %s, %s, %s)"


    for stadium_id in stadiums_data:
        
        values = (stadium_id['StadiumId'], stadium_id['StadiumName'], stadium_id['Lat'], stadium_id['Long'])

        cursor.execute(insert_query, values)

        connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
     main()