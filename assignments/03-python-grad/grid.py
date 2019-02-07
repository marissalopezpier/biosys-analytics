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
    #print sys.argv[1:]
    if len(args) is not 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        exit(1)

    num=int(args[0])

    if num <= 1:
        print('NUM ({}) must be between 1 and 9'.format(num))
        exit(1)
    if num > 9:
        print('NUM ({}) must be between 1 and 9'.format(num))
        exit(1)
    for i in range(1,num**2+1):
        #print(i,end='')
        print('{:3d}'.format(i),end='')
        if i%num==0:
            print('')


main()

