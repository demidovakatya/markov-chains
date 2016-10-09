import urllib.request

from bs4 import BeautifulSoup

from src.Text import Text
from src.scraper.AbstractScraper import AbstractScraper
import logging


class RUWomanScraper(AbstractScraper):
    BASE_URL = 'http://www.woman.ru'
    BASE_FORUM_URL = BASE_URL + '/forum/'

    def __init__(self, n_pages=5, n_pages_per_thread=-1):
        super(RUWomanScraper, self).__init__('woman.ru')
        self.n_pages = n_pages
        self.n_pages_per_thread = n_pages_per_thread

    def execute(self):
        result = []
        for thread_url in self.__get_all_thread_links(self.n_pages, self.n_pages_per_thread):
            result += self.__parse_thread(self.__get_page_content(thread_url), thread_url)

        return result

    def __get_page_content(self, url):
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf8')

        return html

    def __get_pagination_links(self, url, n_pages=-1):
        result = []
        first_page = 1
        last_page = n_pages
        if n_pages == -1:
            last_page = self.__get_last_page(self.__get_page_content(url))

        for page in range(first_page, last_page + 1):
            result.append(url + str(page))

        return result

    def __get_last_page(self, html):
        soup = BeautifulSoup(html, 'html5lib')

        try:
            return int(soup.find("li", attrs={'class': 'last'}).get_text())
        except ValueError:
            try:
                return int(soup.find_all("li", attrs={'class': 'page'})[-1].get_text())
            except IndexError:
                return 1

    def __get_thread_links(self, url):
        result = []
        html = self.__get_page_content(url)
        soup = BeautifulSoup(html, 'html5lib')

        for link in soup.find(attrs={'class': 'all-topics'}):
            url = link.find("a")
            if (url != None and url != -1):
                result.append(self.BASE_URL + url.get("href"))

        return result

    def __get_all_thread_links(self, n_pages, n_pages_per_thread):
        result = []
        forum_pagination_links = self.__get_pagination_links(self.BASE_FORUM_URL, n_pages)

        for forum_page_link in forum_pagination_links:
            logging.info('Reading %s...' % forum_page_link)

            thread_links = self.__get_thread_links(forum_page_link)

            logging.info('Found: %s threads.' % len(thread_links))

            for thread_link in thread_links:
                thread_pagination_links = self.__get_pagination_links(thread_link, n_pages_per_thread)
                for thread_page_link in thread_pagination_links:
                    result.append(thread_page_link)

        return result

    def __parse_thread(self, html, url):
        result = []
        soup = BeautifulSoup(html, 'html5lib')

        for comment in soup.find_all('div', attrs={'class': 'text'}):
            reply = comment.find("div", attrs={'class': 'reply'})
            if (reply != None):
                reply.extract()
            text = Text(self.source, self.beautify(comment.get_text()), url)
            logging.debug(text)
            result.append(text)

        return result
