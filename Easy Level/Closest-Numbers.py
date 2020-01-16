#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:30:41 2020

@author: suryakantkumar
"""

'''
Problem : Sorting is useful as the first step in many different tasks. 
The most common task is to make finding things easier, but there are other uses as well. 
In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

For example, if you've got the list [5, 2, 3, 4, 1], sort it as [1, 2, 3, 4, 5] to see that several pairs have the minimum difference of : 
1: [(1, 2), (2, 3), (3, 4), (4, 5)]. The return array would be [1, 2, 2, 3, 3, 4, 4 ,5].

Given a list of unsorted integers, arr, find the pair of elements that have the smallest absolute difference between them. 
If there are multiple pairs, find them all.
'''


import os

def closestNumbers(arr):
    li = sorted(arr)

    min_diff = li[1] - li[0]
    for i in range(1, len(li)):
        if li[i] - li[i -1] < min_diff:
            min_diff = li[i] - li[i -1]
            
    result = []
    for i in range(1, len(li)):
        if li[i] - li[i-1] == min_diff:
            result.append(li[i-1])
            result.append(li[i])
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()