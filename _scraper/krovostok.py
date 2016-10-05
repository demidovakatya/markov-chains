import re
import urllib.request
from bs4 import BeautifulSoup

# DOMAIN = 'http://megalyrics.ru'

# start_url = 'http://megalyrics.ru/about/krovostok.htm'
# with urllib.request.urlopen(start_url) as response:
#    html = response.read()
# soup = bs4.BeautifulSoup(html, 'html5lib')
# rel_urls = soup.findAll(attrs = {'class' : 'st-title'})
# urls = []
# for rel_url in rel_urls:
#     if re.search('<a href="/lyric/', str(rel_url.contents[0])):
#         urls.append(DOMAIN + rel_url.a.get('href'))



urls = []
BASE_URL = 'http://www.krovostok.ru/lyrics/'

for i in range(1, 14):
    id = '0' + str(i)
    id = id[-2:]
    urls.append(BASE_URL + 'gantalya/gan%s.html' % id)

for i in range(1, 16):
    id = '0' + str(i)
    id = id[-2:]
    urls.append(BASE_URL + 'skvoznoye/LS%s.html' % id)

for i in range(1, 11):
    id = '0' + str(i)
    id = id[-2:]
    urls.append(BASE_URL + 'L%s.html' % id)

lyrics = []

for url in urls:
    with urllib.request.urlopen(url) as response:
       html = response.read().decode('cp1251')

    soup = bs4.BeautifulSoup(html, 'html5lib')
    lyric = soup.find(attrs = {'class': 'style2'}).get_text()
    lines = [re.sub('\s\s+', ' ', line.strip()) for line in lyric.split('\t')]
    lyrics += lines

with open('lyrics.txt', 'w') as txt_file:
        txt_file.write('\n'.join(lyrics))
