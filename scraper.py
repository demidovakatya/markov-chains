import re
import urllib.request
from bs4 import BeautifulSoup

def get_thread_urls(board = 'b', n_pages = 5):
    '''
    Goes to `board`'s first `n_pages` pages and gets links to threads.
    Returns a list of links to threads from the given `board`.
    '''
    domain = 'http://2ch.hk'
    thread_urls = []

    for page in range(1, n_pages + 1):
        url = domain + '/' + board + '/' + str(page) + '.html'
        print('Reading %s...' % url)
        with urllib.request.urlopen(url) as response:
           html = response.read()

        soup = BeautifulSoup(html, 'lxml')
        thread_urls += [domain + a.get('href') for a 
                    in soup.findAll(attrs = {'class': 'orange'})]

    print('Found: %s urls' % len(thread_urls))
    return thread_urls
    

def get_posts_from_thread(url):
    '''
    Gets all text messages in the `url` thread.
    Returns a list of strings.
    '''

    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'lxml')

    posts = []
    for hit in soup.findAll(attrs={'class' : 'post-message'}):
        this_post = hit.get_text(separator = ' ')
        # remove quotes, unnecessary punctuation, etc
        this_post = re.sub(r'>>[0-9]*|\(OP\)|>', '', this_post)
        this_post = re.sub(r'&gt;', ' ', this_post).strip()

        # print(this_post)
        posts.append(this_post)

    print('Found: %s posts' % len(posts))
    return posts

def make_text_from_posts(board = 'b', save_to_txt = True):
    thread_urls = get_thread_urls(board)

    threads = []
    for url in thread_urls:
        threads.append(get_posts_from_thread(url))

    text = '\n'.join(['\n'.join(thread) for thread in threads])

    if save_to_txt:
        filename = board + '_posts_' + text[:10] + '.txt'
        with open(filename, 'w') as txt_file:
            txt_file.write(text)
        print('Successfully saved bullshit to: %s\n' % filename)

# ============================================================

from pymarkovchain import MarkovChain

# import scraper

text = make_text_from_posts()

def create_mc(text = text):
    mc = MarkovChain()
    mc.generateDatabase(text, '\n')
    return mc

def generate_strings(mc, n_strings = 50):
    for _ in range(n_strings): 
        print(mc.generateString())

mc = create_mc()
generate_strings(mc = mc)