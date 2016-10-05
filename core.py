def get_paths_to_txt():
    """
    returns list of files with texts
    """
    import os
    files = []
    TXT_DIR = './txt/'
    for txt_item in os.listdir(TXT_DIR):
        if txt_item.endswith('.txt'):
            files.append(os.path.join(TXT_DIR, txt_item))
        if os.path.isdir(txt_item):
            for item in os.listdir(os.path.join(TXT_DIR, txt_item)):
                if item.endswith('.txt'):
                    files.append(os.path.join(TXT_DIR, txt_item, item))
    return files

def read_txt_files():
    files = get_paths_to_txt()
    texts = []

    for file in files:
        fragments = [f.strip() for f in open(file).read().split('\n')]
        fragments = [f for f in fragments if f != '']
        texts += fragments

    text = '\n'.join(texts)
    return text

def beautify(text = read_txt_files()):
    import re
    # text = text.lower()
    # remove urls
    text = re.sub('(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),#]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', '', text)
    # remove quotes, unnecessary punctuation, etc
    text = re.sub(r'>>[0-9]*|>', '', text)
    text = re.sub(r'<+', ' ', text)
    text = re.sub(r'\.{2,}', '. ', text)
    text = re.sub(r'[\(|\)]{2,}', ' ', text)
    text = re.sub(r'\(OP\)|\(YOU\)', '', text)
    text = re.sub(r'&gt;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
    