import math

with open("3rd Assignment/rosalind_prob.txt") as file:
    probs = []
    AT = 0
    GC = 0

    sequence = file.readline()
    GC_content = [float(i) for i in file.readline().strip().split()]

    for i in sequence:
        if i == 'A' or i == 'T':
            AT += 1
        elif i == 'G' or i == 'C':
            GC += 1

    for i in range(len(GC_content)):
        probability = (((1 - GC_content[i])/2)**AT) * (GC_content[i]/2)**GC
        commonlog = math.log10(probability)

        probs.append('%.3f'%commonlog)

    print(' '.join(probs))