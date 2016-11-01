import argparse
import logging.config

from src.MCApplication import MCApplication


def main():
    args = __parse_args()
    logging.config.fileConfig('./logging.conf')
    MCApplication(args).run()

def __parse_args():
    description = '''
                  Generate strings using the markov-chains application.\n\nExample:\n\t
                  generate.py --generator 'mvf' --output_size 10 --src 'b'
                  '''

    parser = argparse.ArgumentParser(description=description)
    
    parser.add_argument('--src', 
                        metavar='SC', 
                        nargs='*',
                        choices=['b', 'galya.ru', 'woman.ru'],
                        default=['b', 'galya.ru', 'woman.ru'],
                        help="(str or multiple str separated by space, from {'b', 'galya.ru', 'woman.ru'}) ---- Sources to use for getting data from the web.")
    
    parser.add_argument('--mode', 
                        action='store', 
                        default='generate',
                        choices=['generate'])
    
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
                        help="(str, default './storage') ----- Path to folder the output of program will be saved to.")

    return vars(parser.parse_args())

if __name__ == '__main__':
    main()
