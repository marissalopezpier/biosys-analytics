#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : May 7th 2019
Purpose: Python program to translate text to pig latin
"""

import os
import re
import string
import sys
import argparse

def main():
    args = get_args()
    char = args.character
    inputs = args.Inputs
    scale = args.scale
    min_num = args.minimum

    for num in (sorted(inputs)):
        if num >= min_num:
            print(num, char*int(num/scale))


#def histogram (inputs):
#    for n in intputs:
#        output=''
#        times =n
#        while (times>0):
#            output+='|'
#            times= times -1
#        print(output)
#____________________________________________________________________________
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Histogrammer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# Positional Argument (filein)
    parser.add_argument(
          'Inputs',
          metavar='int',
          help='Inputs',
          type = int,
          nargs='+',

          )
    parser.add_argument(
          '-c',
          '--character',
          metavar='str',
          help='Character to represent',
          type = str,
          default = '|',
          )
    parser.add_argument(
          '-m',
          '--minimum',
          metavar='int',
          help='Minimum value to print',
          type = int,
          default = 1,
          )
    parser.add_argument(
          '-s',
          '--scale',
          metavar='int',
          help='Scale inputs',
          type = int,
          default = 1,
          )
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()

