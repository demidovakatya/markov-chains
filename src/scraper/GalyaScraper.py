import logging
import re
from urllib.parse import urljoin

from src.domain.Text import Text
from src.scraper.AbstractScraper import AbstractScraper


class GalyaScraper(AbstractScraper):
    INDEX = 'http://galya.ru'
    ENCODING = 'windows-1251'

    def __init__(self, n_pages=1):

        super(GalyaScraper, self).__init__('galya.ru')
        self.n_pages = n_pages

    def execute(self):

        for thread_url in self.__get_threads_urls(self.n_pages):
            for text in self.__get_thread_posts(thread_url):
                yield text

    def __make_thread_url(self, page):

        n = page * 115
        rel_url = '/clubs/index.php?dlimit={}&p=1&board_id=0&ltype=0'.format(n)
        return urljoin(self.INDEX, rel_url)

    def __get_threads_urls(self, n_pages):

        for page in range(0, n_pages):
            url = self.__make_thread_url(page)
            logging.info('Reading %s...' % url)

            soup = self.init_soup(self.get_page_content(url, self.ENCODING))
            links = soup.findAll(attrs={'title': 'дата последнего комментария'})
            for link in links:
                yield self.DOMAIN + '/clubs/' + re.sub('&.*', '', link.get('href'))

    def __get_thread_posts(self, url):
        
        soup = self.init_soup(self.get_page_content(url, self.ENCODING))

        for hit in soup.findAll(attrs={'class': 'text'}):
            payload = self.beautify(hit.get_text(separator=' '))
            
            if payload != '':
                text = Text(self.source, self.beautify(payload), url)
                logging.debug(text)
                yield text
