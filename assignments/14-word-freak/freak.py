#!/usr/bin/env python3
"""
Author : Marissa pier
Date   : 4 23 2019
Purpose: Python program for word freak
"""


import os
import sys
import re
import argparse
import csv
from collections import defaultdict


#-------------------------------------

def main():
    args = get_args()
    words_fis = args.input_files
    sort_wd = args.sort
    min_wd = args.min
    
    counter = defaultdict(int)
    
    for fi in words_fis:
        with open(fi,'r') as input_file:
            for line in input_file:
                words = re.sub('[^a-zA-Z0-9 ]','',line).split()
                for word in words:
                    counter[word.lower()] += 1
    
    if sort_wd =='word':
        pairs = sorted(counter.items())
        for p in pairs:
            word, freq = p
            if freq >= min_wd:
                print('{:20} {}' .format(word, freq))
        
    elif sort_wd == 'frequency':
        pairs = sorted([(x[1], x[0]) for x in counter.items()])
        for p in pairs:
            freq, word = p
            if freq >= min_wd:
                print('{:20} {}' .format(word, freq))



   

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Print word frequencies',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'input_files',
        metavar ='FILE',
        help ='File input(s)',
        nargs='+',
#        type = argparse.FileType('r')
        )


    parser.add_argument(
        '-s',
        '--sort',
        help = 'Sort by word or frequency',
        metavar ='str',
        default ='word',
        )

    parser.add_argument(
        '-m',
        '--min',
        help = 'Minimum count',
        metavar ='int',
        type = int,
        default = 0,
        )

    return parser.parse_args()

if __name__ == "__main__":
    main()

