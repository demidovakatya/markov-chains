from src.generator.AbstractGenerator import AbstractGenerator
from src.MText import MText


class MarkovifyGenerator(AbstractGenerator):
    def init_model(self, texts):
        import markovify
        model = markovify.Text('\n'.join(map(lambda text: text.payload, texts)))
        return model

    def generate(self, model, n):
        for _ in range(n):
            yield MText(model.make_sentence())
