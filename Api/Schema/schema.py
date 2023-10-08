
class DBSchema:

    THIRDLEAGUESTANDINGS_SCHEMA = [
                "TeamId CHAR(8) NOT NULL",
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
                "Points int",
                "PRIMARY KEY (TeamId)"
                ]

    TERAPLAYERS_SCHEMA =[
        "PlayerId CHAR(36) NOT NULL"
        "FullName VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci", 
        "DateOfBirth VARCHAR(30)", 
        "Position VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci", 
        "Goals INT", 
        "Assists INT", 
        "GC INT", 
        "RC INT",
        "Team VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci", 
        "PRIMARY KEY (PlayerID)" 
    ]

    TERA_MATCH_DETAILS = [
            "MatchId CHAR(16) NOT NULL", 
            "TeamHome VARCHAR(8) NOT NULL", 
            "TeamAway VARCHAR(8) NOT NULL", 
            "League VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci", 
            "DateTime DATETIME", 
            "Stats JSON", 
            "StadiumId VARCHAR(12)",  
            "PRIMARY KEY (MatchId)"
    ]

class IdContainer:
    
    PLAYERS_IDS = {'Lukas Jatkauskas': '1f8033d0-8d00-4d3a-a105-d97eda0e07be', 'Svajūnas Baušys': 'bf0e2f13-c999-457a-8f72-6bca2630ccd8', 
                   'Edvinas Vencius': '172a0bf9-355c-4fb8-be4f-e9baac2ebbb2', 'Oleksandr Stoianovych': '453a5c11-1c29-42a2-902d-e4a0888e2901', 
                   'Vadim Švaikevič': '4f110c61-cbd7-42f3-9b1e-205fd9edc6da', 'Andrejus Sorokinas': '4f9eca7b-4037-4d07-b5aa-51f5f9b3c1f0', 
                   'Miroslav Bardovski': 'd55bd518-bf61-40be-8d54-f1d6a7371ee4', 'Vladimir Chmelevskij': '3b06ba6f-013b-45f9-93c2-6ae0d8da5e08', 
                   'Gintas Ignatavičius': '635c8a92-48bc-46eb-b28b-7ad2182cd3b6', 'Artūras Lebedevas': 'd26b2134-e863-41aa-90dc-3090394d99fc', 
                   'Paulius Širvys': '00b9ca11-0464-48b6-bc99-b594f6d8a408', 'Edvinas Bogdanovas': 'd735e9d8-dda7-4544-9ce1-3e89baa88c31', 
                   'Justinas Jurčiukonis': '42d2bd66-19be-4b6c-8ad8-fe6aa6306e81', 'Ignas Peikštenis': 'be48c7d4-8abc-4ace-975c-278943e1f4a1', 
                   'David Kirzneris': 'b4e9e586-f231-4cb3-864c-b99cd3a8e2d6', 'Valentyn Yanak': '94c571ef-baf4-4a4c-afe7-e63abe723f5a', 
                   'Mark Daniliuk': 'ccc00638-a766-4a51-90f4-903e5285df1d', 'Denys Chernousov': 'a46377a5-99e4-4600-91a3-f0eb7e49ce65', 
                   'Artem Nastaius': 'cb25ed0e-8c74-4a44-9064-25d7f69f2cd9', 'Sergejus Vasiljevas': 'c23a1abf-b8c3-42e4-a274-e90570e4a3ec', 
                   'Artūr Semaško': 'a365aca6-a3c5-4d54-aa9f-6cc947aa36e8', 'Aleksejus Kliosovas': 'abbad6e0-a397-4aca-b0d6-90f70992ef9b', 
                   'Simonas Laužikas': 'edabfa49-2b71-48c9-b57f-41eff9e393b2', 'Vytautas Velička': 'ffa3a27e-0b69-461f-9e29-f40b428b868c', 
                   'Liudvikas Velička': '862a787a-d27b-429b-aa61-68262138004a', 'Mark Bogdevič': '8cea5c56-a6ee-4c98-9de3-634f4b8e98f3', 
                   'Oleksij Mazurenko': '760a03de-d089-4433-a676-1c8e42dc6f0f', 'Igoris Sinkevicius': '010f2cc6-e2dd-4d78-8e40-6b23d8db0475', 
                   'Oleksandr Saprykin': 'a79159bc-21ee-4597-80a5-9528be65156e', 'Patricijus Steponaitis': 'c347179c-d6ba-45ea-94d8-06ac60a07f71', 
                   'Herkus Adomaitis': 'b1f99c8a-e648-4f02-a991-061e76b1f961', 'Antanas Velutovičius': '286c23ae-d662-4502-8c11-3231f507de8a', 
                   'Oleksii Nastaius': 'a58614fa-5f23-4ec0-b162-368669a19b79', 'Igor Choroškin': '20970981-a1b9-4516-92f6-64cb0e1e30d5', 
                   'Gintautas Sidorovas': 'a0863f14-a0b5-48b1-98c7-0eabf3cfa028', 'Sergejus Ždanovičius': '4f687990-4bc1-4aad-a515-61e73f145412', 
                   'Donat Vasiljev': 'f4321465-de58-4f6a-b4ed-218fcf1c37cc', 'Viačeslav Trušakov': '681dedf9-a462-4c55-ab42-ef334b17947c', 
                   'Artem Shevchenko': 'd1eb6723-7fe0-486f-b05a-5ee872d46ccd', 'Maksimilian  Veršinin': '364e5a75-4acd-40c3-abf9-049aa133a669', 
                   'Aleksandr Fursov': '69650768-f2f1-4d41-a6e8-3d2fdb56491e', 'Nikita Burlakov': 'da11afbf-c3cb-42a0-ad0f-d8a50d6af9a1'}

    TEAM_IDS = {
                'FK Medžiai': '0134e67c', 'FK Granitas': 'b98a65af', 'Granitas': 'b98a65af', 
                'Širvintos-VGTU-Vilkai': '8feb1b7d','VGTU-Vilkai': '8feb1b7d' , 'FK Tera': '9530fd95', 
                'AFK': '28db5534', 'Ataka': '132b0982', 'FC Vova': 'eb875212', 'Vova': 'eb875212',
                'ESFA-Versmė': 'd68ecc9e', 'FK Elektrėnų Versmė': 'd68ecc9e','FK Navigatoriai': 'e955663a', 'Navigatoriai': 'e955663a', 
                'VJFK Trakai': 'bcacbf85', 'FK Geležinis Vilkas': 'd4380b48', 'Geležinis Vilkas': 'd4380b48',
                'FC Vova Juniors': '7faefe00', 'Vova Juniors': '7faefe00'
                }
    
    STADIUM_IDS = {
                'Širvintų stadionas': 'c4f769b4-fc8', 'BFA arena': '8a0360fb-21d', 
                'Nemenčinė': '9a6c5ffb-780', 'Kariškių stadionas': 'ace9be40-309', 
                'Senvagės stadionas': 'ad814714-28c', 'Pilaitės stadionas': 'edbbfae3-496', 
                'Trakų naujas': '7a641419-67c'
                }
    
    Match_IDs = {
                '1': '6ebf2cc1-1912-49', '2': 'f35c66d4-3965-41', '3': 'e6ea0e61-6c83-41', '4': '4aed0cc4-f368-4f', 
                '5': '8a297683-c6d4-47', '6': '64a5e248-da5e-4d', '7': '24f8dcb6-903c-4c', '8': 'b9115000-ce1c-40', 
                '9': 'eec614bc-9859-40', '10': '0c29e94c-40c8-4e', '11': 'f28a6928-229e-47', '12': 'ce55f015-eba8-46', 
                '13': '8cd3e647-d2bc-4e', '14': '7e1578b7-896f-4d', '15': '079ac5b8-1dde-44', '16': '7616b149-9e51-4f', 
                '17': '2d15a28f-d5e1-4d', '18': '4653fdbe-d9a5-45', '19': 'fd9394a1-fc17-41', '20': 'f3293933-28b5-45', 
                '21': '3b0afff4-9150-45', '22': 'c982d441-3a11-42', '23': 'd6c98c20-efdd-44'
               }
    
