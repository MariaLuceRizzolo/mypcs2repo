with open("3rd Assignment/rosalind_dna.txt") as file:
    sequence = file.readline()

    A = sequence[0].count('A')
    C = sequence[0].count('C')
    G = sequence[0].count('G')
    T = sequence[0].count('T')

    print(f'{A} {C} {G} {T}')

