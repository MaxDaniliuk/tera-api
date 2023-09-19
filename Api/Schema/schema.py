STANDINGS_SCHEMA = [
            "Place int",
            "Team VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci PRIMARY KEY",
            "Logo VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "GamesPlayed int",
            "Won int",
            "Drawn int",
            "Lost int",
            "GoalsFor int",
            "GoalsAgainst int",
            "GaolDifference VARCHAR(5)",
            "Points int"
            ]


TERAPLAYERS_SCHEMA =[
    "PlayerID INT AUTO_INCREMENT PRIMARY KEY"
    "FullName VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci", 
    "DateOfBirth VARCHAR(30)", 
    "Position VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci", 
    "Goals INT", 
    "Assists INT", 
    "GC INT", 
    "RC INT"
]


'''
CREATE TABLE TeraPlayers (
    PlayerID UUID PRIMARY KEY DEFAULT UUID(),
    FullName VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, 
    DateOfBirth VARCHAR(30), 
    Position VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci, 
    Goals INT, 
    Assists INT, 
    GC INT, 
    RC INT
);
'''


#Create table query
'''CREATE TABLE ThirdLeagueStandings (
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
            );'''