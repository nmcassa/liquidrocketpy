# liquidrocketpy

 A webscrapping api for the [rocket league page of liquipedia](https://liquipedia.net/rocketleague/Main_Page)

## Install

 ```
 pip install liquidrocketpy
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
 print(rl.jsonify(teams[1:5]))

[
    {
        "name": "303 Esports",
        "url": "/rocketleague/303_Esports"
    },
    {
        "name": "72PC",
        "url": "/rocketleague/72PC"
    },
    {
        "name": "Akrew",
        "url": "/rocketleague/Akrew"
    },
    {
        "name": "Alter Ego",
        "url": "/rocketleague/Alter_Ego"
    }
]
 ```
