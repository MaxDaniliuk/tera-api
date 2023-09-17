from imagesdata import ImagesData
from dataextractor import DataExtractor
from standingsdata import StandingsData
import requests
import json


#dotenv.load_dotenv()
#FOOTBALL_WEBSITE_URL= os.environ.get("FOOTBALL_WEBSITE_URL")

def main(): 
    extracted_table = DataExtractor('http://www.vilniausfutbolas.lt/lyga/III-Lyga/20')
    standings_table = extracted_table.get_table()

    standings_data = StandingsData(standings_table)
    #print(standings_data.get_data())

    data = {'standings': standings_data.get_data()}
    

    #images_data = ImagesData(standings_table)
    #images_data.save_images()

    #Move to posting data to the api. 

    response = requests.post('http://127.0.0.1:8000/db/insert/data', json=data)
    if response.status_code == 201:
        print('Data successfully posted to the API.')
    else:
        print('Failed to post data:', response.status_code)
        print(response.content)
        print(response.json())


if __name__ == "__main__":
    main()
