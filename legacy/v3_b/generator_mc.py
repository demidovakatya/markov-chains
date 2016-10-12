import re
from pymarkovchain import MarkovChain
import scraper

def create_mc(text):
    mc = MarkovChain()
    mc.generateDatabase(text, '\n')
    return mc

def generate_strings(mc, n_strings = 50):
    for _ in range(n_strings): 
        print(mc.generateString(), '\n')


text = scraper.make_text_from_posts()

mc = create_mc(text)
generate_strings(mc)