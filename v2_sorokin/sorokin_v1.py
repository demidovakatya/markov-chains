import re
import os
from bs4 import BeautifulSoup

files = [n for n in os.listdir() if n.endswith('.html')]
files = files[1:]

text = ''
for f in files:
    html = open(f).read()
    soup = BeautifulSoup(html, 'lxml')

    for hit in soup.findAll(attrs={'class' : 'post_comment_body'}):
        this_text = re.sub(r'<.+>', ' ', hit.prettify())
        this_text = re.sub(r'&gt;&gt;[0-9]+', ' ', this_text)
        this_text = re.sub(r'["\';&]', ' ', this_text)
        this_text = re.sub(r'\s+', ' ', this_text)
        text += ' '
        text += this_text.strip().lower()


from pymarkovchain import MarkovChain
mc = MarkovChain(".")
mc.generateDatabase(text)

mc.generateString()
