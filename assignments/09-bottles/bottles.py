#!/usr/bin/env python3
"""
Author : Marissa pier
Date   : 3 18 2019
Purpose: Python program for 99 bottles
"""
import os
import sys
import argparse

def main():
    args = get_args()
    num_bottles = args.num_bottles
    #10 bottles to 9 bottles
    statement_1 = "{} bottles of beer on the wall,\n{} bottles of beer,\nTake one down, pass it around,\n{} bottles of beer on the wall!"
    #2 bottles to 1 bottle
    statement_2 = "{} bottles of beer on the wall,\n{} bottles of beer,\nTake one down, pass it around,\n{} bottle of beer on the wall!"
    # 1 bottle to zero bottles
    statement_3 = "{} bottle of beer on the wall,\n{} bottle of beer,\nTake one down, pass it around,\n{} bottles of beer on the wall!"
    for i in reversed(range(num_bottles)):
        high = i + 1
        low = i
        if high >2:
            print(statement_1.format(high,high,low))
        elif high ==2:
            print(statement_2.format(high,high,low))
        else :
            print(statement_3.format(high,high,low))
        if i!=0:
            print()

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        default=10,
        type=int,
        )

    return parser.parse_args()

if __name__ == "__main__":
    main()

