import markovify
from pymarkovchain import MarkovChain
from src.MText import MText


class Generator:
    def create_mc(self, text):
        model = MarkovChain()
        model.generateDatabase(text, '\n')
        return model

    def create_mvf(self, text):
        model = markovify.Text(text)
        return model

    def generate_sentences_mc(self, text, n=50):
        model = self.create_mc(text)
        for _ in range(n):
            yield model.generateString()

    def generate_sentences_mvf(self, text, n=50):
        model = markovify.Text(text)
        for _ in range(n):
            yield model.make_sentence()

    def generate_from_model(self, model):
        if str(type(model)) == "<class 'markovify.text.Text'>":
            return model.make_sentence()
        elif str(type(model)) == "<class 'pymarkovchain.MarkovChain.MarkovChain'>":
            return model.generateString()

    def generate(self, model, n=50):
        for _ in range(n):
             yield self.generate_from_model(model)
