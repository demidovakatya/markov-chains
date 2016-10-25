import collections

from src.scraper.BScraper import BScraper
from src.scraper.GalyaScraper import GalyaScraper
from src.scraper.KrovostokScraper import KrovostokScraper
from src.scraper.RUWomanScraper import RUWomanScraper


class Scrapers:

    def make(self, scrapers):
        if not isinstance(scrapers, collections.Iterable):
            scrapers = [scrapers]

        result = [self.__get_instance(scraper) for scraper in scrapers]
        return result

    def __get_instance(self, scraper):
        scrapers_dict = {
            'b': BScraper(),
            'galya.ru': GalyaScraper(),
            'krovostok': KrovostokScraper(),
            'woman.ru': RUWomanScraper()}

        return scrapers_dict.get(scraper, None)
