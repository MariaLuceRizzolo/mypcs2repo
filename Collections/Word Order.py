from collections import Counter
n=int(input())
lst=list()

for i in range (0,n):
    lst.append(input())
 
words=Counter(lst)
print(len(words))
print(*words.values())
