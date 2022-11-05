from itertools import combinations_with_replacement

S, k = input().split(' ')
my_list = list(combinations_with_replacement(sorted(S),int(k)))

for i in my_list:
    print(''.join(i))