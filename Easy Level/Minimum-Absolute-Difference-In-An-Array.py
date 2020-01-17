#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:18:07 2020

@author: suryakantkumar
"""

'''
Problem : Consider an array of integers, arr = [arr[0], arr[1]....arr[n]]. 
We define the absolute difference between two elements, a[i] and a[j] (where i ≠ j), to be the absolute value of a[i] - a[j].

Given an array of integers, find and print the minimum absolute difference between any two elements in the array. 
For example, given the array arr = [-2, 2, 4] we can create 3 pairs of numbers: [-2, 2], [-2, 4] and [2, 4]. 
The absolute differences for these pairs are 4, 6 and 2. The minimum absolute difference is 2.
'''

import os

def minimumAbsoluteDifference(arr):
    absolute = 123456789
    for i in range(0, len(arr)-1):
        for j in range(i +1, len(arr)):
            diff = (arr[i] - arr[j])
            if diff < 0:
                diff *= -1
            if diff < absolute:
                absolute = diff

    return absolute

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()