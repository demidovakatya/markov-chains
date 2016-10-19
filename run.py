import argparse
import logging.config
from src.MCApplication import MCApplication


def main():
    args = __parse_args()
    logging.config.fileConfig('./logging.conf')
    MCApplication(args).run()

def __parse_args():
    description = '''
                  Run markov-chains application.\n\nExample:\n\t
                  run.py --scrapers 'b' --generator 'mvf' --output_size 10
                  '''
    
    parser = argparse.ArgumentParser(description=description)
    
    parser.add_argument('--scrapers', 
                        metavar='SC', 
                        nargs='*',
                        choices=['b', 'galya.ru', 'krovostok', 'woman.ru'],
                        required=True,
                        help="(str or array of str from {'b', 'galya.ru', 'krovostok', 'woman.ru'}) ---- Scrapers to use for getting data from the web.")
    
    parser.add_argument('--mode', 
                        action='store', 
                        default='all',
                        choices=['all', 'parse', 'generate'],
                        help="({'all', 'parse', 'generate'}, default 'all') ---- Mode in which the script should be run. If 'all' (default), it will parse the data and generate strings from it. If 'parse', new data will be parsed only. If 'generate', generated strings will be streamed to output.")
    
    parser.add_argument('--writer', 
                        action='store', 
                        default='console',
                        choices=['console', 'txt'],
                        help="({'console', 'txt'}, default 'console') ---- Preferred output – console or txt file.")
    
    parser.add_argument('--generator', 
                        action='store', 
                        default='mvf',
                        choices=['mvf', 'mc'],
                        help="({'mvf', 'mc'}, default 'mvf') ---- Markov chains generator.")
    
    parser.add_argument('--output_size', 
                        action='store', 
                        default=50, 
                        type=int,
                        help='(int, default 50) ----- Number of lines to be sent to output.')
    
    parser.add_argument('--storage_path', 
                        action='store', 
                        default='./storage',
                        help="(str, default './storage') ----- Path to txt file the output will be saved to. If --writer=='txt', set this argument (example: '~/Downloads/markov-chains/output.txt')." )

    return vars(parser.parse_args())

if __name__ == '__main__':
    main()
