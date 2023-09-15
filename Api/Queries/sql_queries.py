#This file should contain code that process SQL queries: INSERT, UPDATE, DELETE etc

class StandingsSQLQueries:

    INSERT_STANDINGS_DATA = "INSERT INTO ThirdLeagueStandings (Vieta, Komanda, Logo, Rungtynes, Pergales, Lygiosios, Pralaimejimai, Imusta, Praleista, Skirtumas, Taskai) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    UPDATE_STANDINGS_DATA = 'UPDATE ThirdLeagueStandings SET Vieta = %s, Komanda = %s, Logo = %s, Rungtynes = %s, Pergales = %s, Lygiosios = %s, Pralaimejimai = %s, Imusta = %s, Praleista = %s, Skirtumas = %s, Taskai = %s WHERE ID = %s'

    DELETE_STANDINGS_DATA = ''

    