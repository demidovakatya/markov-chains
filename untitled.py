import markovify
from pymarkovchain import MarkovChain
import os
import re

B_DIR = 'threads'
KROVOSTOK_LYRICS_FILE = 'krovostok_lyrics.txt'

b_text = ''
b_files = [f for f in os.listdir(B_DIR) if f.endswith('.txt')]
for b_file in b_files:
    with open('/'.join([B_DIR, b_file]), 'r') as txt_file:
        b_text += txt_file.read()
        b_text += '\n'

with open(KROVOSTOK_LYRICS_FILE, 'r') as txt_file:
        krovostok_text = txt_file.read()

text = b_text + krovostok_text
text = re.sub('>>[0-9]+|\(OP\)|>', ' ', text)
text = re.sub('[\t ]+', ' ', text)

# Markovify
def generate_sentences(text_model, n = 50):
    for _ in range(n):
        sentence = text_model.make_sentence()
        print(sentence, '\n')
text_model = markovify.Text(text)
generate_sentences(text_model)

# pymarkovchain
def create_mc(text):
    mc = MarkovChain()
    mc.generateDatabase(text, '\n')
    return mc
def generate_strings(mc, n_strings = 50):
    for _ in range(n_strings):
        print(mc.generateString(), '\n')
mc = create_mc(text)
generate_strings(mc)
