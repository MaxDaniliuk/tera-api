import requests
from bs4 import BeautifulSoup as bs
import re
from Schemas.schemas import IdContainer



class MatchProcessor:
    
    def __init__(self, match_url):
        self.match_url = match_url

    def process_match_link(self):
        response = requests.get(self.match_url)

        if response.status_code != 200:
            print('Match URL is invalid. Request failed with status code:', response.status_code)
            return 
        soup = bs(response.content, 'html.parser')

        return soup
    
    def get_match_details(self):
        soup = self.process_match_link()
        match_details = {}
        match_info = soup.find('div', id='match-info')
        
        teams_list = match_info.find_all('h3')
        if teams_list:
            if teams_list[0].text not in IdContainer.TEAM_IDS.keys() or teams_list[1].text not in IdContainer.TEAM_IDS.keys():
                raise Exception("One team is not identified")
            match_details['TeamHome'] = IdContainer.TEAM_IDS[teams_list[0].text]
            match_details['TeamAway'] = IdContainer.TEAM_IDS[teams_list[1].text]
            
        match_p_tags = match_info.find_all('p')
        if match_p_tags:
            match_details['League'] = match_p_tags[0].text
            match_details['DateTime'] = match_p_tags[1].text

        stadium_section = match_info.find('div', class_='span4 no-space center-teams')
        if stadium_section:
            stadium_tag = stadium_section.find('a')
            if stadium_tag.text:
                stadium = stadium_tag.text
            else:
                stadium = None

        return match_details, stadium

    def get_match_stats(self):
        match_statistics = []
        soup = self.process_match_link()
        statistics_section = soup.find('div', attrs={"id": "tabwidget", "class": "top-margin tabwidget widget tab-container two"})
        goals_section = statistics_section.find('div', class_='goals')
        
        if goals_section:
            match_events = goals_section.find_all('div', class_='statistic-event row-fluid')
            
            for event in match_events:
                match_event = {}

                if event.find('p').text not in IdContainer.TEAM_IDS.keys():
                    raise Exception(f"{event.find('p').text} not identified")     
                match_event['TeamId'] = IdContainer.TEAM_IDS[event.find('p').text]
                
                match_event['Minute'] = event.find('div', class_='span2 minute').text
                a_tag = event.find_all('a')
                match_event['PlayerName'] = a_tag[0].text.strip()

                main_event = event.find('img')['src']
                match = re.search(r'/([^/]+)\.png', main_event)
                if match:
                    fragment = match.group(1)
                    match_event['Event'] = fragment
                else:
                    print("No match event found")

                if len(a_tag) > 1:
                    match_event['AssistedBy'] = a_tag[1].text.strip()
                


                match_statistics.append(match_event)
                 
            

        else:
            #match_event = {} 
            #match_event["TBA"] = None
            match_statistics = None
            
        return match_statistics




'''match_list = ['http://www.vilniausfutbolas.lt/varzybos/Sirvintos-VGTU-Vilkai-FK-Tera/26714', 
              'http://www.vilniausfutbolas.lt/varzybos/Granitas-FK-Tera/26728', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-Vova-Juniors/26500', 
              'http://www.vilniausfutbolas.lt/varzybos/Gelezinis-Vilkas-FK-Tera/26900', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Medziai-FK-Tera/26905', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-Vova/26910', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-Gelezinis-Vilkas/26998', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-Navigatoriai/26918', 
              'http://www.vilniausfutbolas.lt/varzybos/Ataka-FK-Tera/26923', 
              'http://www.vilniausfutbolas.lt/varzybos/AFK-FK-Tera/26929', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-VJFK-Trakai/26721', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-ESFA-Versme/26933', 
              'http://www.vilniausfutbolas.lt/varzybos/Vova-FK-Tera/27348', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-Granitas/27360', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-Gelezinis-Vilkas/27366', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-Sirvintos-VGTU-Vilkai/27372', 
              'http://www.vilniausfutbolas.lt/varzybos/Sirvintos-VGTU-Vilkai-FK-Tera/27238', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-Ataka/27375', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-FK-Medziai/27381', 
              'http://www.vilniausfutbolas.lt/varzybos/FK-Tera-AFK/27353', 
              'http://www.vilniausfutbolas.lt/varzybos/VJFK-Trakai-FK-Tera/27385', 
              'http://www.vilniausfutbolas.lt/varzybos/ESFA-Versme-FK-Tera/27392', 
              'http://www.vilniausfutbolas.lt/varzybos/Navigatoriai-FK-Tera/27401']


for match_link in match_list:   

    obj = MatchProcessor(match_link)
    #print(obj.get_match_details())
    obj.get_match_stats()'''
    
   

