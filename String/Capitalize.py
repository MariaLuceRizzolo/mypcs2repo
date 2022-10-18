
import math
import os
import random
import re
import sys

def solve(s):
    splitted = s.split()
    for i in splitted:
        word = i
        capitalized = word.capitalize()

        s = s.replace(word,capitalized)

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
