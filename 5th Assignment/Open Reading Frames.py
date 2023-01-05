import re
from Bio import SeqIO
   
codons_table = {                                                     
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'STOP',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'STOP',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'STOP',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G' 
}

with open ("5th Assignment/rosalind_orf.txt") as file:
    seq = []
    for seq_record in SeqIO.parse(file,'fasta'):
        seq = (str(seq_record.seq))

    complement = seq.translate(str.maketrans('ACTG', 'TGAC'))
    reverse = complement[::-1]
    RNA1 = seq.replace('T','U')
    RNA2 = reverse.replace('T','U')

    pattern = re.compile(r'(?=(AUG(?:...)*?)(?=UAA|UAG|UGA))')

    fragments = []
    
    for i in re.findall(pattern, RNA1):
        fragments.append(i)
    for j in re.findall(pattern, RNA2):
        fragments.append(j)

    for s in set(fragments):
        peptide = []
        codons=[]
        Met = s.find("AUG")
        for Met in range(Met, len(s), 3):
            codons.append(s[Met:Met+3])
        for c in codons:
            peptide += codons_table.get(c)

        print(''.join(map(str, peptide)))