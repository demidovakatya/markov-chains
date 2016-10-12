from src.domain.MText import MText
from src.generator.AbstractGenerator import AbstractGenerator


class PyMarkovChainGenerator(AbstractGenerator):

    def init_model(self, texts):
        from pymarkovchain import MarkovChain
        model = MarkovChain()
        model.generateDatabase(
            '\n'.join(map(lambda text: text.payload, texts)), '\n')

        return model

    def generate(self, model, n):
        for _ in range(n):
            yield MText(model.generateString())
