import logging

from urllib.parse import urljoin
from urllib.request import HTTPError

from src.domain.Text import Text
from src.scraper.AbstractScraper import AbstractScraper


class RUWomanScraper(AbstractScraper):
    """RUWomanScraper
    arguments:
        pagelimit    (int): how many forum pages to parse
        thread_limit (int): how many pages in one thread to parse
    """
    INDEX = 'http://www.woman.ru'
    FORUM = INDEX + '/forum/'

    def __init__(self, pagelimit=1, thread_limit=1):
        super(RUWomanScraper, self).__init__('woman.ru')
        self.pagelimit = pagelimit
        self.thread_limit = thread_limit

    def execute(self):
        thread_urls = self.__get_thread_urls(self.pagelimit, self.thread_limit)

        try:
            # for text in self.__get_thread_posts(thread_url):
            #     yield text
            texts = [text for text in self.__get_thread_posts(thread_url)]
        except HTTPError:
            continue

    def __get_thread_urls(self, pagelimit, thread_limit):
        
        for forum_page_link in self.__get_pagination_links(self.FORUM_INDEX, pagelimit):
            logging.info('Reading %s...' % forum_page_link)

            for thread_link in self.__get_thread_links(forum_page_link):
                for thread_page_link in self.__get_pagination_links(thread_link, thread_limit):
                    yield thread_page_link


    def __parse_posts(self, url):
        
        soup = self.init_soup(self.get_page_content(url))
        
        for hit in soup.find_all('div', attrs={'class': 'text'}):
            reply = hit.find("div", attrs={'class': 'reply'})

            if reply is not None:
                reply.extract()
            payload = self.beautify(hit.get_text())

            if payload != '':
                text = Text(self.source, payload, url)
                logging.debug(text)
                yield text


    def __get_pagination_links(self, url, pagelimit=-1):
        first_page = 1
        last_page = pagelimit
        if pagelimit == -1:
            last_page = self.__get_last_page(self.get_page_content(url))

        for page in range(first_page, last_page + 1):
            yield url + str(page)

    def __get_last_page(self, html):
        soup = self.init_soup(html)

        try:
            return int(soup.find("li", attrs={'class': 'last'}).get_text())
        except ValueError:
            try:
                return int(soup.find_all("li", attrs={'class': 'page'})[-1].get_text())
            except IndexError:
                return 1

    def __get_thread_links(self, url):

        soup = self.init_soup(self.get_page_content(url))
        all_topics = soup.find(attrs={'class': 'all-topics'})

        for link in soup.find(attrs={'class': 'all-topics'}):
            url = link.find('a')
            if url is not None and url != -1:
                yield self.INDEX + url.get('')
