from collections import defaultdict

n,m = map(int, input().split())
dict_A = defaultdict(list)
dict_B = []

for i in range (0,n):
    dict_A[input()].append(str(i+1))
    
for i in range (0,m):
    dict_B.append(input())
 
    
for i in dict_B:
    if i in dict_A.keys():
       print (' '.join(dict_A[i]))
    else:
         print ('-1')
