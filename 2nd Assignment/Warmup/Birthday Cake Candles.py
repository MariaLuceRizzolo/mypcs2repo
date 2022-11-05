import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    max_height= max(candles)
    counter=0
    n= len(candles)
    
    for i in range(n):
        if candles[i]==max_height:
            counter+=1
    
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
