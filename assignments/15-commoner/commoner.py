#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : 4.29.2019
Purpose: Find Common Words with Mismatch
"""

import os
import sys
import argparse
import logging
import re
from tabulate import tabulate

def main():

    args = get_args()

    S1 ,S2 = args.wordfile #left has two positional args if not filled explodes

    error = args.debug
    ham = args.hamming_distance
    table = args.table
    log = args.logfile
    min_len = args.min_len
    
    logging.basicConfig(
        filename=log,
        filemode='w', # append is default
        level=logging.DEBUG if args.logfile else logging.CRITICAL
        )
    

    if not os.path.isfile(S1):
        print('"{}" is not a file'.format(S1),file=sys.stderr)
        exit(1)
    if not os.path.isfile(S2):
        print('"{}" is not a file'.format(S2),file=sys.stderr)
        exit(1)
    if ham < 0:
        print ('--distance "{}" must be > 0'.format(ham))
        exit(1)

    f1 = open(S1, 'r') #default is text file read
    txt1=list(map(make_simple,f1.read().split())) # automatically split and put into list # not good way to read big files
    f1.close()
    f2 = open(S2, 'r') #default is text file read
    txt2=list(map(make_simple,f2.read().split())) # automatically split and put into list (can make more simple with list within lists)
    f2.close()
    
    logging.debug('f1 = {}, f2 = {}'.format(S1, S2))
    
    headers = ['word1','word2','distance']
    output = []
    
    for word1 in sorted(set(txt1)):
        if len(word1)<min_len or not word1:
            continue
        for word2 in sorted(set(txt2)):
            if len(word2)<min_len or not word2:
                continue
            d = dist(word1,word2)
            if d > ham:
                continue
#            print(word1,word2,d)
            output.append((word1,word2,d))
#    print(output)
    if output:
        if table:
            print(tabulate(output, headers, tablefmt="psql"))
        else:
            print('\t'.join(headers))
            for line in output:
                print('{}\t{}\t{}'.format(*line))
    else:
        print("No words in common.")
            

def make_simple( word ):
    new_word = re.sub('[^a-zA-Z0-9]', '', word).lower()
    return new_word

def dist(S1, S2):
    counter =abs(len(S1)-len(S2)) #need to evaluate length of word; abs is for if S1 is greater than S2
    for c1 ,c2 in zip(S1,S2): #break each zip tuple/element into the two characters of the two strings; ordered
        if not c1 == c2:
            counter+=1
    #create logging statement here
#    logging.debug('c1 = {}, c2 = {}, counter = {}'.format(S1, S2, counter))
    logging.debug('c1 = {}, c2 = {}, counter = {}'.format(S1, S2, counter))
    return counter

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

#positional argument statement
    parser.add_argument(
        'wordfile',
        metavar='FILE',
        help='Input files',
        nargs = 2,
        type=str
        )
    parser.add_argument(
        '-m',
        '--min_len',
        help='Min length of words',
        metavar = 'int',
        default = 0,
        type=int,
        #default='False', # default false do not need to enter
        )
    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type =int,
        default=0,
        #default='False', # default false do not need to enter
        )
    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        default = '.log',
        #default='False', # default false do not need to enter
        )
    parser.add_argument(
        '-d',
        '--debug',
        help='Debug',
        action='store_true',
        #default='False', # default false do not need to enter
        )
    parser.add_argument(
        '-t',
        '--table',
        help='Table output',
        action='store_true',
        #default='False', # default false do not need to enter
        )
    return parser.parse_args()

if __name__ == "__main__":
    main()

