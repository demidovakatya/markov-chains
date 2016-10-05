from abc import ABC, abstractmethod


class AbstractOutputWriter(ABC):
    @abstractmethod
    def output(self, text):
        pass
