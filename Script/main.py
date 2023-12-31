from ThirdLeagueStandings.imagesdata import ImagesData
from ThirdLeagueStandings.dataextractor import DataExtractor
from ThirdLeagueStandings.standingsdata import StandingsData
from TeraData.tera_team import TeraTeam
import requests


def main(): 
    
    extracted_table = DataExtractor('http://www.vilniausfutbolas.lt/lyga/III-Lyga/20')
    standings_table = extracted_table.get_table()
    standings_data = StandingsData(standings_table)
    table_data_third_league = {'standings': standings_data.get_data()}

    #Final task
    #
    #images_data = ImagesData(standings_table)
    #images_data.save_images()
    
    post_response_third_league = requests.post('http://0.0.0.0:5973/db/post/thirdleaguestandings', json=table_data_third_league)
    if post_response_third_league.status_code == 201:
        third_league_data = post_response_third_league.json()
        if isinstance(third_league_data, dict):  
            message = third_league_data.get("Message")
            teams_ids = third_league_data.get("TeamsIds")

            print('ThirdLeagueStandings Data has been successfully sent to the API.')
            print('Message:', message)
            print('Teams IDs:', teams_ids)

    else:
        print('Failed to post data:', post_response_third_league.status_code)
        print(post_response_third_league.content)

    
    put_response_third_league = requests.put('http://0.0.0.0:5973/db/put/thirdleaguestandings', json=table_data_third_league)
    if put_response_third_league.status_code == 201:
        print('ThirdLeagueStandings Data has been successfully sent to the API.')
    else:
        print('Failed to send data:', put_response_third_league.status_code)
        print(put_response_third_league.content)
    

    tera_team = TeraTeam('http://www.vilniausfutbolas.lt/komanda/FK-Tera/210/20/30')
    players_stats = {"players_data": tera_team.get_players_data()}
    match_data = {"matchStats": tera_team.get_match_data()}
    
    
    post_response_players = requests.post('http://0.0.0.0:5973/db/post/teraplayers', json=players_stats)
    if post_response_players.status_code == 201:
        data_players = post_response_players.json()
        if isinstance(data_players, dict):  
            message = data_players.get("Message")
            players_ids = data_players.get("PlayersIds")

            print('Tera Team data has been successfully sent to the API.')
            print('Message:', message)
            print('Players IDs:', players_ids)
        
    else:
        print('Failed to post team data:', post_response_players.status_code)
        print(post_response_players.content)
        
    
    put_response_players = requests.put('http://0.0.0.0:5973/db/put/teraplayers', json=players_stats)    
    if put_response_players.status_code == 201:
        print('Team Data has been successfully sent to the API.')
    else:
        print('Failed to send team data:', put_response_players.status_code)
        print(put_response_players.content)
    
    
    post_response_match = requests.post('http://0.0.0.0:5973/db/post/teramatch', json=match_data)
    if post_response_match.status_code == 201:
        data_match = post_response_match.json()
        if isinstance(data_match, dict):  
            message = data_match.get("Message")
            matches_ids = data_match.get("MatchIds")

            print('Tera Team match data has been successfully sent to the API.')
            print('Message:', message)
            print('Matches IDs:', matches_ids)
        
    else:
        print('Failed to post Tera match data:', post_response_match.status_code)
        print(post_response_match.content)
    

    put_response_match = requests.put('http://0.0.0.0:5973/db/put/teramatch', json=match_data)    
    if put_response_match.status_code == 201:
        print('Tera Team match data has been successfully sent to the API.')
    else:
        print('Failed to send Tera match data:', put_response_match.status_code)
        print(put_response_match.content)
        

if __name__ == "__main__":
    main()
    
    
