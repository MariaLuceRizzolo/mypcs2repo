from Bio import SeqIO

with open ("5th Assignment/rosalind_long.txt") as file:
    for seq_record in SeqIO.parse(file,'fasta'):
        seq = []
        seq.append(str(seq_record.seq))

    i = 0
    k = int((len(seq[0]))/2+1)

    while i == 0:
        newseq=seq[0]
        for j in range(k,2*(k-1)):
            for seq in seq[1:]:
                if seq[0][-j:] == seq[:j]:
                    seq[0] = seq[0] + seq[j:]
        if newseq == seq[0]:
            i = 1
    print(seq[0])