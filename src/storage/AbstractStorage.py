from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def store(self, text, group_name):
        pass

    @abstractmethod
    def get(self, group_name):
        pass
