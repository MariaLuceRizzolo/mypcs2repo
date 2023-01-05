import re
import requests

def get_file (id):
    file = requests.get(f"http://www.uniprot.org/uniprot/{id}.fasta").text
    return "".join(line.strip() for line in file.splitlines()[1:])

with open("5th Assignment/rosalind_mprt.txt") as file:
    ids = file.readlines()

    N_glycosylation_motif = re.compile(r'(?=[N][^P][ST][^P])')
    for i in ids:
        seq = get_file(i)
        pos = []
        for j in re.finditer(N_glycosylation_motif, seq):
            pos.append(j.start()+1)
        if len(pos) > 0:
            print(i)
            print(' '.join([str(p) for p in pos]))


