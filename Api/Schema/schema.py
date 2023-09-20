THIRDLEAGUESTANDINGS_SCHEMA = [
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
    "PlayerId"
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


PLAYERS_IDS = {
            'Lukas Jatkauskas': 'cceb100f-1d4a-42de-ac17-da7d03722055', 'Svajūnas Baušys': '58da8811-7b3a-4c2f-abbf-ce820cc94434', 
            'Oleksandr Stoianovych': '27cc09cc-fd3f-4c86-805e-44ec82d59970', 'Vadim Švaikevič': 'd6e92127-7692-4da4-9bd7-0b20c84fa1f6', 
            'Andrejus Sorokinas': '39bee918-fae2-4fe6-b779-426b400967d4', 'Miroslav Bardovski': '04dc3e03-2bfb-4212-8474-6d1d9814504f', 
            'Vladimir Chmelevskij': 'b777752a-4ff6-4650-9166-4fea968361fa', 'Gintas Ignatavičius': '7b0c734f-e6ab-4de6-ada7-42f7f2e1d788', 
            'Artūras Lebedevas': 'e9b39559-5329-4082-a37f-9c1fc1d5e32d', 'Paulius Širvys': 'ae117d3a-22d5-49d2-b078-c746cb382c9d', 
            'Edvinas Bogdanovas': '4381bd72-3350-4946-847c-9fecc7b2f181', 'Justinas Jurčiukonis': '29a8fbec-c8e5-4380-aab7-b1d62f977ec1', 
            'Ignas Peikštenis': '24f383c6-f8d0-4019-a470-1d8ae2dafcdb', 'David Kirzneris': 'd4d15ad0-2143-432d-962f-c897c6996531', 
            'Valentyn Yanak': '13fb6d8b-1ace-4e16-b7eb-666ffd65b1e2', 'Mark Daniliuk': 'c8a1bb49-eca3-49a4-b41c-99e0e9307a0d', 
            'Denys Chernousov': 'ff9beb10-b7e2-4459-a403-1d54161036d2', 'Artem Nastaius': '92f01c5f-1f3c-4a35-bce5-1e7ad428dcbe', 
            'Sergejus Vasiljevas': '6b366236-d5c1-4769-ac06-4c19b820b587', 'Artūr Semaško': '4ad0580f-2d34-42e2-9073-88bf56b91158', 
            'Aleksejus Kliosovas': 'f603adb9-5e4b-40b4-ac14-3de685ccfe27', 'Simonas Laužikas': 'd0150387-0182-4848-b16e-90e27a0df96b', 
            'Vytautas Velička': '66f67e47-fd45-4532-9194-eca94b3abcac', 'Liudvikas Velička': '9d90f467-0031-4d33-b34d-7913eb7c8734', 
            'Mark Bogdevič': 'c55406f4-09f7-428e-85cd-ee814c7570d9', 'Oleksij Mazurenko': 'a4529fa1-7b78-42af-8cb0-c3b05f9ef2a4', 
            'Igoris Sinkevicius': '4855a267-cdc4-4be7-bf8a-7041e9f1f3b7', 'Oleksandr Saprykin': '3dc67b7b-9901-48d2-8944-135b199d8634', 
            'Patricijus Steponaitis': 'd78790d1-26d9-4350-8791-76c1f40742fb', 'Herkus Adomaitis': '2ab6c818-6ba3-4d2a-aa49-96015b8c8224', 
            'Antanas Velutovičius': 'd7cbad10-9e9f-41cd-97bf-1b76a8819c5e', 'Oleksii Nastaius': 'bdce4856-d4bc-41da-bc65-049db8df18a6', 
            'Igor Choroškin': '97f1e06d-732a-4df4-8d3f-e26d119173f2', 'Gintautas Sidorovas': '1ce56627-3836-456b-bab0-e948789dd706', 
            'Sergejus Ždanovičius': '5aa811e5-a043-4cf5-b033-4efc692b1739', 'Donat Vasiljev': 'ed1ba2a6-994e-4504-81c6-71467a00e849', 
            'Viačeslav Trušakov': '2a76e225-0df8-4f39-91ce-b72af5982545', 'Artem Shevchenko': '4a969177-05bf-4348-9df5-044756c24b81', 
            'Maksimilian  Veršinin': '19467182-9d50-4b96-920d-acf8f013df78', 'Aleksandr Fursov': 'cb242cfd-eb88-4ecb-8ef4-7139ee84a1d3', 
            'Nikita Burlakov': 'a2ab355b-fefe-4022-8801-f9cd1917fa4e'}
    
