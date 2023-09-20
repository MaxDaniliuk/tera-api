#This file should contain code that process SQL queries: INSERT, UPDATE, DELETE etc

class StandingsSQLQueries:

    CREATE_THIRD_LEAGUE_STANDINGS = '''
        CREATE TABLE ThirdLeagueStandings (
            Place int,
            Team VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci PRIMARY KEY,
            Logo VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
            GamesPlayed int,
            Won int,
            Drawn int,
            Lost int,
            GoalsFor int,
            GoalsAgainst int,
            GoalDifference VARCHAR(5),
            Points int
            );
        '''

    INSERT_STANDINGS_DATA = "INSERT INTO ThirdLeagueStandings (Place, Team, Logo, GamesPlayed, Won, Drawn, Lost, GoalsFor, GoalsAgainst, GoalDifference, Points) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    UPDATE_STANDINGS_DATA = 'UPDATE ThirdLeagueStandings SET Place = %s, Team = %s, Logo = %s, GamesPlayed = %s, Won = %s, Drawn = %s, Lost = %s, GoalsFor = %s, GoalsAgainst = %s, GoalDifference = %s, Points = %s WHERE Team = %s'

    DELETE_STANDINGS_DATA = ''


class TeraTeamSQLQueries:

    CREATE_TERA_PLAYERS = '''
        CREATE TABLE TeraPlayers ( 
            PlayerId CHAR(36) NOT NULL, 
            FullName VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, 
            DateOfBirth VARCHAR(30), 
            Position VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, 
            Goals INT, 
            Assists INT, 
            GC INT, 
            RC INT, 
            Team VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, 
            PRIMARY KEY (PlayerId) 
            );
        '''

    INSERT_PLAYERS_DATA = "INSERT INTO TeraPlayers (PlayerID, FullName, DateOfBirth, Position, Goals, Assists, GC, RC, Team) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    
    UPDATE_PLAYERS_DATA = "UPDATE TeraPlayers SET FullName = %s, DateOfBirth = %s, Position = %s, Goals = %s, Assists = %s, GC = %s, RC = %s WHERE PlayerId = %s"

