import logging
import re
import urllib.request

from bs4 import BeautifulSoup

from src.domain.Text import Text
from src.scraper.AbstractScraper import AbstractScraper


class KrovostokScraper(AbstractScraper):
    SITE_URL = 'http://hip-hop.name'
    BASE_URL = SITE_URL + '/text/krovostok/'

    def __init__(self):
        super(KrovostokScraper, self).__init__('krovostok')

    def execute(self):
        result = []
        for album_link in self.__get_albums_links():
            for track_link in self.__get_tracks_links(album_link):
                for text in self.__parse_lyrics(track_link):
                    result.append(text)

        return result

    def __get_site_links(self, base_url, href_matcher):
        soup = self.__init_soup(self.__get_page_content(base_url))
        for link in soup.find(name='ul', attrs={'class': 'sitemap'}) \
                .findAll(name='a', href=href_matcher):
            yield self.SITE_URL + link['href']

    def __get_albums_links(self):
        return self.__get_site_links(self.BASE_URL, re.compile(r'album'))

    def __get_tracks_links(self, album_link):
        return self.__get_site_links(album_link, True)

    def __get_page_content(self, url):
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf8')

        return html

    def __init_soup(self, html):
        return BeautifulSoup(html, 'html5lib')

    def __parse_lyrics(self, url):
        soup = self.__init_soup(self.__get_page_content(url))
        lyrics = soup.find(name='div', attrs={'class': 'entry'}).get_text()

        for line in lyrics.split('\n'):
            payload = self.beautify(line)
            if payload != '':
                text = Text(self.source, payload, url)
                logging.debug(text)
                yield text
