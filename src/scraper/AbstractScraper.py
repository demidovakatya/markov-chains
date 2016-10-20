import re
import urllib.request
from http.client import IncompleteRead
import string

from abc import ABC, abstractmethod

from bs4 import BeautifulSoup


class AbstractScraper(ABC):

    def __init__(self, source):
        self.source = source

    @abstractmethod
    def execute(self):
        pass

    def beautify(self, text):
        
        # remove urls
        regex_url = re.compile(r'https?://[^\s]*')
        text = regex_url.sub(' ', text)

        # remove specific shit     
        text = re.sub(r'>>[0-9]*|\(OP\)|\(YOU\)', '', text)
        text = re.sub(r'&gt;|\s+', '', text)

        # remove punctuation
        punct = ''.join([p for p in string.punctuation if p not in ('.,-?')])
        regex_punct = re.compile('[%s]' % re.escape(punctuation))
        text = regex_punct.sub(' ', text)

        # remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        # lower
        text = text.lower()

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
