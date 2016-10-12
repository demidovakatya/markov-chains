from src.generator.MarkovifyGenerator import MarkovifyGenerator
from src.generator.PyMarkovChainGenerator import PyMarkovChainGenerator


class Generators:

    def make(self, generator):
        if generator == 'mc':
            return PyMarkovChainGenerator()
        elif generator == 'mvf':
            return MarkovifyGenerator()
        else:
            raise Exception('Not existing generator: %s!' % generator)
