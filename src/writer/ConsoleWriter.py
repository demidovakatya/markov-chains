from src.writer.AbstractOutputWriter import AbstractOutputWriter


class ConsoleWriter(AbstractOutputWriter):
    counter = 0

    def write(self, m_text):
        self.counter += 1
        print(str(self.counter) + ". -> " + str(m_text), '\n')
