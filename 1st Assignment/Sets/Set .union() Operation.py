n = int(input())
english_newspaper = set(map(int,input().split()))

b = int(input())
french_newspaper = set(map(int,input().split()))

subscribed = english_newspaper.union(french_newspaper)
print(len(subscribed))
