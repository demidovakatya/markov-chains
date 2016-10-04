import re

from bs4 import BeautifulSoup
html = open('butthurt_thread.html').read()
soup = BeautifulSoup(html)

texts = []
for hit in soup.findAll(attrs={'class' : 'post-message'}):
    # print(re.sub(r'>[0-9]*', '', hit.text))
    this_text = re.sub(r'<.+>|\n|[&gt;]+[0-9]+', '', hit.prettify()).strip()
    this_text = re.sub(r'\s+', ' ', this_text)
    print(this_text)
    texts += this_text.split('. ')

text = '\n'.join(texts)

# In [32]: a.contents
# Out[32]: 
# ['\nУгадай аниме и прочую японщину по бугутру тред.',
#  <br/>,
#  <br/>,
#  <strong>ВЕТЕР ЗАГНУЛ ТЮЛЬПАН НА БОК<br/>@<br/>МОЛНИЯ СВЕРКНУЛА<br/>@<br/>КОСОЙ ДОЖДЬ ПОЛИЛ<br/>@<br/>ПРОТЕКАЕТ ЧЕРЕЗ ТРЕЩИНЫ<br/>@<br/>И СОБИРАЕТСЯ В ОКРУГЛЫЕ ЛУЖИЦЫ<br/>@<br/>ДАВАЙ ПОРЫБАЧИМ! ВОТ КРЮЧОК<br/>@<br/>ЗАСУШИМ НЕМНОГО ПОЙМАННОЙ РЫБЫ<br/>@<br/>ПОЛУЧИЛИ ТАЙТЛ-NAME</strong>,
#  <br/>,
#  '\n']

from pymarkovchain import MarkovChain
mc = MarkovChain(".")
mc.generateDatabase(text, '\n')

mc.generateString()
