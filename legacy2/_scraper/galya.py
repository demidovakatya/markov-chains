import re
import os
import urllib.request
from bs4 import BeautifulSoup

TXT_DIR = './txt/galya'
DOMAIN = 'http://galya.ru'

def get_threads_urls(n_pages = 1):
    threads_urls = []
    for page in range(0, n_pages):
        url = DOMAIN + '/clubs/index.php?dlimit=%s&p=1&board_id=0&ltype=0' % (page * 115)
        print('Reading %s...' % url)

        with urllib.request.urlopen(url) as response:
           html = response.read()

        soup = BeautifulSoup(html, 'html5lib')
        threads_urls += [DOMAIN + '/clubs/' + re.sub('&.*', '', a.get('href')) for a
                    in soup.findAll(attrs = {'title': 'дата последнего комментария'})]
    print('Found: %s threads.' % len(threads_urls))

    return threads_urls

urls = get_threads_urls()

def get_posts(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html5lib')

    posts = []
    for hit in soup.findAll(attrs={'class' : 'text'}):
        this_post = hit.get_text(separator = ' ')
        posts.append(this_post)

    filename = re.sub('[\s\S]+id=', '', url) + '.txt'
    with open(os.path.join(TXT_DIR, filename), 'w') as txt_file:
        txt_file.write('\n'.join(posts))

    print('Successfully saved %s posts to: %s/%s' % (len(posts), TXT_DIR, filename))

    return posts

def get_threads_posts(threads_urls):
    threads_posts = []
    for url in threads_urls:
        threads_posts += get_posts(url)
    return threads_posts

posts = get_threads_posts(urls)