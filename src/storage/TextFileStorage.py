from src.storage.AbstractStorage import AbstractStorage
from src.utils.Logger import Logger


class TextFileStorage(AbstractStorage):
    LOG = Logger()

    def __init__(self, base_dir):
        self.base_dir = base_dir

    def store(self, text, group_name):
        with open(self.base_dir + '/' + group_name, 'w') as txt_file:
            txt_file.write('\n'.join(text.payload))

        self.LOG.info('Successfully saved %s posts to: %s/%s' % (len(text), self.base_dir, self.group_name))

    def get(self, group_name):
        pass
