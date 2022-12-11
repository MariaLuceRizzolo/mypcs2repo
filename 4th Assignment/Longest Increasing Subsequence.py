with open('4th Assignment/rosalind_lgis.txt') as file:
    n = int(file.readline())
    seq_str = file.readline().strip().split()    
   
    seq=[]
    for i in seq_str:
        seq.append(int(i))
    seq.pop(0)

    sequence_list = [[] for i in range (len(seq))]
    sequence_list[0].append(seq[0])
    sequence_list2 = [[] for i in range (len(seq))]
    sequence_list2[0].append(seq[0])

    for i in range(1,len(seq)):
        for j in range(i):
            if (seq[i] > seq[j] and (len(sequence_list[i]) < len(sequence_list[j]))):
                sequence_list[i] = list(sequence_list[j]) 
            if (seq[i] < seq[j] and (len(sequence_list2[i]) < len(sequence_list2[j]))):
                sequence_list2[i] = list(sequence_list2[j]) 
        sequence_list[i].append(seq[i])
        sequence_list2[i].append(seq[j])

    inc =(max(sequence_list,key=len))
    increasing=" ".join(map(str,inc))
    dec= (max(sequence_list2,key=len))
    decreasing=" ".join(map(str,dec))

    print(increasing)
    print(decreasing)
