import requests
from bs4 import BeautifulSoup


class TeraPlayers:
    
    def __init__(self, web_url):
        self.web_url = web_url
        self.target_block = self.get_html_data()

    def get_html_data(self):
        response = requests.get(self.web_url)

        if response.status_code != 200:
            print('TeraData. Request failed with status code:', response.status_code)
            return

        #with open("data.html", "w", encoding="utf-8") as f:
        #    f.write(response.text)

        soup = BeautifulSoup(response.content, 'html.parser')

        return soup
    
    def get_players_data(self):
        soup = self.target_block
        target_table = soup.find('table', class_='standings full-width all-matches')
        
        if target_table:
            headings = []
            rows = []
            
            for th_element in target_table.find_all('th')[1:]:
                # Do something with each <tr> element here.
                headings.append(th_element.text)
            
            for tr_block in target_table.find_all('tr')[1:]:
                individual_row = []
                for td_element in tr_block.find_all('td')[1:]:
                    td_element = td_element.get_text(strip=True)
                    individual_row.append(td_element)
                rows.append(individual_row)
            
            if len(headings) == 0 or len(rows) == 0:
                return f"Players names and performance data collection has failed"
            
            team_data = [] 
            for row in rows: 
                combined = dict(zip(headings, row))
                team_data.append(combined)
            
            #json_data = json.dumps(my_lst, ensure_ascii=False, indent=4)
            return team_data

    #Gets link to a match    
    def get_match_link(self):
        soup = self.target_block
        #target_div = soup.find('div', id='rungtynes')
        target_table = soup.find('table', class_='standings all-matches')

        if target_table:
            headings = []
            rows = []

            for th_element in target_table.find_all('th'):
                headings.append(th_element.text)
            
            
            for tr_block in target_table.find_all('tr')[1:]:
                individual_row = []
                match_list = []
                td_elements = tr_block.find_all('td')
                #Perhaps you may consider adding a dictionary to a row
                for td_element in td_elements:
                    match_outcome = {}
                    td_class = td_element.get('class')
                    if td_class:
                        if 'tr' in td_class:
                            match_list.append(td_element.get_text(strip=True))
                        if 'tc' in td_class:
                            
                            if td_element.find(class_='score lost'):
                                match_outcome['Lost'] = td_element.get_text(strip=True)
                                match_list.append(match_outcome)
                            elif td_element.find(class_='score won'):
                                match_outcome['Won'] = td_element.get_text(strip=True)
                                match_list.append(match_outcome)
                            elif td_element.find(class_='score draw'):
                                match_outcome['Draw'] = td_element.get_text(strip=True)
                                match_list.append(match_outcome)
                            else: 
                                match_outcome['TBA'] = td_element.get_text(strip=True)
                                match_list.append(match_outcome)

                        if 'tl' in td_class:
                            match_list.append(td_element.get_text(strip=True))
                    else: 
                        td_element = td_element.get_text(strip=True)
                        individual_row.append(td_element)
                individual_row.append(match_list)
                rows.append(individual_row)
            
            match_data = [] 
            for row in rows: 
                combined = dict(zip(headings, row))
                match_data.append(combined)
            
            #json_data = json.dumps(my_lst, ensure_ascii=False, indent=4)
            return match_data
    
    def get_match_results(self, data_list):
        pass

        
obj = TeraPlayers('http://www.vilniausfutbolas.lt/komanda/FK-Tera/210/20/30')

#print(obj.get_players_data())