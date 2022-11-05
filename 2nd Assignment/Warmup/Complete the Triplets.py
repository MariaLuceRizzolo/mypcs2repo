import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    point_first=0
    point_second=0

    for i, j in zip(a,b):
        if i>j:
            point_first+=1
        elif i<j:
            point_second+=1
            
    return point_first, point_second

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
