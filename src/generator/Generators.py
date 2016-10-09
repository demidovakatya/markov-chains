from src.generator.PyMarkovChainGenerator import PyMarkovChainGenerator
from src.generator.MarkovifyGenerator import MarkovifyGenerator


class Generators:
    def make(self, generator):
        if generator == 'mc':
            return PyMarkovChainGenerator()
        elif generator == 'mvf':
            return MarkovifyGenerator()
