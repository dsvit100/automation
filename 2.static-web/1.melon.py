import requests
from bs4 import BeautifulSoup

lotto_url = 'https://www.melon.com/chart/index.htm'

res = requests.get(lotto_url)

soup = BeautifulSoup(res.text, 'html.parser')

songs = soup.select('div')
print(songs)
for song in songs:
    print(song)

