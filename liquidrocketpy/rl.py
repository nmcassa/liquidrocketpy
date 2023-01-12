import requests
from bs4 import BeautifulSoup
import json
from json import JSONEncoder

class Team:
    def __init__(self, url: str):
        self.url = "https://liquipedia.net" + url
        page = get_parsed_page(self.url)

        self.roster = self.get_roster(page)
        self.info = self.side_bar_info(page)
        
    def __str__(self):
        return jsonify(self)

    def side_bar_info(self, page: BeautifulSoup):
        data = page.find_all("div", {"class": "infobox-cell-2"})

        i = 0
        ret = {}

        while i < len(data):
            ret[data[i].text[:len(data[i].text)-1]] = data[i+1].text.replace('\xa0','')
            i += 2

        return ret

    def get_roster(self, page: BeautifulSoup):
        data = page.find_all("tbody")

        ret = {'curr': [], 'former': []}

        for table in data:
            if table.find("th", {"class": "roster-title-row2-border"}):
                if table.find("th", {"class": "large-only"}).text == "Active Squad":
                    players = table.find_all("span", {"style": "white-space:pre"})
                    for player in players:
                        ret['curr'].append(player.text)
                if table.find("th", {"class": "large-only"}).text == "Former Players":
                    players = table.find_all("span", {"style": "white-space:pre"})
                    for player in players:
                        ret['former'].append(player.text)

        return ret

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def jsonify(info: dict) -> str:
    return json.dumps(info, indent=4,cls=Encoder)

def get_parsed_page(url: str) -> BeautifulSoup:
    headers = {
        "referer": "https://liquipedia.net",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

def get_na_teams() -> list:
    return get_teams("North_America")

def get_eu_teams() -> list:
    return get_teams("Europe")

def get_oce_teams() -> list:
    return get_teams("Oceania")

def get_sa_teams() -> list:
    return get_teams("South_America")

def get_mena_teams() -> list:
    return get_teams("Middle_East_and_North_Africa")

def get_ap_teams() -> list:
    return get_teams("Asia-Pacific")

def get_ssa_teams() -> list:
    return get_teams("Sub-Saharan_Africa")

def get_school_teams() -> list:
    return get_teams("School")

def get_teams(region: str) -> list:
    page = get_parsed_page("https://liquipedia.net/rocketleague/Portal:Teams/" + region)
    ret = []

    data = page.find_all("span", {"class": "team-template-text"})

    for item in data:
        a = item.find("a")
        ret.append({"name": a.text, 
                    "url": a["href"]})

    return ret

if __name__ == "__main__":
    teams = get_na_teams()

    #print(teams[1:5])

    t = Team('/rocketleague/FaZe_Clan')
    print(t)