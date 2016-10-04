import os, re
import generator, core

text = core.read_txt_files()
text = core.beautify(text)

# Markovify
mvf = generator.create_mvf(text)
generator.generate(mvf)

# pymarkovchain
mch = generator.create_mc(text)
generator.generate(mch)
