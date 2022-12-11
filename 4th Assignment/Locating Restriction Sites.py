data = open('4th Assignment/rosalind_revp.txt').read().split('>')[1:]
sequence = []
for i in range(len(data)):
    row = data[i].split('\n',1)
    sequence.append(row[1].replace('\n',''))
sequence = sequence[0]

for i in range(len(sequence)):
    for j in range(i,len(sequence)):
        string1 = str(sequence[i:1+j])
        complement = string1.translate(str.maketrans('ACTG', 'TGAC'))
        reverse = complement[::-1]

        if len(string1) >= 4 and len(string1) <= 12:
            if string1 == reverse:
                pos = i + 1                
                print(pos, len(string1))




    