import itertools

with open('4th Assignment/rosalind_lexf.txt') as file:
    sequence = file.readline().strip().split()
    n = int(file.readline())

    output = []

    perm = list(itertools.product(sequence, repeat = n))

    for i in perm:
        permutation = ''
        for j in i:
            permutation += j
        output.append(permutation)
        
    print('\n'.join(sorted(output)))  

