from src.domain.MText import MText
from src.generator.AbstractGenerator import AbstractGenerator


class MarkovifyGenerator(AbstractGenerator):

    def init_model(self, texts):
        import markovify
        model = markovify.Text(
            '\n'.join(map(lambda text: text.payload, texts)))
        return model

    def generate(self, model, start_sentence, n):
        if start_sentence is None:
            for _ in range(n):
                yield MText(model.make_sentence())
        else:
            safety_counter = self.SAFETY_COUNTER + n
            while True:
                safety_counter -= 1

                sentence = model.make_sentence()
                if sentence is not None and start_sentence in sentence:
                    n -= 1
                    yield MText(sentence)

                if n <= 0 or safety_counter <= 0:
                    break
