import markovify
from pymarkovchain import MarkovChain


with open('krovostok_lyrics.txt', 'r') as txt_file:
        lyrics = [lr for lr in txt_file.read().split('\n') if lr != '']

text = '\n'.join(lyrics)


text_model = markovify.Text(text)
def generate_sentences(text_model, n = 50):
    # filename = 'markovify_generated_krovosrok.txt'
    for _ in range(n):
        sentence = text_model.make_sentence()
        print(sentence, '\n')
        # try:
        #     open(filename, 'a').write(sentence, '\n')
        # except TypeError:
        #     pass


def create_mc(text):
    mc = MarkovChain()
    mc.generateDatabase(text, '\n')
    return mc
def generate_strings(mc, n_strings = 50):
    for _ in range(n_strings):
        print(mc.generateString(), '\n')
mc = create_mc(text)
generate_strings(mc)
