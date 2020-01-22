#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:23:49 2020

@author: suryakantkumar
"""

'''
Problem : You will be given an array of integers and a target value. 
Determine the number of pairs of array elements that have a difference equal to a target value.

For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: 2 - 1 = 1, 3 -2 = 1, and 4 - 3 = 1.
'''


import os

def pairs(k, arr):
    count =0
    arr.sort()  
  
    l = 0
    r = 0
    while r < len(arr): 
        if arr[r] - arr[l] == k: 
            count += 1
            l += 1
            r += 1
        elif arr[r] - arr[l] > k:  
            l += 1
        else: 
            r += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()