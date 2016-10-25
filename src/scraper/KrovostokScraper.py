import logging
import re
from urllib.parse import urljoin

from src.domain.Text import Text
from src.scraper.AbstractScraper import AbstractScraper


class KrovostokScraper(AbstractScraper):
    INDEX = 'http://hip-hop.name'
    TEXTS = urljoin(INDEX, '/text/krovostok/')

    def __init__(self):
        super(KrovostokScraper, self).__init__('krovostok')

    def execute(self):

        for album_link in self.__get_albums_links():
            for track_link in self.__get_tracks_links(album_link):
                for text in self.__parse_lyrics(track_link):
                    yield text

    def __get_albums_links(self):
        return self.__get_site_links(self.BASE_URL, re.compile(r'album'))

    def __get_tracks_links(self, album_link):
        return self.__get_site_links(album_link, True)

    def __get_site_links(self, base_url, href_matcher):

        soup = self.init_soup(self.get_page_content(base_url))
        sitemap = soup.find(name='ul', attrs={'class': 'sitemap'})

        for link in sitemap.findAll(name='a', href=href_matcher):
            yield urljoin(INDEX, link['href'])

    def __parse_lyrics(self, url):
        content = self.get_page_content(url)
        soup = self.init_soup(content)

        entry = soup.find(name='div', attrs={'class': 'entry'})
        lyrics = entry.get_text()

        for line in lyrics.split('\n'):
            payload = self.beautify(line)

            if payload != '':
                text = Text(self.source, payload, url)
                logging.debug(text)
                yield text
