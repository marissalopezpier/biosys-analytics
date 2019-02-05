#!/usr/bin/env python3
"""
Author : mal1
Date   : 2019-01-31
Purpose: Rock the Casbah
"""

import os
import sys


# Set up main fuction
def main():
    names = sys.argv[1:]

    if len(names) == 0:
        print('Usage: {} NAME [NAME ...]'.format(os.path.basename(sys.argv[0])))
        exit(1)
    if len(names) ==1:
        print('Hello to the 1 of you: '+ names[0] + '!')
        #printf('Hello to the 1 of you: {} !' .format(names))
    elif len(names)==2:
        print('Hello to the 2 of you: {}!' .format (' and '.join(names)))
    elif len(names) >2:
        num=len(names)
        print('Hello to the {} of you: {}, and {}!' .format ( num, ', '.join(names[:-1]), names[-1]))


main() # Call main function

