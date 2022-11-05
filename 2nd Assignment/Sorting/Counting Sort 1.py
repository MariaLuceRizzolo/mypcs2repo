import math
import os
import random
import re
import sys

def countingSort(arr):
    frequency=[] 
    item=0 
    count=0
    n=len(arr)
    
    while(item<100): 
        for i in range(n):
            if(arr[i]==item):
                count+=1
        item+=1
        frequency.append(count)
        count=0
          
    return frequency

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
