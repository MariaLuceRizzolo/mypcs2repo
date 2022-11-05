import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    new_arr=sorted(arr)
    
    min_sum=0
    min_=new_arr[0:4]
    
    for i in (min_):
        min_sum+=i  
    
    max_sum=0
    max_=new_arr[-4:]
    
    for i in (max_):
        max_sum+=i
        
    print(str(min_sum)+' '+str(max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
