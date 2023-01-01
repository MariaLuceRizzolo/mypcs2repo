from Bio import SeqIO

with open ("5th Assignment/rosalind_grph.txt") as file:
    name = []
    seq = []
    for seq_record in SeqIO.parse(file,'fasta'):
        name.append(str(seq_record.name))
        seq.append(str(seq_record.seq))

    for i in range(len(seq)):
        for j in range(len(seq)):
            if i != j and seq[i][-3:] == seq[j][:3]:
                name1 = name[i]
                name2 = name[j]

                print(name1, name2)