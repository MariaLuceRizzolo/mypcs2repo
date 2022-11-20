with open("3rd Assignment/rosalind_gc.txt") as file:
    text = file.read().replace('\n', '')
    content = text.split('>Rosalind_')[1:]

    GC_max = 0

    for sequence in content:
        GC_cont = ((sequence.count('G')+sequence.count('C'))/(sequence.count('G')+sequence.count('C')+sequence.count('A')+sequence.count('T')))*100
        if GC_cont > GC_max:
            GC_max = GC_cont
            ID = 'Rosalind_' + sequence[:4]

    print(ID)                                  
    print(GC_max)