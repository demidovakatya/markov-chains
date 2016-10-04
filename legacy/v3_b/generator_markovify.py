import markovify

text = scraper.make_text(scraper.get_board_posts(urls))
text_model = markovify.Text(text)

def generate_sentences(text_model, n = 50):
    filename = '../markovify_generated_b.txt'
    for _ in range(n): 
        sentence = text_model.make_sentence()
        print(sentence, '\n')
        try:
            open(filename, 'a').write(sentence, '\n')
        except TypeError:
            pass