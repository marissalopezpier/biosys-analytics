#!/usr/bin/env python3
"""
Author : Marissa pier
Date   : 3 13 2019
Purpose: Python program for blastomics
"""


import os
import sys
import argparse
import csv
#import Bio
#from Bio import SeqIO

from collections import defaultdict
#-------------------------------------

def main():
    args = get_args()
    hits_header = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
    annotations_filename = args.annotations
    hits_filename = args.hits_file
    outfile = args.outfile

    if outfile=='':
        f_out = sys.stdout
    else:
        f_out = open(outfile,'w')

    if not os.path.isfile(hits_filename):
        print('"{}" is not a file'.format(hits_filename),file=sys.stderr)
        exit(1)
    if not os.path.isfile(annotations_filename):
        print('"{}" is not a file'.format(annotations_filename),file=sys.stderr)
        exit(1)

    f_annot = open(annotations_filename,'r')
    genus_dict = {}
    species_dict = {}
    csv_reader = csv.DictReader(f_annot) #using first line as hits_header

    for row in csv_reader:
        centroid = row['centroid']
        genus = row['genus']
        if not genus:
            genus = 'NA'
        species = row['species']
        if not species:
            species = 'NA'
        genus_dict[centroid] = genus
        species_dict[centroid] = species
    f_annot.close()

    print('seq_id\tpident\tgenus\tspecies',file=f_out)

    f_hits = open(hits_filename,'r')
    #sseqid = []
    #pident = []
    csv_reader = csv.DictReader(f_hits,fieldnames=hits_header,delimiter='\t')
    for row in csv_reader:
        #print(row)
        sseqid = row["sseqid"]
        pident = row["pident"]

        if sseqid in genus_dict:
            genus = genus_dict[sseqid]
            species = species_dict[sseqid]
            print('{}\t{}\t{}\t{}'.format(sseqid,pident,genus,species),file=f_out)
        else:
            print('Cannot find seq "{}" in lookup'.format(sseqid),file=sys.stderr)

    f_out.close()





# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'hits_file',
        metavar='FILE',
        help='BLAST output(-outfmt 6)',
        type=str
        )

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotaiton file',
        metavar='FILE',
        default='',
        )

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        default='',
        )

    return parser.parse_args()

if __name__ == "__main__":
    main()

