import re
text = re.sub('\n\n', '\n', open('butthurts.txt').read())

from pymarkovchain import MarkovChain
mc = MarkovChain(".")
mc.generateDatabase(text, '\n')

mc.generateString()
