#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : 4.15.2019
Purpose: Compare Hamm Text
"""

import os
import sys
import argparse
import hamm
import logging

def main():

    args = get_args()

    S1 , S2 = args.Hamm #left has two positional args if not filled explodes

    error = args.debug

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
        )

    if not os.path.isfile(S1):
        print('"{}" is not a file'.format(S1),file=sys.stderr)
        exit(1)
    if not os.path.isfile(S2):
        print('"{}" is not a file'.format(S2),file=sys.stderr)
        exit(1)

    f1 = open(S1, 'r')
    txt1=f1.read().split()
    f1.close()
    f2 = open(S2, 'r')
    txt2=f2.read().split()
    #number of words matches
    f2.close()
    total_dist = 0
    for w1, w2 in zip(txt1,txt2):
        cur_dist = dist(w1, w2)
        total_dist += cur_dist
    print(total_dist)

    logging.debug('f1 = {}, f2 = {}'.format(S1, S2))

def dist(S1, S2):
    counter =abs(len(S1)-len(S2)) #need to evaluate length of word; abs is for if S1 is greater than S2
    for c1 ,c2 in zip(S1,S2): #break each zip tuple/element into the two characters of the two strings; ordered
        if not c1 == c2:
            counter+=1
    #create logging statement here
    logging.debug('c1 = {}, c2 = {}, counter = {}'.format(S1, S2, counter))
    return counter

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

#positional argument statement
    parser.add_argument(
        'Hamm',
        metavar='FILE',
        help='File inputs',
        nargs=2,
        type=str
        )

    parser.add_argument(
        '-d',
        '--debug',
        help='Debug',
        action='store_true',
        #default='False',
        )

    return parser.parse_args()

if __name__ == "__main__":
    main()

