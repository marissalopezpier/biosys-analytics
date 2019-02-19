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

    args = parse_args()
    sequence = args.sequence
    codons = args.codons
    outfile = args.outfile

    # Check if codons points to a valid filename, else exit
    if not os.path.isfile(codons):
        print('--codons "{}" is not a file'.format(codons))
        exit(1)

    codon_file = open( codons, 'r' )
    codon_dict = {}
    for line in codon_file:
        line = line.split() # split by white space results in [codon,amino acid] -> [key,value]
        codon = line[0].upper() #codon is in the key position
        amino_acid = line[1] #amino_acid is in the value posiiton
        codon_dict[codon]=amino_acid #to set dict use format dict_variable[key]=value
    codon_file.close()


    amino_acid_seq = ''
    codon = ''
    for char in sequence:
        codon += char
        if len(codon)==3:
            #full codon
            if codon.upper() in codon_dict: #Check if the key is in the dictionary
                amino_acid = codon_dict[codon.upper()] #get the value from the dictionary for the key
            else:
                amino_acid = '-'
            amino_acid_seq += amino_acid
            codon = ''

    f_out = open( outfile, 'w' )
    f_out.write(amino_acid_seq)
    f_out.close()
    print('Output written to "{}"'.format(outfile))




def parse_args():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
    parser = ArgumentParser(description="Translate DNA/RNA to proteins",formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument( 'sequence', help='DNA/RNA sequence', type=str, metavar='STR')
    # default type is string so you don't have to put it. If you want to convert to a float or an int that is when you should do it
    parser.add_argument( '-c', '--codons', help='A file with codon translations', type=str, metavar='FILE', default=None, required=True )
    #required=true is that you have to input the -c argument
    parser.add_argument( '-o', '--outfile', help='Output filename', type=str, metavar='FILE', default='out.txt')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()

