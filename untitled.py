import os
import markovify
import scraper

text = scraper.make_text_from_posts()

# txt_files = [f for f in os.listdir() if f.startswith('b_')]
# text = ''

# for txt_file in txt_files:
#     with open(txt_file) as f:
#         text += f.read().lower()

text_model = markovify.Text(text)

for _ in range(25): print(text_model.make_sentence())
