#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : 4.17.2019
Purpose: Extract k-mers from string
"""

import os
import sys
import argparse
import Bio
from Bio import SeqIO
from collections import Counter

def main():

    args = get_args()
    fasta = args.fasta
    k = args.overlap
    
    
    if not os.path.isfile(fasta):
        print('"{}" is not a file'.format(fasta),file=sys.stderr)
        exit(1)
    if k < 1:
        print('-k "{}" must be a positive integer'.format(k),file=sys.stderr)
        exit(1)
    
    seq_ids = []
    seqs = []
    first_kmers = []
    last_kmers = []

    for record in SeqIO.parse ( fasta, 'fasta'):
        seqid = record.id
        kmers = find_kmers(str(record.seq),k)
        
        seq_ids.append( seqid )
        seqs.append( str(record.seq) )
        first_kmers.append( kmers[0] )
        last_kmers.append( kmers[-1] )
    #print(seqs)
    #print(first_kmers)
    #print(last_kmers)
    
    for i in range(len(last_kmers)):
        kmer2 = last_kmers[i]
        for j in range(len(first_kmers)):
            kmer1 = first_kmers[j]
            if kmer1==kmer2 and not (i==j):
                print(seq_ids[i],seq_ids[j])

def find_kmers( string, k ):
    output = []
    if len(string) < k:
        print('There are no {}-length substrings in "{}"'.format(k,string))
    else:
        n = len(string) - k +1
        for i in range (0,n):
            output.append(string[i:i+k])
    return output

def test_find_kmers():
    """Test the `find_kmers` function"""
    assert grph.find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert grph.find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert grph.find_kmers('ACTG', 4) == ['ACTG']



# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Graph through sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

#positional argument statement
    parser.add_argument(
        'fasta',
        metavar='str',
        help = 'FASTA file',
        type = str,
        )

#optional argument statement
    parser.add_argument(
        '-k',
        '--overlap',
        metavar='int',
        help='K size of overlap',
        type =int,
        default = 3,
        )

    return parser.parse_args()

if __name__ == "__main__":
    main()

