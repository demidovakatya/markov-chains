from src.MText import MText


class Generator:
    def create_mc(text):
        from pymarkovchain import MarkovChain
        model = MarkovChain()
        model.generateDatabase(text, '\n')
        return model

    def create_mvf(text):
        import markovify
        model = markovify.Text(text)
        return model

    def generate_sentences_mc(text, n=50):
        model = Generator.create_mc(text)
        for _ in range(n):
            yield MText(model.generateString())

    def generate_sentences_mvf(text, n=50):
        import markovify
        model = markovify.Text(text)
        for _ in range(n):
            yield MText(model.make_sentence())

    def generate_from_model(model):
        if str(type(model)) == "<class 'markovify.text.Text'>":
            # print('markovify')
            return model.make_sentence()
        elif str(type(model)) == "<class 'pymarkovchain.MarkovChain.MarkovChain'>":
            # print('MarkovChain')
            return model.generateString()

    def generate(model, n=50):
        for _ in range(n):
            yield MText(Generator.generate_from_model(model))
