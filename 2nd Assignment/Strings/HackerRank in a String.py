import math
import os
import random
import re
import sys

def hackerrankInString(s):
    hackerrank=list('hackerrank')
    subseq='.*'.join(hackerrank)
    
    if re.search(subseq,s):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
