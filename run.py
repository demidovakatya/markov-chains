from src.MCApplication import MCApplication
import logging.config

logging.config.fileConfig('./logging.conf')

MCApplication().run({
    'storage_path': "./storage",
    'scrapers': ['b', 'krovostok', 'galya.ru'],
    'generator': 'mc',
    'output_size': 50
})
