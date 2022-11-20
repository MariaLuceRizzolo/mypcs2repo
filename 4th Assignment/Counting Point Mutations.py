with open("4th Assignment/rosalind_hamm.txt") as file:
    sequence = file.read().splitlines()

    hamming_distance = 0                                                
    for i, j in zip(sequence[0],sequence[1]):                        
        if i != j:                                         
            hamming_distance += 1                                       
    print(hamming_distance)