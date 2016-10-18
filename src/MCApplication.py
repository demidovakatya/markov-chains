from src.generator.Generators import Generators
from src.scraper.Scrapers import Scrapers
from src.storage.BinaryFileStorage import BinaryFileStorage
from src.writer.Writers import Writers


class MCApplication:

    def __init__(self, config):
        self.storage = BinaryFileStorage(config['storage_path'])
        self.scrapers = Scrapers().make(config['scrapers'])
        self.generator = Generators().make(config['generator'])
        self.writer = Writers().make(config['writer'], config['storage_path'])
        self.mode = config['mode']
        self.output_size = config['output_size']

    def run(self):
        if self.mode == 'parse':
            self.__parse_and_store()
        elif self.mode == 'generate':
            self.__get_and_generate()
        elif self.mode == 'all':
            self.__parse_and_store()
            self.__get_and_generate()
        else:
            raise Exception('Unsupported mode: %s!' % self.mode)

    def __parse_and_store(self):
        for scraper in self.scrapers:
            self.storage.store(scraper.source, list(scraper.execute()))

    def __get_and_generate(self):
        texts = self.storage.get(map(lambda sc: sc.source, self.scrapers))
        model = self.generator.init_model(texts)
        for m_text in self.generator.generate(model, self.output_size):
            self.writer.write(m_text)
