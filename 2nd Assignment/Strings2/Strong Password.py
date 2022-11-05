import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    numb=0
    low=0
    up=0
    special=0
    add=0
    numbers="0123456789"
    lower_case="abcdefghijklmnopqrstuvwxyz"
    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters="!@#$%^&*()-+"
    
    
    for i in password:
        if i in numbers:
            numb+=1
        if i in lower_case:
            low+=1
        if i in upper_case:
            up+=1
        if i in special_characters:
            special+=1

    if numb==0:
        add+=1
    if low==0:
        add+=1   
    if up==0:
        add+=1 
    if special==0:
        add+=1 
        
    return max(add, 6-n) 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
