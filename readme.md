# liquidrocketpy

 [![PyPI version](https://badge.fury.io/py/liquidrocketpy.svg)](https://badge.fury.io/py/liquidrocketpy)
 [![Downloads](https://static.pepy.tech/personalized-badge/liquidrocketpy?period=month&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/liquidrocketpy)

 A webscrapping api for the [rocket league page of liquipedia](https://liquipedia.net/rocketleague/Main_Page)

## Install

 ```
 pip install liquidrocketpy
 ```

## Team Object

 ```python
 from liquidrocketpy import rl
 t = rl.Team('/rocketleague/FaZe_Clan')
 print(t)

 {
    "url": "https://liquipedia.net/rocketleague/FaZe_Clan",
    "roster": {
        "curr": [
            "Firstkiller",
            "Sypical",
            "mist",
            "Roll Dizz"
        ],
        "former": [
            "AYYJAYY",
            "Moopy",
            "Allushin"
        ]
    },
    "info": {
        "Location": "United States",
        "Region": "North America",
        "Coach": " Raul \"Roll Dizz\" Diaz",
        "Approx. Total Winnings": "$736,870",
        "LPRating": "2789(Rank #1)",
        "RLCS Points": "9 (Rank #1)",
        "Created": "2021-03-19"
    }
 }
 ```

## get_achievements(team: Team) -> list
 get achievements from the teams page (example just prints one result, there's a whole list)

 ```python
 from liquidrocketpy import rl
 t = rl.Team('/rocketleague/FaZe_Clan')
 print(rl.get_achievements(t)[1])

 {'date': '2022-12-11', 'place': '3rd-4th', 'tier': 'S-Tier', 'tourn-name': 'RLCS 2022-23 - Fall Split Major', 'prize': '$25,500'}
 ```

## get_played_matches(team: Team) -> list
 get all matches played with info

 ```python
 from liquidrocketpy import rl
 t = rl.Team('/rocketleague/FaZe_Clan')
 print(rl.get_played_matches(t)[1:5])

 [{'Date': '2023-02-19', 'Tier': 'A-Tier', 'Event': 'RLCS 2022-23 - Winter: NA Regional 2 - Winter Cup', 'Score': '4 : 2', 'Opponent': 'G2 Esports', 'Opponent_Link': '/rocketleague/G2_Esports'}, {'Date': '2023-02-18', 'Tier': 'A-Tier', 'Event': 'RLCS 2022-23 - Winter: NA Regional 2 - Winter Cup', 'Score': '4 : 0', 'Opponent': 'Knights', 'Opponent_Link': '/rocketleague/Knights'}, {'Date': '2023-02-17', 'Tier': 'A-Tier', 'Event': 'RLCS 2022-23 - Winter: NA Regional 2 - Winter Cup', 'Score': '3 : 1', 'Opponent': 'NRG', 'Opponent_Link': '/rocketleague/NRG'}, {'Date': '2023-02-17', 'Tier': 'A-Tier', 'Event': 'RLCS 2022-23 - Winter: NA Regional 2 - Winter Cup', 'Score': '3 : 0', 'Opponent': 'M80', 'Opponent_Link': '/rocketleague/M80'}]
 ```

## Get Teams
 returns a list of dicts holding team's names and liquipedia urls

 | Region      | function call |
 | ----------- | ----------- |
 | North America      | get_na_teams()       |
 | Europe   | get_eu_teams()        |
 | Oceania   | get_oce_teams()    |
 | South America | get_sa_teams() |
 | MENA | get_mena_teams() |
 | Asia-Pacific | get_ap_teams() |
 | Sub-Saharan Africa | get_ssa_teams() |
 | School | get_school_teams() |

 ```python
 from liquidrocketpy import rl
 teams = rl.get_na_teams()
 print(teams[1:5])

 [{'name': '72PC', 'url': '/rocketleague/72PC'}, {'name': 'Akrew', 'url': '/rocketleague/Akrew'}, {'name': 'Alter Ego', 'url': '/rocketleague/Alter_Ego'}, {'name': 'Andriette', 'url': '/rocketleague/Andriette'}]
 ```
