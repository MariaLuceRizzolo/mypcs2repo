if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
mylist = list(set(arr)) 
mylist.sort()
highest = max(mylist)
mylist.remove(highest)
runnerup = max(mylist)
print(runnerup)