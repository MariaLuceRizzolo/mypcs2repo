from Bio import SeqIO

with open ("5th Assignment/rosalind_sseq.txt") as file:
    seq = []
    for seq_record in SeqIO.parse(file,'fasta'):
        seq.append(str(seq_record.seq))

    s = seq[0]
    t = seq[1]

    pos = 0                                    
    positions = []     
                            
    for i in range(len(t)):                    
        for j in range(pos, len(s)):  
            pos += 1                           
            if len(positions) < len(t):        
                if t[i] == s[j]:               
                    positions.append(pos)      
                    break                      
    print(*positions, sep=' ')                 


