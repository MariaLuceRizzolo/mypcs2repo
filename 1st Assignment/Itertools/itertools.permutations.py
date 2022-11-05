from itertools import permutations

S, k = input().split(' ')

my_list = list(permutations(sorted(S),int(k)))

for i in my_list:
    print(''.join(i))
