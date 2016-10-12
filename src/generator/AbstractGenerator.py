from abc import ABC, abstractmethod


class AbstractGenerator(ABC):

    @abstractmethod
    def init_model(self, texts):
        pass

    @abstractmethod
    def generate(self, texts, n):
        pass
