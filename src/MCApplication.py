from src.scraper.GalyaScraper import GalyaScraper
import logging.config

logging.config.fileConfig('../logging.conf')


class MCApplication:
    def run(self):
        # print(BScraper('b', 1).execute())
        # print(RUWomanScraper(1, 1).execute())
        print(GalyaScraper(1).execute())
        # print(KrovostokScraper().execute())


MCApplication().run()
