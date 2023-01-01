from Bio import SeqIO                        
seq = []                               
with open ("5th Assignment/rosalind_tran.txt") as file:
    for seq_record in SeqIO.parse(file,'fasta'): 
        seq.append(str(seq_record.seq))        
                              
    s1 = seq[0]                            
    s2 = seq[1]                            
    transition = 0                               
    transversion = 0                             
    AG = ['A', 'G']                              
    CT = ['C', 'T']   

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if (s1[i], s2[i]) in AG:                               
                transition += 1                  
            elif (s1[i], s2[i]) in CT:        
                transition += 1                  
            else:                                
                transversion += 1  

    ratio = (transition/transversion)
    print(ratio)
