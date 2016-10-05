from abc import ABC, abstractmethod


class AbstractScraper(ABC):
    @abstractmethod
    def execute(self):
        pass
