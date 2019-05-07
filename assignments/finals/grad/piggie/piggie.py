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
#    print(make_piggy('tiger'))
#    print(make_piggy('The'))
#    print(line_to_piggy('The quick brown fox.'))

    #inputs filein, fileout(probably has a default)
    #fileout = filein + '.out'

    args = get_args()
    filein = args.filein
    outdir = args.outdir
#    print(filein,fileout)
    #can put bad input statement here
    for file in filein:
        if not os.path.isfile(file):
            print('FILE "{}" is not a file'.format(file),file=sys.stderr)
            exit(1)
    for foo in outdir: 
        if not os.path.isfile(foo):
            print('FILE "{}" is not a file'.format(foo),file=sys.stderr)
            exit(1)


    ## (START) If it is a file
    f_in = open( filein, 'r' )
    if len(outdir)>0:
        f_out = open( outdir, 'w' )

    for line in f_in:
        new_line = line_to_piggy( line )
        #print or write new_line to a file
        if len(outdir)>0:
            f_out.write(new_line+'\n')
        else:
            print(new_line)
#        print(new_line)
#

    f_in.close()
    if len(outdir)>0:
        f_out.close()
    ## (END) If it is a file

#def paragraph_to_piggy( paragraph)

def line_to_piggy( line ):
#    new_line = re.sub('\w+',lambda x: make_piggy(x.group()),line)
#    return new_line
    new_words = []
    for word in line.split():
        new_words.append(make_piggy(word))
    return ' '.join(new_words) #join new_words list together with spaces inbetween

def make_piggy( word ):
    consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    match = re.match('^([' + consonants + ']+)(.+)', word)
    if match:
        new_word = '-'.join([match.group(2), match.group(1) + 'ay'])
    else:
        new_word = word + '-ay'
    return new_word

#____________________________________________________________________________
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Convert to Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# Positional Argument (filein)
    parser.add_argument(
          'filein',
          metavar='FILE',
          help='Input file(s)',
          type = str,
          nargs='+',

          )
    parser.add_argument(
          '-o',
          '--outdir',
          help='Output directory',
          metavar='str',
          type = str,
          default='out-yay',
          )

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()

