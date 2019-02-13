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
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        exit(1)

    if not os.path.isfile(args[0]):
        print('{} is not a file'.format(args[0]))
        exit(1)
    if len(args) == 1:
        num_lines = 3
    else:
        num_lines = int(args[1])
        if num_lines <= 0 :
            print('lines ({}) must be a positive number'. format(args[1]))
            exit(1)
    infile = open(args[0])
    data = infile.read()
    lines = data.splitlines()

    for i,line in enumerate(lines):
        if i+1 >num_lines:
            break
        print(line)

main() # Call main function

