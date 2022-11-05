import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n=len(arr)
    i=0
    firstdiagonal=0
    seconddiagonal=0
    
    for i in range(n):
        firstdiagonal+=arr[i][i]
        seconddiagonal+=arr[i][n-i-1]

    abs_difference=abs(firstdiagonal-seconddiagonal)
    
    return abs_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
