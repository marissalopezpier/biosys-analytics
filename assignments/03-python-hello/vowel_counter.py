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
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        exit(1)

    word = args[0]

    num_vowels = 0

    for vowel in ['a','e','i','o','u','A','E','I','O','U']:#'aeiou':
        num_vowels = num_vowels + word.count(vowel)
    if (num_vowels)==1:
        print('There is {} vowel in "{}."' .format (num_vowels, word))
    elif (num_vowels) >1 or (num_vowels)==0:
        print('There are {} vowels in "{}."'.format (num_vowels, word))

main() # Call main function
