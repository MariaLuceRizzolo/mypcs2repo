import math
import os
import random
import re
import sys

def quickSort(arr):
    pivot=arr[0]
    j=0
    n=len(arr)
    
    for i in range(1,n):
        if arr[i]<=pivot:
            j+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[0],arr[j]=arr[j],arr[0]
    
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
