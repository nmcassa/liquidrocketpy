# liquidrocketpy

 A webscrapping api for the [rocket league page of liquipedia](https://liquipedia.net/rocketleague/Main_Page)

## get_na_teams()
 returns a list of dicts holding na team's names and liquipedia urls

 ```python
 print(jsonify(get_na_teams()[1:5]))

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
