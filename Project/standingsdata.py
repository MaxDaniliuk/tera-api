#import dotenv
#import os
#import requests
#from bs4 import BeautifulSoup 
import json
from dataextractor import DataExtractor

class StandingsTable:
    def __init__(self, web_url):
        self.web_url = web_url
        self.standings_table = DataExtractor(self.web_url).get_table()

    def format_data(self):
        
        # if None: wolud return in  
        # if standings_table:
        #     return standings_table
        # else: 
        #     print("Table's location has changed")
        #     return"
        #
        # So code should be written as an Exeption
        # like:
        # raise Exception("Table has not been found by class 'standings': Table does not exist on on that web-page" )
        # 
        # if standings_table is None: 
        #     return      
        # also standings_table says more about content than target_table, you can use words describing content more if it is helpful

        headings = []
        rows = []
        for th_elements in self.standings_table.find_all('th'):
            headings.append(th_elements.text)
        for tr_blocks in self.standings_table.find_all('tr')[1:]:
            seperated_rows = []
            for td_blocks in tr_blocks.find_all('td'):
                seperated_rows.append(td_blocks.text.strip())
                a_tag = td_blocks.find('a')
                if a_tag:
                    img_tag = a_tag.find('img')
                    if img_tag and img_tag.has_attr('src'):
                        img_name = a_tag.get_text(strip=True).lower().replace(' ', '-')
                        seperated_rows.append(img_name.strip())
                    else: 
                        seperated_rows.append(None)      
            rows.append(seperated_rows)
        headings.insert(headings.index('Komanda') + 1, 'Logo')
        return headings, rows
    
    def get_data(self):
        try: 
            headings, rows = self.format_data()
            my_list = [] # is my_list suitable name? maybe
            for row in rows: 
                combined = dict(zip(headings, row))
                my_list.append(combined)
            json_data = json.dumps(my_list, ensure_ascii=False, indent=4)
            return json_data
        except:
            return 

    def save_data(self):
        try:
            json_string = json.loads(self.get_data())
            with open('footballdata.json', 'w', encoding='utf-8') as json_file:
                json.dump(json_string, json_file, ensure_ascii=False, indent=4)
        except:
            return print('Json string cannot be serialized. Go to the link and check whether the table is there')
            

my_obj = StandingsTable("http://www.vilniausfutbolas.lt/lyga/III-Lyga/20")

print(my_obj.get_data())
#my_obj.save_data()