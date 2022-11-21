import math
import os
import random
import re
import sys

def funnyString(s):
    r=s[::-1]
    ascii_r=[]
    ascii_s=[]
    diff_s=[]
    diff_r=[]

    for i in range (len(s)):
        ascii_r.append(ord(r[i]))
        ascii_s.append(ord(s[i]))

    for i in range (len(s)-1):
        diff_s.append(abs(ascii_s[i]-ascii_s[i+1]))
        diff_r.append(abs(ascii_r[i]-ascii_r[i+1]))

    if diff_s==diff_r:
        return ('Funny')
    else:
        return ('Not Funny')
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
