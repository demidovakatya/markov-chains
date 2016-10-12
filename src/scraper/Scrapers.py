from src.scraper.BScraper import BScraper
from src.scraper.GalyaScraper import GalyaScraper
from src.scraper.KrovostokScraper import KrovostokScraper
from src.scraper.RUWomanScraper import RUWomanScraper
import collections


class Scrapers:

    def make(self, scrapers):
        result = []

        if not isinstance(scrapers, collections.Iterable):
            scrapers = [scrapers]

        for scraper in scrapers:
            result.append(self.__get_instance(scraper))

        return result

    def __get_instance(self, scraper):
        if scraper == 'b':
            return BScraper()
        elif scraper == 'galya.ru':
            return GalyaScraper()
        elif scraper == 'krovostok':
            return KrovostokScraper()
        elif scraper == 'woman.ru':
            return RUWomanScraper()
