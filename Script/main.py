from imagesdata import ImagesData
from dataextractor import DataExtractor
from standingsdata import StandingsData
import os
import dotenv
import requests


dotenv.load_dotenv()
FOOTBALL_WEBSITE_URL= os.environ.get("FOOTBALL_WEBSITE_URL")

def main(): 
    extracted_table = DataExtractor('http://www.vilniausfutbolas.lt/lyga/III-Lyga/20')
    standings_table = extracted_table.get_table()

    standings_data = StandingsData(standings_table)
    #print(standings_data.get_data())
    data = {'standings': standings_data.get_data()}
    #print(data)
    
    #images_data = ImagesData(standings_table)
    #images_data.save_images()

    response = requests.post('http://127.0.0.1:8000/data', json=data)
    if response.status_code == 201:
        print('Data successfully posted to the API.')
    else:
        print('Failed to post data:', response.status_code)
        print(response.json())


if __name__ == "__main__":
    main()
