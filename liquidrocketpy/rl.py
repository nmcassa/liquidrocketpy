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

        self.clean()
        
    def __str__(self):
        return jsonify(self)

    def side_bar_info(self, page: BeautifulSoup) -> dict:
        data = page.find_all("div", {"class": "infobox-cell-2"})

        ret = {}

        for item in data:
            adult = item.parent

            d = adult.find_all('div')

            if len(d) != 2:
                raise Exception("Unexpected Side Bar Info")

            ret[d[0].text] = d[1].text

        return ret

    def get_roster(self, page: BeautifulSoup) -> dict:
        #gets current and former players for a team
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

    def clean(self) -> None:
        #removes unwanted chars from class info
        for idx, item in enumerate(self.roster['curr']):
            self.roster['curr'][idx] = item.replace('\u00a0', '')

        for idx, item in enumerate(self.roster['former']):
            self.roster['former'][idx] = item.replace('\u00a0', '')

        for item in self.info.keys():
            self.info[item] = self.info[item].replace('\u00a0', '')


def get_achievements(team: Team) -> list:
    page = get_parsed_page(team.url)

    data = page.find("div", {"class": "achievements"}).find("tbody")
    rows = data.find_all("tr")
    rows = rows[1:len(rows)-1]

    ret = []

    for row in rows:
        outcome = {}

        displays = row.find_all("span", {"style": "display:none;"})

        outcome['date'] = row.find("td").text
        outcome['place'] = row.find("b", {"class": "placement-text"}).text.replace('\xa0', ' ')
        outcome['tier'] = displays[0].next_sibling.text
        outcome['tourn-name'] = displays[1].text
        outcome['prize'] = row.find_all("td", {"style": "text-align:left"})[1].text

        ret.append(outcome)

    return ret

def get_played_matches(team: Team) -> list:
    page = get_parsed_page(team.url + '/Played_Matches')
    data = page.find_all('tr')[1:]

    ret = []

    for item in data:
        info = {}

        table_data = item.find_all('td')

        info['Date'] = table_data[0].text
        info['Tier'] = table_data[2].find('a').text
        info['Event'] = table_data[3].find('span').text
        info['Score'] = table_data[5].text.replace('\xa0', ' ')
        info['Opponent'] = table_data[6].find('a')['title']
        info['Opponent_Link'] = table_data[6].find('a')['href']

        ret.append(info)

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
    #teams = get_na_teams()
    #print(teams[1:5])

    #t = Team('/rocketleague/Gen.G_Mobil1_Racing')
    t = Team('/rocketleague/FaZe_Clan')
    print(t)
    #print(get_achievements(t)[1])
    #print(get_played_matches(t)[1:5])

