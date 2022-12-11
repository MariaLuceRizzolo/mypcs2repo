import math                                         
import itertools  

with open("4th Assignment/rosalind_perm.txt") as file:
    n = int(file.read())
                                              
    total = math.factorial(n)
    print(total)

    perm = list(itertools.permutations(range(1, n + 1)))    

    for i in perm:
        permutation = ''
        for j in i:
            permutation += str(j) + ' '
        print(permutation)