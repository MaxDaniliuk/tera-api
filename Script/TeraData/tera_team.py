import requests
from bs4 import BeautifulSoup
from match_processor import MatchProcessor



class TeraTeam:
    
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
            headings = ['FullName', 'DateOfBirth', 'Position', 'Goals', 'Assists', 'GC', 'RK']
            rows = []
            
            '''for th_element in target_table.find_all('th')[1:]:
                # Do something with each <tr> element here.
                headings.append(th_element.text)'''
            
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

       
    def get_match_data(self):
        soup = self.target_block
        target_table = soup.find('table', class_='standings all-matches')
        match_details_list = []
        match_statistics_list = []
        if target_table:
            for target_td_tag in target_table.find_all('td', class_="tc"):
                for a_tag in target_td_tag.find_all('a', href=True): 
                    match_link = a_tag['href']
                    if match_link:
                        #Pass a link to the instances so the class could work with individual links
                        #match_links.append(match_link)
                        #match_data = MatchProcessor(match_link)
                        #Invoke two methods responsible for data engineering 
                        pass

                        

                    else:
                        raise Exception("Match link has not been found")
            
        return 



        
            
'''This block is inside [1:] tr blocks. Or simply find all td block containing class tc and href
<td class="tc">
<a href="http://www.vilniausfutbolas.lt/varzybos/Sirvintos-VGTU-Vilkai-FK-Tera/26714" class="score lost">2-1</a>
</td>
'''
            
            
   

        
obj = TeraTeam('http://www.vilniausfutbolas.lt/komanda/FK-Tera/210/20/30')

print(obj.get_match_data())