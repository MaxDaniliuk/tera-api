from ThirdLeagueStandings.imagesdata import ImagesData
from ThirdLeagueStandings.dataextractor import DataExtractor
from ThirdLeagueStandings.standingsdata import StandingsData
#Consider changing the dir name
from TeraData.tera_team import TeraTeam
#from TeraData.match_processor import MatchProcessor
import requests



def main(): 
    extracted_table = DataExtractor('http://www.vilniausfutbolas.lt/lyga/III-Lyga/20')
    standings_table = extracted_table.get_table()
    standings_data = StandingsData(standings_table)
    data = {'standings': standings_data.get_data()}
    
    #Final task
    #
    #images_data = ImagesData(standings_table)
    #images_data.save_images()

    
    
    third_league_standings = input("Do you want to post or put ThirdLeagueStandings data? ")

    if third_league_standings == 'post':
        response = requests.post('http://127.0.0.1:8000/db/thirdleaguestandings', json=data)
        if response.status_code == 201:
            data = response.json()
            if isinstance(data, dict):  
                message = data.get("Message")
                teams_ids = data.get("TeamsIds")

                print('ThirdLeagueStandings Data has been successfully sent to the API.')
                print('Message:', message)
                print('Teams IDs:', teams_ids)

        else:
            print('Failed to post data:', response.status_code)
            print(response.content)
            print(response.json())
    if third_league_standings == 'put':
        response = requests.put('http://127.0.0.1:8000/db/thirdleaguestandings', json=data)
        if response.status_code == 201:
            print('ThirdLeagueStandings Data successfully posted to the API.')
        else:
            print('Failed to post data:', response.status_code)
            print(response.content)
            print(response.json())

    

    tera_team = TeraTeam('http://www.vilniausfutbolas.lt/komanda/FK-Tera/210/20/30')
    players_stats = {"players_data": tera_team.get_players_data()}
    match_data = {"matchStats": tera_team.get_match_data()}
    
    #print(match_data['matchStats'])

    tera_team_players_data = input("Do you want to post or put Tera players' data? ")

    if tera_team_players_data == 'post':
        post_response = requests.post('http://127.0.0.1:8000/db/post/teraplayers', json=players_stats)
        if post_response.status_code == 201:
            data = post_response.json()
            if isinstance(data, dict):  
                message = data.get("Message")
                players_ids = data.get("PlayersIds")

                print('Tera Team data has been successfully sent to the API.')
                print('Message:', message)
                print('Players IDs:', players_ids)
            
        else:
            print('Failed to post team data:', post_response.status_code)
            print(post_response.content)
            print(post_response.json())
    
    if tera_team_players_data == 'put':
        put_response = requests.put('http://127.0.0.1:8000/db/put/teraplayers', json=players_stats)    
        if put_response.status_code == 201:
            print('Team Data has been successfully sent to the API.')
        else:
            print('Failed to post team data:', put_response.status_code)
            print(put_response.content)
            print(put_response.json())
    
    tera_team_matches_data = input("Do you want to post or put Tera match data? ")

    if tera_team_matches_data == 'post':
        post_response_match = requests.post('http://127.0.0.1:8000/db/post/teramatch', json=match_data)
        if post_response_match.status_code == 201:
            data = post_response_match.json()
            if isinstance(data, dict):  
                message = data.get("Message")
                matches_ids = data.get("MatchIds")

                print('Tera Team match data has been successfully sent to the API.')
                print('Message:', message)
                print('Matches IDs:', matches_ids)
            
        else:
            print('Failed to post Tera match data:', post_response_match.status_code)
            print(post_response_match.content)
            #print(post_response_match.json())


    if tera_team_matches_data == 'put':
        put_response_match = requests.put('http://127.0.0.1:8000/db/put/teramatch', json=match_data)    
        if put_response_match.status_code == 201:
            print('Tera Team match data has been successfully sent to the API.')
        else:
            print('Failed to post Tera match data:', put_response_match.status_code)
            print(put_response_match.content)
            #print(put_response_match.json())

if __name__ == "__main__":
    main()
