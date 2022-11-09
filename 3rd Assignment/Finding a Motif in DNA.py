with open("3rd Assignment/rosalind_subs.txt") as file:
    text = file.read()

    sequence, motif = text.splitlines()

    for location in range(len(sequence)):
        if sequence[location:].startswith(motif):
            print(location+1)