from abc import ABC, abstractmethod


class AbstractGenerator(ABC):
    SAFETY_COUNTER = 10000

    @abstractmethod
    def init_model(self, texts):
        pass

    @abstractmethod
    def generate(self, texts, start_sentence, n):
        pass
