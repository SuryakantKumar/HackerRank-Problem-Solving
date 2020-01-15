#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:43:10 2020

@author: suryakantkumar
"""

'''
Problem : This is a simple challenge to get things started. Given a sorted array (arr) and a number (V), 
can you print the index location of V in the array?

For example, if arr = [1, 2, 3] and V = 3, you would print 2 for a zero-based index array.

If you are going to use the provided code for I/O, this next section is for you.
'''


import os

def introTutorial(V, arr):
    si = 0
    ei = len(arr) - 1

    while si <= ei:
        mid = (si + ei)// 2

        if arr[mid] == V:
            return mid
        elif arr[mid] > V:
            ei = mid - 1
        else:
            si = mid + 1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    V = int(input())
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = introTutorial(V, arr)
    fptr.write(str(result) + '\n')
    fptr.close()