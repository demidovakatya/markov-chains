from src.scraper.Scrapers import Scrapers
from src.storage.TextFileStorage import TextFileStorage
from src.storage.BinaryFileStorage import BinaryFileStorage
from src.writer.ConsoleWriter import ConsoleWriter
from src.generator.Generators import Generators


class MCApplication:
    def run(self, config):
        # init
        # storage = TextFileStorage(config['storage_path'])
        storage = BinaryFileStorage(config['storage_path'])
        scrapers = Scrapers().make(config['scrapers'])
        generator = Generators().make(config['generator'])
        output = ConsoleWriter()

        # parse and store
        for scraper in scrapers:
            storage.store(scraper.source, scraper.execute())

        # get from storage
        texts = storage.get(map(lambda sc: sc.source, scrapers))

        # run through mc and display
        model = generator.init_model(texts)
        for m_text in generator.generate(model, config['output_size']):
            output.write(m_text)
