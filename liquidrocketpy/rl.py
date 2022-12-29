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
    page = get_parsed_page("https://liquipedia.net/rocketleague/Portal:Teams/North_America")
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
	print(jsonify(get_na_teams()[1:5]))