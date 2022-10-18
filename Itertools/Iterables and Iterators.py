from itertools import combinations

N = input()
string = list(input().split(' '))
indices = int(input())

comb = list(combinations(string,indices))
counter = 0

for i in comb:
    if "a" in i:
        counter += 1
        
prob = counter/len(comb)
print('%.3f'%prob)
