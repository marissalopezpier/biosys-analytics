#!/usr/bin/env python3
"""
Author : Marissa pier
Date   : 3 20 2019
Purpose: processes a swiss-prot file as positional arg
"""
import os
import sys
import argparse
import Bio
from Bio import SeqIO
from pprint import pprint

def main():
    args = get_args()
    #converting a list/tuple into a set
    skip_taxa=set()
    for s in args.skip:
        skip_taxa.add(s.lower())

    take_keyword =args.keyword.lower()
    file_output =args.output
    input_uniprot =args.input

    if not os.path.isfile(input_uniprot):
        print('"{}" is not a file'.format(input_uniprot),file=sys.stderr)
        exit(1)

    print ('Processing "{}"'.format(input_uniprot))
    skipped=0
    took=0
    f_out=open(file_output,'w')
    for record in SeqIO.parse (input_uniprot,'swiss'):
        annotations=(record.annotations)
        keywords = set()
        for k in annotations['keywords']:
            keywords.add(k.lower())
        if take_keyword not in keywords:
            skipped +=1
            continue
        taxonomy = set()
        for t in annotations['taxonomy']:
            taxonomy.add(t.lower())
        if len(skip_taxa.intersection(taxonomy)) >0:
            skipped +=1
            continue
        took +=1
        SeqIO.write( record,f_out,'fasta' )
    f_out.close()
    print('Done, skipped {} and took {}. See output in "{}".'. format(skipped, took, file_output))


# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'input',
        help='Uniprot file',
        metavar='FILE',
        type=str,
        )
    parser.add_argument(
        '-s',
        '--skip',
        help='Skip Taxa',
        metavar='STR [STR ...]',
        default='',
        nargs='+',
        type=str,
        )
    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on Keyword',
        metavar='STR',
        default=None,
        required=True,
        type=str,
        )
    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='FILE',
        default='out.fa',
        type=str,
        )

    return parser.parse_args()

if __name__ == "__main__":
    main()

