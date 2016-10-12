import logging
import urllib.request

from bs4 import BeautifulSoup

from src.domain.Text import Text
from src.scraper.AbstractScraper import AbstractScraper


class BScraper(AbstractScraper):
    DOMAIN = 'http://2ch.hk'

    def __init__(self, board='b', n_pages=5):
        super(BScraper, self).__init__('2ch')
        self.board = board
        self.n_pages = n_pages

    def execute(self):
        return self.__get_board_posts(self.__get_thread_urls(self.n_pages))

    def __get_thread_urls(self, n_pages):
        thread_urls = []
        for page in range(1, n_pages + 1):
            url = self.DOMAIN + '/' + self.board + '/' + str(page) + '.html'
            logging.info('Reading %s...' % url)

            with urllib.request.urlopen(url) as response:
                html = response.read()

            soup = BeautifulSoup(html, 'html5lib')
            thread_urls += [self.DOMAIN + a.get('href') for a
                            in soup.findAll(attrs={'class': 'orange'})]
        logging.info('Found: %s threads.' % len(thread_urls))

        return thread_urls

    def __get_thread_posts(self, url):
        with urllib.request.urlopen(url) as response:
            html = response.read()
        soup = BeautifulSoup(html, 'html5lib')

        posts = []
        for hit in soup.findAll(attrs={'class': 'post-message'}):
            this_post = hit.get_text(separator=' ')
            text = Text(self.source, self.beautify(this_post), url)
            logging.debug(text)
            posts.append(text)

        return posts

    def __get_board_posts(self, thread_urls):
        board_posts = []
        for url in thread_urls:
            board_posts += self.__get_thread_posts(url)
        return board_posts
