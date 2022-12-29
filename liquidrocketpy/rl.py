import requests
from bs4 import BeautifulSoup
import json
from json import JSONEncoder

def get_parsed_page(url: str) -> BeautifulSoup:
    # This fixes a blocked by cloudflare error i've encountered
    headers = {
        "referer": "https://liquipedia.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

if __name__ == "__main__":
	print(get_parsed_page("https://liquipedia.net/rocketleague/Portal:Teams"))