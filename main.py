import requests
from bs4 import BeautifulSoup

CHAIR_URL = "https://www.amazon.com/BZLSFHZ-Ergonomic-Adjustable-Headrest-Breathable/dp/B09MB1QT4G/ref=sr_1_206?crid=1BTMETGBD2VVO&keywords=chairs+for+desk&qid=1649319961&sprefix=chairs%2Caps%2C394&sr=8-206"

headers = {
    'Accept-Language': 'en-GB,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0',
}

response = requests.get(CHAIR_URL, headers=headers)
print(response.status_code) #503 Service Unavailable Error on first request without headers; 200 with headers

print(response.text)






# headers not required
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#    'Connection': 'keep-alive',
