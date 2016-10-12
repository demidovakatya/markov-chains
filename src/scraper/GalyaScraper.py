import logging
import re
import urllib.request

from bs4 import BeautifulSoup

from src.domain.Text import Text
from src.scraper.AbstractScraper import AbstractScraper


class GalyaScraper(AbstractScraper):
    DOMAIN = 'http://galya.ru'

    def __init__(self, n_pages=1):
        super(GalyaScraper, self).__init__('galya.ru')
        self.n_pages = n_pages

    def execute(self):
        return self.__get_threads_posts(self.__get_threads_urls(self.n_pages))

    def __get_threads_urls(self, n_pages=1):
        threads_urls = []
        for page in range(0, n_pages):
            url = self.DOMAIN + \
                '/clubs/index.php?dlimit=%s&p=1&board_id=0&ltype=0' % (
                    page * 115)
            logging.info('Reading %s...' % url)

            with urllib.request.urlopen(url) as response:
                html = response.read()

            soup = BeautifulSoup(html, 'html5lib')
            threads_urls += [self.DOMAIN + '/clubs/' + re.sub('&.*', '', a.get('href')) for a
                             in soup.findAll(attrs={'title': 'дата последнего комментария'})]
        logging.info('Found: %s threads.' % len(threads_urls))

        return threads_urls

    def __get_posts(self, url):
        with urllib.request.urlopen(url) as response:
            html = response.read()
        soup = BeautifulSoup(html, 'html5lib')

        posts = []
        for hit in soup.findAll(attrs={'class': 'text'}):
            this_post = hit.get_text(separator=' ')
            text = Text(self.source, self.beautify(this_post), url)
            logging.debug(text)
            posts.append(text)

        return posts

    def __get_threads_posts(self, threads_urls):
        threads_posts = []
        for url in threads_urls:
            threads_posts += self.__get_posts(url)

        return threads_posts
