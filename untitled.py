import markovify
import scraper
import gen_markovify

# n_pages = input('Enter n_pages (1-5): ')
urls = scraper.get_thread_urls(3)

text = scraper.make_text(scraper.get_board_posts(urls))
text_model = markovify.Text(text)
gen_markovify.generate_sentences(text_model)