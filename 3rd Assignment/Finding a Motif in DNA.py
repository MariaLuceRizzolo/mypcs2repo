with open("3rd Assignment/rosalind_subs.txt") as file:
    input = file.read()

    sequence, motif = input.splitlines()

    for location in range(len(sequence)):
        if sequence[location:].startswith(motif):
            print(location+1)