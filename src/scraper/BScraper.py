import logging

from src.domain.Text import Text
from src.scraper.AbstractScraper import AbstractScraper


class BScraper(AbstractScraper):
    INDEX = 'http://2ch.hk'

    def __init__(self, board='b', n_pages=5):
        super(BScraper, self).__init__('2ch')
        self.board = board
        self.n_pages = n_pages

    def execute(self):
        for thread_url in self.__get_thread_urls(self.n_pages):
            for text in self.__get_thread_posts(thread_url):
                yield text

    def __make_thread_url(self, page):
        return self.INDEX + '/' + self.board + '/' + str(page) + '.html'

    def __get_thread_urls(self, n_pages):
        for page in range(1, n_pages + 1):
            url = self.__make_thread_url(page)
            logging.info('Reading %s...' % url)

            soup = self.init_soup(self.get_page_content(url))
            
            for link in soup.findAll(attrs={'class': 'orange'}):
                yield self.INDEX + link.get('href')

    def __get_thread_posts(self, url):        
        soup = self.init_soup(self.get_page_content(url))
        for hit in soup.findAll(attrs={'class': 'post-message'}):
            payload = self.beautify(hit.get_text(separator=' '))

            if payload != '':
                text = Text(self.source, payload, url)
                logging.debug(text)
                yield text
