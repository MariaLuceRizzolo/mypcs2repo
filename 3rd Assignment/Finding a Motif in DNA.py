with open("3rd Assignment/rosalind_subs.txt") as file:
    sequences = file.read()

    sequence, motif = sequences.splitlines()

    for location in range(len(sequence)):
        if sequence[location:].startswith(motif):
            print(location+1)