with open("3rd Assignment/rosalind_rna.txt") as file:
    sequence = file.readlines()

    RNA = sequence[0].replace('T','U')
    print(RNA)