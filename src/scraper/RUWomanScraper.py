import logging
from urllib.request import HTTPError

from src.domain.Text import Text
from src.scraper.AbstractScraper import AbstractScraper


class RUWomanScraper(AbstractScraper):
    BASE_URL = 'http://www.woman.ru'
    BASE_FORUM_URL = BASE_URL + '/forum/'

    def __init__(self, n_pages=1, n_pages_per_thread=1):
        super(RUWomanScraper, self).__init__('woman.ru')
        self.n_pages = n_pages
        self.n_pages_per_thread = n_pages_per_thread

    def execute(self):
        for thread_url in self.__get_thread_urls(self.n_pages, self.n_pages_per_thread):
            try:
                for text in self.__get_thread_posts(thread_url):
                    yield text
            except HTTPError:
                continue

    def __get_thread_urls(self, n_pages, n_pages_per_thread):
        for forum_page_link in self.__get_pagination_links(
                self.BASE_FORUM_URL, n_pages):
            logging.info('Reading %s...' % forum_page_link)

            for thread_link in self.__get_thread_links(forum_page_link):
                for thread_page_link in self.__get_pagination_links(
                        thread_link, n_pages_per_thread):
                    yield thread_page_link

    def __get_thread_posts(self, url):
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

    def __get_pagination_links(self, url, n_pages=-1):
        first_page = 1
        last_page = n_pages
        if n_pages == -1:
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
        for link in soup.find(attrs={'class': 'all-topics'}):
            url = link.find("a")
            if url is not None and url != -1:
                yield self.BASE_URL + url.get("href")
