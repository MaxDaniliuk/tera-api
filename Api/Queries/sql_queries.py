#This file should contain code that process SQL queries: INSERT, UPDATE, DELETE etc

class StandingsSQLQueries:

    CREATE_THIRD_LEAGUE_STANDINGS = '''
        CREATE TABLE ThirdLeagueStandings (
            TeamId CHAR(8) NOT NULL,
            Place int,
            Team VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
            Logo VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
            GamesPlayed int,
            Won int,
            Drawn int,
            Lost int,
            GoalsFor int,
            GoalsAgainst int,
            GoalDifference VARCHAR(5),
            Points int,
            PRIMARY KEY (TeamId)
            );
        '''

    INSERT_STANDINGS_DATA = "INSERT INTO ThirdLeagueStandings (TeamId, Place, Team, Logo, GamesPlayed, Won, Drawn, Lost, GoalsFor, GoalsAgainst, GoalDifference, Points) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    UPDATE_STANDINGS_DATA = 'UPDATE ThirdLeagueStandings SET Place = %s, Team = %s, Logo = %s, GamesPlayed = %s, Won = %s, Drawn = %s, Lost = %s, GoalsFor = %s, GoalsAgainst = %s, GoalDifference = %s, Points = %s WHERE TeamId = %s'

    SELECT_THIRD_LEAGUE_STANDINGS = "SELECT Place, Team, GamesPlayed, Won, Drawn, Lost, GoalsFor, GoalsAgainst, GoalDifference, Points FROM ThirdLeagueStandings ORDER BY Place" 


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

    INSERT_PLAYERS_DATA = "INSERT INTO TeraPlayers (PlayerID, FullName, DateOfBirth, Position, Goals, Assists, GC, RC, TeamId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    UPDATE_PLAYERS_DATA = "UPDATE TeraPlayers SET FullName = %s, DateOfBirth = %s, Position = %s, Goals = %s, Assists = %s, GC = %s, RC = %s WHERE PlayerId = %s"

    SELECT_PLAYERS_BY_POSTION = "SELECT FullName, DateOfBirth, Position, Goals, Assists, GC, RC FROM TeraPlayers WHERE Position = %s ORDER BY Goals DESC"


class TeraMatchSQLQueries:
    CREATE_TERA_MATCH = '''
        CREATE TABLE TeraMatch ( 
            MatchId CHAR(16) NOT NULL, 
            TeamHome VARCHAR(8) NOT NULL, 
            TeamAway VARCHAR(8) NOT NULL, 
            League VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, 
            DateTime DATETIME, 
            Stats JSON, 
            StadiumId VARCHAR(12),  
            PRIMARY KEY (MatchId)
            );
        '''

    INSERT_TERA_MATCH = "INSERT INTO TeraMatch (MatchId, TeamHome, TeamAway, League, DateTime, Stats, StadiumId) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    UPDATE_TERA_MATCH = "UPDATE TeraMatch SET TeamHome = %s, TeamAway = %s, League = %s, DateTime = %s, Stats = %s, StadiumId = %s WHERE MatchId = %s"

    SELECT_PREVIOUS_MATCH = "SELECT TeamHome, TeamAway, League, DateTime, CAST(Stats AS JSON), StadiumId FROM TeraMatch WHERE DateTime < %s ORDER BY DateTime DESC LIMIT %s" #s is current DateTime

    SELECT_NEXT_MATCH = "SELECT TeamHome, TeamAway, League, DateTime, CAST(Stats AS JSON), StadiumId FROM TeraMatch WHERE DateTime > %s ORDER BY DateTime LIMIT %s" #s is current DateTime
                                                            

class Stadiums:
    #Incomplete query
    CREATE_STADIUMS = '''
            StadiumId CHAR(12) NOT NULL, 
            StadiumName VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, 
            Lat DOUBLE,
            Long DOUBLE,
            PRIMARY KEY (StadiumId) 
'''
    INSERT_STADIUMS = "INSERT INTO Stadiums (StadiumId, StadiumName, Lat, Long) VALUES (%s, %s, %s, %s)"

    SELECT_STADIUM = "SELECT StadiumName, Lat, Long FROM Stadiums WHERE StadiumId = %s"