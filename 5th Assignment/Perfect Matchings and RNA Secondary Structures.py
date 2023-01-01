from Bio import SeqIO
from math import factorial

with open ("5th Assignment/rosalind_pmch.txt") as file:
    seq = []
    for seq_record in SeqIO.parse(file,'fasta'):
        seq = (str(seq_record.seq))

    matchings  = factorial(seq.count("A")) * factorial((seq.count("G")))
    print(matchings)

