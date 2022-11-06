import math
import os
import random
import re
import sys

def timeConversion(s):
    time_format=s[-2:]
    hours=s[0:2]
    minutes=s[3:5]
    seconds=s[6:8]
    
    if time_format=="PM" and int(hours)<12:
        hours=str(int(hours)+12)
    elif time_format=="AM" and hours=='12':
        hours="00"

    military_time=f'{hours}:{minutes}:{seconds}'
    
    return military_time
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
