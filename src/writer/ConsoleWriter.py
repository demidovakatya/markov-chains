from src.writer.AbstractOutputWriter import AbstractOutputWriter


class ConsoleWriter(AbstractOutputWriter):
    def write(self, m_text):
        print(m_text, '\n')
