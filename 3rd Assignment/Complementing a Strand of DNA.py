with open("3rd Assignment/rosalind_revc.txt") as file:
    sequence = file.readline()

    complement = sequence[0].translate(str.maketrans('ACTG', 'TGAC'))
    reverse = complement[::-1]

    print(reverse)