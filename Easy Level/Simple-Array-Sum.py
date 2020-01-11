#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 6 10:08:44 2020

@author: suryakantkumar
"""

'''
Problem : Given an array of integers, find the sum of its elements.

For example, if the array ar = [1, 2, 3], 1 + 2 + 3 = 6, so return 6.
'''


import os

def simpleArraySum(arr):
    result = 0
    for ele in arr:
        result += ele
    return result

if __name__ == '__main__': 
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()