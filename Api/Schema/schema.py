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


TEAM_SCHEMA =[
    "Komanda VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci PRIMARY KEY",
    "Logo VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
]


'''CREATE TABLE players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY,
    PlayerName VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    TeamKomanda VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    FOREIGN KEY (TeamKomanda) REFERENCES team(Komanda)
);'''


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