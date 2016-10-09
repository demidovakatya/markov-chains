from src.storage.AbstractStorage import AbstractStorage
from src.Text import Text
from src.Util import argument_to_list
import logging
import os
import re


class TextFileStorage(AbstractStorage):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def store(self, source, texts):
        texts = argument_to_list(texts)
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        with open(self.base_dir + '/' + source + '.txt', 'w', encoding='utf8') as file:
            logging.debug("Writing to file %s" % file)
            for text in texts:
                text = self.__serialize(text)
                logging.debug("Writing: %s" % text)
                file.write(text + '\n')

        logging.debug('Successfully saved %s posts to: %s/%s' % (len(texts), self.base_dir, source))

    def get(self, sources):
        texts = []

        for source in argument_to_list(sources):
            for file in self.__get_paths_to_txt(source):
                logging.debug("Reading file: %s" % file)
                fragments = [self.__deserialize(f) for f in open(file, encoding='utf8').read().split('\n')]
                fragments = [f for f in fragments if f != '']
                texts += fragments

        return texts

    def __deserialize(self, text):
        m = re.search('\[S_\](.*)\[_S\]\[U_\](.*)\[_U\]\[P_\](.*)\[_P\]', text.strip(), re.U)
        if m:
            return Text(m.group(1), m.group(3), m.group(2))
        else:
            return ''

    def __serialize(self, text):
        return "[S_]%s[_S][U_]%s[_U][P_]%s[_P]" % (text.source, text.url, text.payload)

    def __get_paths_to_txt(self, source):
        # files = []
        # dir = self.base_dir + '/' + source
        #
        # for txt_item in os.listdir(dir):
        #     if txt_item.endswith('.txt'):
        #         files.append(os.path.join(dir, txt_item))
        #     if os.path.isdir(os.path.join(dir, txt_item)):
        #         for item in os.listdir(os.path.join(dir, txt_item)):
        #             if item.endswith('.txt'):
        #                 files.append(os.path.join(dir, txt_item, item))
        # return files
        return [self.base_dir + '/' + source + '.txt']
