import src.scraper.AbstractScraper as AbstractScraper
import src.Logger as Logger
import src.Text as Text
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
        return self.__make_text(self.__get_board_posts(self.__get_thread_urls(self.n_pages)))

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
            posts.append(this_post)

        return posts

    def __get_board_posts(self, thread_urls):
        board_posts = []
        for url in thread_urls:
            board_posts += self.get_thread_posts(url)
        return board_posts

    # remove quotes, unnecessary punctuation, etc
    def __format_text(self, board_posts):
        result = []

        for text in board_posts:
            text = re.sub(r'>>[0-9]*|>', '', text).lower()
            text = re.sub(r'\(op\)|\(you\)', '', text)
            text = re.sub(r'&gt;', ' ', text).strip()
            result.append(Text(text))

        return result
