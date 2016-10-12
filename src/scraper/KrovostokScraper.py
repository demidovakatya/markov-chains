import logging
import re
import urllib.request

from bs4 import BeautifulSoup

from src.domain.Text import Text
from src.scraper.AbstractScraper import AbstractScraper


class KrovostokScraper(AbstractScraper):
    BASE_URL = 'http://www.krovostok.ru/lyrics/'

    def __init__(self):
        super(KrovostokScraper, self).__init__('krovostok')

    def execute(self):
        result = []
        for url in self.__get_urls():
            result += self.__parse_lyrics(self.__get_page_content(url), url)

        return result

    def __get_urls(self):
        urls = []

        for i in range(1, 14):
            id = '0' + str(i)
            id = id[-2:]
            urls.append(self.BASE_URL + 'gantalya/gan%s.html' % id)

        for i in range(1, 16):
            id = '0' + str(i)
            id = id[-2:]
            urls.append(self.BASE_URL + 'skvoznoye/LS%s.html' % id)

        for i in range(1, 11):
            id = '0' + str(i)
            id = id[-2:]
            urls.append(self.BASE_URL + 'L%s.html' % id)

        return urls

    def __get_page_content(self, url):
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('cp1251')

        return html

    def __parse_lyrics(self, html, url):
        lyrics = []
        soup = BeautifulSoup(html, 'html5lib')
        lyric = soup.find(attrs={'class': 'style2'}).get_text()

        for line in lyric.split('\t'):
            text = Text(
                self.source, re.sub('\s\s+', ' ', self.beautify(line)), url)
            logging.debug(text)
            lyrics.append(text)

        return lyrics
