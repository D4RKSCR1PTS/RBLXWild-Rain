import requests
from bs4 import BeautifulSoup

url = 'https://pastebin.com/raw/kaihdPC7'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
output = ''
blacklist = []

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

open('AutoRain.py', 'w+').write(output)