from itertools import groupby 

S = input()
S_grouped = groupby(S)

for a, b in S_grouped:
    print(tuple([len(list(b)), int(a)]), end = " ")
