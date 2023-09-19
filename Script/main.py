from ThirdLeagueStandings.imagesdata import ImagesData
from ThirdLeagueStandings.dataextractor import DataExtractor
from ThirdLeagueStandings.standingsdata import StandingsData
from TeraTeam.team_comp import TeraPlayers
import requests



def main(): 
    extracted_table = DataExtractor('http://www.vilniausfutbolas.lt/lyga/III-Lyga/20')
    standings_table = extracted_table.get_table()

    standings_data = StandingsData(standings_table)
    #print(standings_data.get_data())

    data = {'standings': standings_data.get_data()}
    

    #images_data = ImagesData(standings_table)
    #images_data.save_images()

    #Move to posting data to the api. 
    third_league_standings = input("Do you want to post or put ThirdLeagueStandings data? ")

    if third_league_standings == 'post':
        response = requests.post('http://127.0.0.1:8000/db/standingsdata', json=data)
        if response.status_code == 201:
            print('Data successfully posted to the API.')
        else:
            print('Failed to post data:', response.status_code)
            print(response.content)
            print(response.json())
    if third_league_standings == 'put':
        response = requests.put('http://127.0.0.1:8000/db/standingsdata', json=data)
        if response.status_code == 201:
            print('Data successfully posted to the API.')
        else:
            print('Failed to post data:', response.status_code)
            print(response.content)
            print(response.json())

    

    '''results = TeraPlayers('http://www.vilniausfutbolas.lt/komanda/FK-Tera/210/20/30')
    team_data = {'team': results.get_players_data()}

    tera_team = input("Do you want to post or put players' data? ")

    if tera_team == 'post':
        response_team = requests.post('http://127.0.0.1:8000/db/teamdata', json=team_data)
        if response_team.status_code == 201:
            print('Team Data has been successfully posted to the API.')
        else:
            print('Failed to post team data:', response_team.status_code)
            print(response_team.content)
            print(response_team.json())
    if tera_team == 'put':
        response_team = requests.put('http://127.0.0.1:8000/db/teamdata', json=team_data)    
        if response_team.status_code == 201:
            print('Team Data has been successfully posted to the API.')
        else:
            print('Failed to post team data:', response_team.status_code)
            print(response_team.content)
            print(response_team.json())'''

if __name__ == "__main__":
    main()
