from src.writer.AbstractOutputWriter import AbstractOutputWriter


class ConsoleWriter(AbstractOutputWriter):
    def write(self, m_text):
        print("> " + str(m_text), '\n')
