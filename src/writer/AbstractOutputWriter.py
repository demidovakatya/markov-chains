from abc import ABC, abstractmethod


class AbstractOutputWriter(ABC):

    @abstractmethod
    def write(self, m_text):
        pass
