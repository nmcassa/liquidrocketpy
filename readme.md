# liquidrocketpy

 [![PyPI version](https://badge.fury.io/py/liquidrocketpy.svg)](https://badge.fury.io/py/liquidrocketpy)
 [![Downloads](https://static.pepy.tech/badge/liquidrocketpy)](https://pepy.tech/project/liquidrocketpy)

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
