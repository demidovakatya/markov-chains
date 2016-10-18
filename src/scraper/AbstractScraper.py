import re
import urllib.request
from http.client import IncompleteRead
from abc import ABC, abstractmethod

from bs4 import BeautifulSoup


class AbstractScraper(ABC):
    def __init__(self, source):
        self.source = source

    @abstractmethod
    def execute(self):
        pass

    def beautify(self, text):
        # text = text.lower()
        # remove urls
        text = re.sub(
            '(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),#]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', '', text)
        # remove quotes, unnecessary punctuation, etc
        text = re.sub(r'>>[0-9]*|>', '', text)
        text = re.sub(r'<+', ' ', text)
        text = re.sub(r'\.{2,}', '. ', text)
        text = re.sub(r'[\(|\)]{2,}', ' ', text)
        text = re.sub(r'\(OP\)|\(YOU\)', '', text)
        text = re.sub(r'&gt;', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def get_page_content(self, url, encoding='utf8'):
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read().decode(encoding)
        except IncompleteRead as e:
            html = e.partial

        return html

    def init_soup(self, html, lib='html5lib'):
        return BeautifulSoup(html, lib)
