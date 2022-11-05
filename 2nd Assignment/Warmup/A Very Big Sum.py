import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    bigresult=0
    n=len(ar)
    
    for i in range (n):
        bigresult+=ar[i]
        
    return bigresult

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
