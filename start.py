"""
Log File Parser

Usage:
    start.py parse_ifwi <input_dir>
    start.py parse_minimax <input_dir>

Options:
    input_dir       Input Directory with files for parsing
    --dir           Input directory
    -h --help       Show the screen
"""
from docopt import docopt
from parse_it import parse_log

__version__ = "1.0.0"

def main(arg):
    obj = parse_log.LogParsing(arg["<input_dir>"])
    if arg["parse_ifwi"]:
        obj.parse_ifwi_log(parse_file_name = "parse_ifwi")
    if arg["parse_minimax"]:
        obj.parse_minimax_results_log(parse_file_name = "parse_minimax")

if __name__ == '__main__':
    arg = docopt(__doc__)
    #print(arg)
    main(arg)