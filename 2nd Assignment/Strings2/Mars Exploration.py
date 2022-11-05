import math
import os
import random
import re
import sys

def marsExploration(s):
    count=0
    n=len(s)
    sub='SOS'
     
    for i in range(n):
        if s[i]!=sub[i%3]:
            count+=1
        
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
