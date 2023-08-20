import dotenv
import os
import requests
from bs4 import BeautifulSoup 


dotenv.load_dotenv()
FOOTBALL_WEBSITE_URL= os.environ.get("FOOTBALL_WEBSITE_URL")

class DataExtractor:
    def __init__(self, web_url):
        self.web_url = web_url
        self.standings_table = self.get_table()

    def get_target_url(self):
        response_html = requests.get(self.web_url)

        if response_html.status_code != 200:
            print('Request failed with status code:', response_html.status_code)
            return
        
        soup = BeautifulSoup(response_html.content, 'html.parser')
        for link in soup.select('a[href*="turnyrine-lentel"]'):        
            return link['href']
        
    def get_table(self):
        target_url = self.get_target_url()
        if target_url is None:
            return
        response_html = requests.get(target_url)
        if response_html.status_code != 200:
            print('Final request failed with status code:', response_html.status_code)
            return
        soup = BeautifulSoup(response_html.content, 'html.parser')
        standings_table = soup.find('table', class_='standings')
        
        if standings_table:
            return standings_table
        else:
            raise Exception("Table has not been found by class 'standings': Table does not exist on on that web-page" )
    