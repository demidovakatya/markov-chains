from src.Util import argument_to_list
from src.scraper.GalyaScraper import GalyaScraper
from src.scraper.BScraper import BScraper
from src.scraper.KrovostokScraper import KrovostokScraper
from src.scraper.RUWomanScraper import RUWomanScraper


class Scrapers:
    def make(self, scrapers):
        result = []

        for scraper in argument_to_list(scrapers):
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
