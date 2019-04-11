#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : 4_10_2019
Purpose: Python program to find unclustered proteins
"""

import os
import sys
import argparse
import Bio
from Bio import SeqIO
from pprint import pprint
import re

def main():
    args = get_args()
    # parse the cdhit file then get all the protein IDs that have been clustered
    outfile_cdhit = args.cdhit
    #input file that has protein IDS these are clustered IDs
    proteins_fasta =args.proteins
    #IDs of all proteins
    outfile =args.outfile
    # file that outputs which ones were unclustered (aka total-clustered)
    if not os.path.isfile(proteins_fasta):
        print('--proteins "{}" is not a file'.format(proteins_fasta),file=sys.stderr)
        exit(1)

    if not os.path.isfile(outfile_cdhit):
        print('--cdhit "{}" is not a file'.format(outfile_cdhit),file=sys.stderr)
        exit(1)


    clustered_proteins = set()
    with open(outfile_cdhit,'r') as f:
        for line in f:
            out = re.search('\|(\d+)\|',line)
            if out:
                clustered_proteins.add(out.group(1))

    total_proteins = 0
    unclustered_protiens = 0
    f_out = open( outfile,'w')

    for record in SeqIO.parse (proteins_fasta, 'fasta'):
        #print(record.id)
        out = re.search('^(\d+)',record.id)
        if out:
            protien = out.group(1)
            total_proteins += 1
            if protien not in clustered_proteins:
                unclustered_protiens += 1
                SeqIO.write( record, f_out, "fasta")
    f_out.close()
    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(unclustered_protiens,total_proteins,outfile))

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Find unclustered proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        default=None,
        type=str,
        required =True,
        )
    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        default=None,
        required =True,
        type=str,
        )
    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        default='unclustered.fa',
        type=str,
        )

    return parser.parse_args()

if __name__ == "__main__":
    main()

