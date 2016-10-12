import os
from time import gmtime, strftime

from src.writer.AbstractOutputWriter import AbstractOutputWriter


class TextFileWriter(AbstractOutputWriter):
    counter = 0

    def __init__(self, storage_path):
        self.storage_path = storage_path + '/output/'

    def write(self, m_text):
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

        self.counter += 1

        file_name = self.storage_path + '/file_' + \
            strftime("%Y-%m-%d_%H:%M", gmtime()) + '.txt'

        with open(file_name, 'a', encoding='utf8') as file:
            file.write(str(self.counter) + ". -> " + str(m_text) + '\n')
