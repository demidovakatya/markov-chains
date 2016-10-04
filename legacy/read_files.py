import os
import scraper

TXT_DIR = 'posts'
files = os.listdir(TXT_DIR)

posts = []
for file in files:
    h = open('/'.join([TXT_DIR, file]), 'rb')
    for line in h.readlines():
        posts.append(line.decode('utf8').strip())

import markovify

def generate_sentences(text_model, n = 50):
    # filename = 'markovify_generated_b.txt'
    for _ in range(n): 
        sentence = text_model.make_sentence()
        print(sentence, '\n')
        # try:
            # open(filename, 'a').write(sentence, '\n')
        # except TypeError:
            # pass

text = scraper.make_text(posts)
text_model = markovify.Text(text)
generate_sentences(text_model)