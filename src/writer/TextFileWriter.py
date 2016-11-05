import os
from time import gmtime, strftime

from src.writer.AbstractOutputWriter import AbstractOutputWriter


class TextFileWriter(AbstractOutputWriter):
    counter = 0

    def __init__(self, storage_path):
        self.storage_path = os.path.join(storage_path, 'output')

    def write(self, m_text):
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

        self.counter += 1

        date_time = strftime("%Y-%m-%d_%H:%M", gmtime())
        file_name = os.path.join(self.storage_path, 
                                 'file_{}.txt'.format(date_time))

        with open(file_name, 'a', encoding='utf8') as file:
            file.write(str(m_text) + '\n')
