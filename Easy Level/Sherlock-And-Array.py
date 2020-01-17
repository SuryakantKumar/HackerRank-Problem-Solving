#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:00:38 2020

@author: suryakantkumar
"""

'''
Problem : Watson gives Sherlock an array of integers. 
His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right. 
For instance, given the array arr = [5, 6, 8, 11], 8 is between two subarrays that sum to 11. 
If your starting array is [1], that element satisfies the rule as left and right sum to 0.

You will be given arrays of integers and must determine whether there is an element that meets the criterion.
'''


import os

def balancedSums(arr):
    if len(arr) == 1:
        return 'YES'
    elif len(arr) == 2:
        if arr[0] == arr[1]:
            return 'YES'
        elif arr[0] == 0 or arr[1] == 0:
            return 'YES'
        else:
            return 'NO'
    
    ls = 0          # Left Sum
    rs = 0          # Right Sum
    for e in arr:
        rs += e
    
    for i in range(len(arr)):
        if i == 0:
            rs -= arr[0]
        else:
            ls += arr[i -1]
            rs -= arr[i]

        if ls == rs :
            return 'YES'

    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        fptr.write(result + '\n')
    fptr.close()