from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @abstractmethod
    def store(self, source, texts):
        pass

    @abstractmethod
    def get(self, sources):
        pass
