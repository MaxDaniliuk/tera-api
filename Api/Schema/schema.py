STANDINGS_SCHEMA = [
            "Vieta int",
            "Komanda VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci PRIMARY KEY",
            "Logo VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Rungtynes int",
            "Pergales int",
            "Lygiosios int",
            "Pralaimejimai int",
            "Imusta int",
            "Praleista int",
            "Skirtumas VARCHAR(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci",
            "Taskai int"
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
            Vieta int,
            Komanda VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci PRIMARY KEY,
            Logo VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
            Rungtynes int,
            Pergales int,
            Lygiosios int,
            Pralaimejimai int,
            Imusta int,
            Praleista int,
            Skirtumas VARCHAR(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
            Taskai int
            );'''