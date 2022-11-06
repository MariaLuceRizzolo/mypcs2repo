import math
import os
import random
import re
import sys

def runningTime(arr):
    n=len(arr)
    running_time=0
    
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while (j>=0) and (arr[j]>key):
           arr[j+1]=arr[j]
           j-=1
           running_time+=1
        arr[j+1]=key
        
    return running_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
