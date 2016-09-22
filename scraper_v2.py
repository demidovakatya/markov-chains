import re
import urllib.request
from bs4 import BeautifulSoup

TXT_DIR = 'posts'
BOARD = 'b'
DOMAIN = 'http://2ch.hk'

n_pages = 5
thread_urls = []

for page in range(1, n_pages + 1):
    url = DOMAIN + '/' + BOARD + '/' + str(page) + '.html'
    print('Reading %s...' % url)

    with urllib.request.urlopen(url) as response:
       html = response.read()

    soup = BeautifulSoup(html, 'lxml')
    thread_urls += [DOMAIN + a.get('href') for a 
                in soup.findAll(attrs = {'class': 'orange'})]

print('Found: %s thread urls' % len(thread_urls))


board_posts = []

for url in thread_urls:
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'lxml')

    posts = []
    for hit in soup.findAll(attrs={'class' : 'post-message'}):
        this_post = hit.get_text(separator = ' ')
        posts.append(this_post)

    board_posts += posts
    print('Found: %s posts' % len(posts))

    filename = re.sub('[^0-9]', '', url)[1:] + '.txt'
    with open(TXT_DIR + '/' + filename, 'w') as txt_file:
        txt_file.write('\n'.join(posts))
    
    print('Successfully saved to: %s/%s' % (TXT_DIR, filename))


board_text = '\n'.join(board_posts)
# remove quotes, unnecessary punctuation, etc
board_text = re.sub(r'>>[0-9]*|>', '', board_text).lower()
board_text = re.sub(r'\(op\)|\(you\)', '', board_text)
board_text = re.sub(r'&gt;', ' ', board_text).strip()
