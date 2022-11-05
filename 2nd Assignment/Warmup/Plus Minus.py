import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    n=len(arr)
    
    for i in range(n):
        if arr[i]>0:
            pos+=1
        elif arr[i]<0:
            neg+=1
        else:
            zer+=1
            
    print('%.6f'%(pos/len(arr)))
    print('%.6f'%(neg/len(arr)))
    print('%.6f'%(zer/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
