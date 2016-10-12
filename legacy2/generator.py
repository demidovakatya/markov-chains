def create_mc(text):
    from pymarkovchain import MarkovChain
    model = MarkovChain()
    model.generateDatabase(text, '\n')
    return model

def create_mvf(text):
    import markovify
    model = markovify.Text(text)
    return model
    
def generate_sentences_mc(text, n = 50):
    from pymarkovchain import MarkovChain
    model = create_mc(text)
    for _ in range(n):
        print(model.generateString(), '\n')

def generate_sentences_mvf(text, n = 50):
    import markovify
    model = markovify.Text(text)
    for _ in range(n):
        print(model.make_sentence(), '\n')

def generate_from_model(model):
    if str(type(model)) == "<class 'markovify.text.Text'>":
        # print('markovify')
        return model.make_sentence()
    elif str(type(model)) == "<class 'pymarkovchain.MarkovChain.MarkovChain'>":
        # print('MarkovChain')
        return model.generateString()

def generate(model, n = 50):
    for _ in range(n):
        print(generate_from_model(model), '\n')