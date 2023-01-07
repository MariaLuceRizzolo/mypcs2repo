from Bio import SeqIO

with open ("5th Assignment/rosalind_long.txt") as file:
    for seq_record in SeqIO.parse(file,'fasta'):
        seq = []
        seq.append(str(seq_record.seq))

    i = 0
    k = int(0.5*(len(seq[0]))+1)

    while i == 0:
        temp = seq[0]
        for j in range(k,2*(k-1)):
            for s in seq[1:]:
                if s[-j:] == seq[0][:j]:
                    seq[0] = s + seq[0][j:]
        if temp == seq[0]:
            i = 1
    print(seq[0])