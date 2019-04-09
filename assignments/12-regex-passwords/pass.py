#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : 3.8.2019
Purpose: Python program to password
"""

import os
import sys


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        exit(1)
    password = args[0]
    alt=args[1]

    if password == alt:
        print('ok')
    elif password.capitalize() == alt.capitalize():
        print('ok')
    elif password.upper() == alt.upper():
        print('ok')
    elif password == alt[1:] or password == alt[:-1] :
        print('ok')
    elif password == alt[1:-1]:
        print ('ok')
    else:
        print('nah')

if __name__ == "__main__":
    main()

