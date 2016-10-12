import markovify
import b_scraper as scraper
from b_generator_markovify import generate_sentences

# n_pages = input('Enter n_pages (1-5): ')
urls = scraper.get_thread_urls(5)

text = scraper.make_text(scraper.get_board_posts(urls))
text_model = markovify.Text(text)
generate_sentences(text_model)
