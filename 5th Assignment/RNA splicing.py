from Bio.Seq import Seq
from Bio import SeqIO

with open ("5th Assignment/rosalind_splc.txt") as file:
    sequence = []
    for seq_record in SeqIO.parse(file,'fasta'):
        sequence.append(str(seq_record.seq))
    
    seq = sequence[0]                        
    introns = sequence[1:]                        

    for i in range(len(introns)):                  
        seq = seq.replace(introns[i], '')

    seq = Seq(seq)                       
    print(seq.translate(to_stop = True))

