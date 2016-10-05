from src.scraper.AbstractScraper import AbstractScraper
from src.Logger import Logger
from src.Text import Text

import re
import urllib.request
from bs4 import BeautifulSoup


class BScraper(AbstractScraper):
    DOMAIN = 'http://2ch.hk'
    LOG = Logger()

    def __init__(self, board, n_pages):
        self.board = board
        self.n_pages = n_pages

    def execute(self):
        return self.__get_board_posts(self.__get_thread_urls(self.n_pages))

    def __get_thread_urls(self, n_pages):
        thread_urls = []
        for page in range(1, n_pages + 1):
            url = self.DOMAIN + '/' + self.board + '/' + str(page) + '.html'
            self.LOG.info('Reading %s...' % url)

            with urllib.request.urlopen(url) as response:
                html = response.read()

            soup = BeautifulSoup(html, 'html5lib')
            thread_urls += [self.DOMAIN + a.get('href') for a
                            in soup.findAll(attrs = {'class': 'orange'})]
        self.LOG.info('Found: %s threads.' % len(thread_urls))

        return thread_urls

    def __get_thread_posts(self, url):
        with urllib.request.urlopen(url) as response:
            html = response.read()
        soup = BeautifulSoup(html, 'html5lib')

        posts = []
        for hit in soup.findAll(attrs={'class' : 'post-message'}):
            this_post = hit.get_text(separator = ' ')
            posts.append(Text(self.__format_text(this_post), url))

        return posts

    def __get_board_posts(self, thread_urls):
        board_posts = []
        for url in thread_urls:
            board_posts += self.__get_thread_posts(url)
        return board_posts

    # remove quotes, unnecessary punctuation, etc
    def __format_text(self, text):
        text = re.sub(r'>>[0-9]*|>', '', text).lower()
        text = re.sub(r'\(op\)|\(you\)', '', text)
        text = re.sub(r'&gt;', ' ', text).strip()

        return text
