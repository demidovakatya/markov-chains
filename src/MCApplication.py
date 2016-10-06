from src.scraper.GalyaScraper import GalyaScraper
from src.scraper.BScraper import BScraper
from src.scraper.KrovostokScraper import KrovostokScraper
from src.storage.TextFileStorage import TextFileStorage
from src.Text import Text
from src.MText import MText
from src.Generator import Generator
from src.writer.ConsoleWriter import ConsoleWriter
import logging.config

logging.config.fileConfig('../logging.conf')


class MCApplication:
    TXT_DIR = '../txt'

    def run(self):
        # init
        storage = TextFileStorage(self.TXT_DIR)
        scraper = KrovostokScraper()
        output = ConsoleWriter()

        # parse
        texts = scraper.execute()

        # store
        storage.store(texts)

        # get from storage
        texts = []
        for text in storage.get(scraper.source):
            texts.append(text.payload)

        # Markovify
        # mvf = generator.create_mvf('\n'.join(texts))
        # for m_text in generator.generate(mvf):
        #     output.write(m_text)

        # pymarkovchain
        mch = Generator.create_mc('\n'.join(texts))
        for m_text in Generator.generate(mch):
            output.write(m_text)


MCApplication().run()
