#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 00:40:17 2020

@author: suryakantkumar
"""

'''
Problem : Consider two n-element arrays of integers, A = [A[0], A[1],....,A[n-1]] and B = [B[0], B[1],....,B[n-1]]. 
You want to permute them into some A' and B' such that the relation A'[i] + B'[i] >= k holds for all i where 0 <= i < n. 
For example, if A = [0, 1], B = [0, 2], and k = 1, a valid A', B' satisfying our relation would be A' = [1, 0] and B' = [2, 0], 1 + 0 >= 1 and 0 + 2 >= 2.

You are given q queries consisting of A, B, and k. For each query, print YES on a new line if some permutation A', B' satisfying the relation above exists. 
Otherwise, print NO.
'''

import os

def twoArrays(k, A, B):
    a = sorted(A)
    a = a[::-1]

    b = sorted(B)

    for i in range(len(a)):
        if a[i] + b[i] < k:
            return 'NO'
    return 'YES'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        result = twoArrays(k, A, B)
        fptr.write(result + '\n')
    fptr.close()