import requests
from bs4 import BeautifulSoup
import json


def scrapBlogs():
    pageToScrape = requests.get("https://mogi.vn/ha-noi/mua-nha-dat")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")

    Contents = soup.findAll('div', attrs={'class': 'sc-q9qagu-14 eOzaio'})
    Links = soup.findAll('a', attrs={'class': 'title'})

    data = []

    for Content, Link in zip(Contents, Links):
        item = {"content": Content.get_text().strip(), "link": Link.get('href')}
        data.append(item)

    with open('scraped_data3.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


scrapBlogs()