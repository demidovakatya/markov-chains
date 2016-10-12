import re
from abc import ABC, abstractmethod


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
