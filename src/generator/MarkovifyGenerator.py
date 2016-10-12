from src.domain.MText import MText
from src.generator.AbstractGenerator import AbstractGenerator


class MarkovifyGenerator(AbstractGenerator):

    def init_model(self, texts):
        import markovify
        model = markovify.Text(
            '\n'.join(map(lambda text: text.payload, texts)))
        return model

    def generate(self, model, n):
        for _ in range(n):
            yield MText(model.make_sentence())
