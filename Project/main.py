from imagesdata import ImagesData
from standingsdata import StandingsData
import os
import dotenv


dotenv.load_dotenv()
FOOTBALL_WEBSITE_URL= os.environ.get("FOOTBALL_WEBSITE_URL")

def main(): 
    pass

#POST to api and receive an output either as 'Success' or 'Failed"

if __name__ == "__main__":
    main()
