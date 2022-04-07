import requests
from bs4 import BeautifulSoup
import pprint

pp = pprint.PrettyPrinter(indent=4)

CHAIR_URL = "https://www.amazon.com/BZLSFHZ-Ergonomic-Adjustable-Headrest-Breathable/dp/B09MB1QT4G/ref=sr_1_206?crid=1BTMETGBD2VVO&keywords=chairs+for+desk&qid=1649319961&sprefix=chairs%2Caps%2C394&sr=8-206"

headers = {
    'Accept-Language': 'en-GB,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0',
}

response = requests.get(CHAIR_URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
item_price_no_currency = soup.find("span", "a-offscreen").getText().split("$")[1]
item_price_no_commas = item_price_no_currency.replace(",", "")
item_price = float(item_price_no_commas)

print(item_price)


