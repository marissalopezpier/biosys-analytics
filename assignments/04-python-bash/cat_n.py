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
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        exit(1)

    if not os.path.isfile(args[0]):
        print('{} is not a file'.format(args[0]))
        exit(1)

    infile = open(args[0])

    data= infile.read()
#    numoflines=len(data.splitlines())
    i = 0
    for line in data.splitlines():
        i += 1
        print('{:>5d}: {}'.format(i,line))

#    for i, line in enumerate(infile):
#        print('{:>5d}: {}'.format(i+1,line))


main() # Call main function

