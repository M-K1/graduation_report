#!/usr/bin/env python 

import os
import pysam
import sys
from collections import Counter
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i',
                '--infile',
                metavar='File',
                help='Input bamfile; should be sorted and indexed',
                type=str,
                required=True)

parser.add_argument('-o',
                '--outfile',
                metavar='File',
                help='Output fasta file for consensus (default stdout)',
                default=sys.stdout,
                type=argparse.FileType('w'),
                required=False)

parser.add_argument('-d', 
                    '--mindepth',
                    help='Minimal depth needed (default: 1)',
                    default=1,
                    type=int,
                    required=False)

args = parser.parse_args()

#naam file boven consensus ipv oudere referentie
filename = os.path.basename(str(args.outfile))
file = filename.replace(".fasta' mode='w' encoding='UTF-8'>", "")

def makeConsensus(bamfile, covlim):
    consensus = []
    with pysam.AlignmentFile(bamfile, "rb") as bamfile:
        for ref in bamfile.references:
            for pileupcolumn in bamfile.pileup(ref):
                pos = Counter()
                for pileupread in pileupcolumn.pileups:
                    if not pileupread.is_del and not pileupread.is_refskip:
                        nt = pileupread.alignment.query_sequence[pileupread.query_position]
                        pos[nt] += 1
                cov = sum(pos.values())
                if (len(pos) == 0) | (cov < covlim):
                    consensus.append('N')
                else:
                    best = max(pos, key=pos.get)
                    consensus.append(best)
        return('>'+file+'_consensus\n'+''.join(consensus))

if __name__ == '__main__':
    with args.outfile as out:
        consensus = makeConsensus(args.infile, args.mindepth)
        print(consensus, file=out)
            
