import re
from urllib.request import urlopen
import string

from abc import ABC, abstractmethod
from http.client import IncompleteRead

from bs4 import BeautifulSoup as bs


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
        text = re.sub(r'>>[0-9]*|\(OP\)|\(YOU\)', ' ', text)
        text = re.sub(r'&gt;', ' ', text)

        # remove punctuation
        punct = ''.join([p for p in string.punctuation if p not in ('.,-?')])
        regex_punct = re.compile('[%s]' % re.escape(punct))
        text = regex_punct.sub(' ', text)

        # replace ё with е
        text = re.sub('ё', 'е', text)

        # remove extra periods (........ -> ...)
        text = re.sub(r'(\.){3,}', '... ', text).strip()

        # add missing spaces (after ?/!)
        # text = re.sub(r'\?\S', '? ', text).strip()
        # text = re.sub(r'!\S', '! ', text).strip()

        # remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()

        # lower
        text = text.lower()

        return text


    def get_page_content(self, url, encoding='utf8'):
        try:
            with urlopen(url) as response:
                html = response.read().decode(encoding)
        except IncompleteRead as e:
            html = e.partial

        return html


    def init_soup(self, html, lib='lxml'):
        return bs(html, lib)
