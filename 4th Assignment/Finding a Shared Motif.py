data = open('4th Assignment/rosalind_lcsm.txt').read().split('>')[1:]
dataset = []

for i in range(len(data)):
    row = data[i].split('\n',1)
    dataset.append(row[1].replace('\n',''))

srt_seq = sorted(dataset, key=len)     
shortest = srt_seq[0]
min_len = len(shortest)                                       
substring = ''

for i in range(min_len):
    for j in range(i, min_len):
        if (j-i) > len(substring):
            present = True
            for s in dataset[1:]:
                if shortest[i:1+j] not in s:
                    present = False
            if present:
                substring = shortest[i:1+j]

print(substring)

