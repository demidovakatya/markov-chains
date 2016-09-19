from bs4 import BeautifulSoup
from pymarkovchain import MarkovChain

url = 'v1_butthurts/butthurt_thread.html'
html = open(url).read()
soup = BeautifulSoup(html)

posts = []
for hit in soup.findAll(attrs={'class' : 'post-message'}):
    this_post = hit.get_text(separator = ' ')
    # remove quotes, unnecessary punctuation, etc
    this_post = re.sub(r'>>[0-9]*|\(OP\)|>', '', this_post).strip()
    this_post = re.sub(r'&gt;', ' ', this_post).strip()

    print(this_post)
    posts.append(this_post)

text = '\n'.join(posts)

# Test
mc = MarkovChain()
mc.generateDatabase(text, '\n')
for _ in range(50): 
    print(mc.generateString())
