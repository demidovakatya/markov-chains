import argparse
import logging.config

from src.MCApplication import MCApplication


def main():
    args = __parse_args()
    logging.config.fileConfig('./logging.conf')
    MCApplication(args).run()


def __parse_args():
    parser = argparse.ArgumentParser(
        description='Run markov-chains application')
    parser.add_argument('--scrapers', metavar='SC', nargs='*',
                        choices=['b', 'galya.ru', 'krovostok', 'woman.ru'],
                        required=True,
                        help='List of scrapers to run and use.')
    parser.add_argument('--mode', action='store', default='all',
                        choices=['all', 'parse', 'generate'],
                        help='Run in which mode.')
    parser.add_argument('--writer', action='store', default='console',
                        choices=['console', 'txt'],
                        help='Where to output the result.')
    parser.add_argument('--generator', action='store', default='mvf',
                        choices=['mvf', 'mc'],
                        help='Which markov-chains generator to use.')
    parser.add_argument('--output_size', action='store', default=50, type=int,
                        help='Output size.')
    parser.add_argument('--storage_path', action='store', default='./storage',
                        help='Where to store parse and generator results.')

    return vars(parser.parse_args())

if __name__ == '__main__':
    main()
