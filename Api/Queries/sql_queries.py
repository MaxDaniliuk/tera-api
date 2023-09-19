#This file should contain code that process SQL queries: INSERT, UPDATE, DELETE etc

class StandingsSQLQueries:

    INSERT_STANDINGS_DATA = "INSERT INTO ThirdLeagueStandings (Place, Team, Logo, GamesPlayed, Won, Drawn, Lost, GoalsFor, GoalsAgainst, GoalDifference, Points) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    UPDATE_STANDINGS_DATA = 'UPDATE ThirdLeagueStandings SET Place = %s, Team = %s, Logo = %s, GamesPlayed = %s, Won = %s, Drawn = %s, Lost = %s, GoalsFor = %s, GoalsAgainst = %s, GoalDifference = %s, Points = %s WHERE Team = %s'

    DELETE_STANDINGS_DATA = ''


class TeraTeamSQLQueries:

    INSERT_TEAM_DATA = "INSERT INTO TeraPlayers (FullName, DateOfBirth, Position, Goals, Assists, GC, RC) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    
    
    UPDATE_TEAM_DATA = "UPDATE TeraPlayers SET FullName = %s, DateOfBirth = %s, Position = %s, Goals = %s, Assists = %s, GC = %s, RC = %s WHERE PlayerID = %s"

class TeraPlayersUUIDs:
    pass
    