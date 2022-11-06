import math
import os
import random
import re
import sys

def findMedian(arr):
    new_arr=sorted(arr)
    median=new_arr[len(arr)//2]
    
    return median

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
