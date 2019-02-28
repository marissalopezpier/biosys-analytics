#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : 2.27.2019
Purpose: Python program to write gc content program
"""

import os
import sys
import Bio
from Bio import SeqIO
from collections import Counter

def main():

    args = parse_args()

    fasta = args.fasta
    outdir = args.outdir
    pct_gc = args.pct_gc

    if not (1<=pct_gc<=100):
        print('--pct_gc "{}" must be between 0 and 100'. format(pct_gc))
        exit(1)
    seqcounter=0

    if not (os.path.isdir(outdir)):
        os.mkdir(outdir)

    for file in fasta:
        if not os.path.isfile(file):
            print('"{}" is not a file'.format(file),file=sys.stderr)
            continue
        #Open files
        basename = os.path.basename(file)
        f_high = open( os.path.join(outdir,os.path.splitext(basename)[0]+'_high.fa'), 'wt' )
        f_low  = open( os.path.join(outdir,os.path.splitext(basename)[0]+'_low.fa'), 'wt' )

        for record in SeqIO.parse (file, 'fasta'):
            seqcounter +=1
            seq_len=len(record.seq)
            nucs=(Counter(record.seq))
            gc_num=nucs.get('G',0)+nucs.get('C',0)
            gc=(int((gc_num/seq_len)* 100))
            #print(seq_len)
            #print(gc)
            #print('HIGH' if gc >= pct_gc else 'LOW')
            if gc >= pct_gc:
                #f_high.write('{}\n'.format(record.seq))
                SeqIO.write( record, f_high, 'fasta' )
            else:
                #f_low.write('{}\n'.format(record.seq))
                SeqIO.write( record, f_low, 'fasta' )

        #Close files
        f_high.close()
        f_low.close()
    print('Done, wrote {} sequences to out dir "{}"'.format(seqcounter,outdir))

def parse_args():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
    parser = ArgumentParser(description="Segregate FASTA sequences by GC content",formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument( 'fasta', help='Input FASTA file(s)', type=str, metavar='FASTA', nargs='+')

    parser.add_argument( '-o', '--outdir', help='Output directory (default: out)', type=str, metavar='DIR', default='out' )

    parser.add_argument( '-p', '--pct_gc', help='Dividing line for percent GC', type=int, metavar='int', default=50)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()

