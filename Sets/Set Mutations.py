a = int(input())
A = set(map(int,input().split()))
b = int(input())

for i in range(0,b):
    tmp=input().split()
    cmd=tmp[0]

    set_new = set(map(int,input().split()))
    
    
    if cmd== "intersection_update":
        A.intersection_update(set_new)
    elif cmd== "update":
        A.update(set_new)
    elif cmd== "symmetric_difference_update":
        A.symmetric_difference_update(set_new)
    elif cmd== "difference_update":
        A.difference_update(set_new)
print(sum(A))
