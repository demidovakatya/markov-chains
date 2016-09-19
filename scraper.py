import urllib.request
from bs4 import BeautifulSoup
from pymarkovchain import MarkovChain

# board_url = 'http://2ch.hk/b/'

def get_thread_urls(board = 'b'):
    domain = 'http://2ch.hk'
    board_url = domain + '/' + board + '/'
    with urllib.request.urlopen(board_url) as response:
       board_html = response.read()

    board_soup = BeautifulSoup(board_html, 'lxml')
    thread_urls = [domain + a.get('href') for a 
                in board_soup.findAll(attrs = {'class': 'orange'})]

    return thread_urls
    
def get_posts_from_thread(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'lxml')

    posts = []
    for hit in soup.findAll(attrs={'class' : 'post-message'}):
        this_post = hit.get_text(separator = ' ')
        # remove quotes, unnecessary punctuation, etc
        this_post = re.sub(r'>>[0-9]*|\(OP\)|>', '', this_post).strip()
        this_post = re.sub(r'&gt;', ' ', this_post).strip()

        # print(this_post)
        posts.append(this_post)

    return posts

# -------------------------------------------------

thread_urls = get_thread_urls()

threads = []
for url in thread_urls:
    threads.append(get_posts_from_thread(url))

text = '\n'.join(['\n'.join(thread) for thread in threads])


def create_mc(text = text):
    mc = MarkovChain()
    mc.generateDatabase(text, '\n')
    return mc

def generate_strings(mc, n_strings = 50):
    for _ in range(n_strings): 
        print(mc.generateString())

mc = create_mc()
generate_strings(mc)