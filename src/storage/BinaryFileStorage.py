import logging
import os
import pickle
import collections

from src.storage.AbstractStorage import AbstractStorage


class BinaryFileStorage(AbstractStorage):

    def __init__(self, base_dir):
        self.base_dir = base_dir

    def store(self, source, texts):
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

        file_name = os.path.join(self.base_dir, '{}.bin'.format(source))

        with open(file_name, 'wb') as file:
            logging.info("Writing to file: {}".format(file))
            pickle.dump(texts, file)

        logging.info('Successfully saved {} posts to: {}/{}'.format(len(texts), 
                                                        self.base_dir, source))

    def get(self, sources):
        texts = []

        if not isinstance(sources, collections.Iterable):
            sources = [sources]

        for source in sources:
            file_name = os.path.join(self.base_dir, '{}.bin'.format(source))
            
            with open(file_name, 'rb') as file:
                logging.info("Reading file: {}".format(file))
                texts += pickle.load(file)

        return texts
