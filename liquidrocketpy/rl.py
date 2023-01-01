import requests
from bs4 import BeautifulSoup
import json
from json import JSONEncoder

def get_parsed_page(url: str) -> BeautifulSoup:
    headers = {
        "referer": "https://liquipedia.com",
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

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def jsonify(self) -> str:
    return json.dumps(self, indent=4,cls=Encoder)

if __name__ == "__main__":
	print(jsonify(get_school_teams()[1:5]))