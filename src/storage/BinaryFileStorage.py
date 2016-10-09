from src.storage.AbstractStorage import AbstractStorage
import pickle
import os
import logging
from src.Util import argument_to_list


class BinaryFileStorage(AbstractStorage):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def store(self, source, texts):
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

        with open(self.base_dir + '/' + source + '.bin', 'wb') as file:
            logging.debug("Writing to file: %s" % file)
            pickle.dump(texts, file)

    def get(self, sources):
        texts = []

        for source in argument_to_list(sources):
            with open(self.base_dir + '/' + source + '.bin', 'rb') as file:
                logging.debug("Reading file: %s" % file)
                texts += pickle.load(file)

        return texts
