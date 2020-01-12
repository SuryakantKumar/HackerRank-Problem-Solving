#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 6 10:44:02 2020

@author: suryakantkumar
"""

'''
Problem : Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:
1 2 3
4 5 6
9 8 9  

The left-to-right diagonal 1 + 5 + 9 = 15. The right to left diagonal 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2.
'''


import os

def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    
    for i in range(n):
        sum1 += arr[i][i]
        
    for k in range(n-1, -1, -1):
        sum2 += arr[n-k-1][k]
        
    diff = sum1 - sum2
    if diff < 0 :
        diff = sum2 - sum1
        
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
    
