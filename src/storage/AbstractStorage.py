from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def store(self, text):
        pass

    @abstractmethod
    def get(self, source):
        pass
