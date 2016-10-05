import re
import urllib.request
from bs4 import BeautifulSoup

TXT_DIR = './txt/threads'
BOARD = 'b'
DOMAIN = 'http://2ch.hk'
# n_pages = 1

def get_thread_urls(n_pages = 1):
    thread_urls = []
    for page in range(1, n_pages + 1):
        url = DOMAIN + '/' + BOARD + '/' + str(page) + '.html'
        print('Reading %s...' % url)

        with urllib.request.urlopen(url) as response:
           html = response.read()

        soup = BeautifulSoup(html, 'html5lib')
        thread_urls += [DOMAIN + a.get('href') for a
                    in soup.findAll(attrs = {'class': 'orange'})]
    print('Found: %s threads.' % len(thread_urls))

    return thread_urls


def get_thread_posts(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html5lib')

    posts = []
    for hit in soup.findAll(attrs={'class' : 'post-message'}):
        this_post = hit.get_text(separator = ' ')
        posts.append(this_post)

    filename = re.sub('[^0-9]', '', url)[1:] + '.txt'
    with open(TXT_DIR + '/' + filename, 'w') as txt_file:
        txt_file.write('\n'.join(posts))

    print('Successfully saved %s posts to: %s/%s' % (len(posts), TXT_DIR, filename))

    return posts


def get_board_posts(thread_urls):
    board_posts = []
    for url in thread_urls:
        board_posts += get_thread_posts(url)
    return board_posts


def make_text(board_posts):
    text = '\n'.join(board_posts)
    # remove quotes, unnecessary punctuation, etc
    text = re.sub(r'>>[0-9]*|>', '', text).lower()
    text = re.sub(r'\(op\)|\(you\)', '', text)
    text = re.sub(r'&gt;', ' ', text).strip()
    return text


def make_text_board(n_pages = 3):
    return make_text(get_board_posts(get_thread_urls(n_pages)))
