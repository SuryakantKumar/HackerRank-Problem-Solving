#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:41:56 2020

@author: suryakantkumar
"""

'''
Problem : You are given two arrays, A and B, both containing N integers.

A pair of indices (i, j) is beautiful if the ith element of array A is equal to the Jth element of array B. 
In other words, pair (i, j) is beautiful if and only if A[i] = B[j]. A set containing beautiful pairs is called a beautiful set.

A beautiful set is called pairwise disjoint if for every pair (l[i], r[i]) belonging to the set there is no repetition of either l[i] or r[i] values. 
For instance, if A = [10, 11, 12, 5, 14] and B = [8, 9, 11, 11, 5] the beautiful set [(1, 2), (1, 3), (3, 4)] is not pairwise disjoint as there is a repetition of 1, that is l[0][0] = l[1][0].

Your task is to change exactly 1 element in B so that the size of the pairwise disjoint beautiful set is maximum.
'''


import os

def beautifulPairs(a, b):
    a = sorted(a)
    b = sorted(b)

    if a == b:
        return len(a) - 1

    freq_a = {}
    for e in a:
        if e in freq_a:
            freq_a[e] += 1
        else:
            freq_a[e] = 1

    a_unique = 0
    val = 12345
    for i in range(len(a)):
        if a[i] not in b:
            if a[i] == val:
                a_unique += 1
            else:
                val = a[i]
                a_unique = 1

    freq_b = {}
    for e in b:
        if e in freq_b:
            freq_b[e] += 1
        else:
            freq_b[e] = 1

    count = 0
    for e in freq_a:
        if e in freq_b:
            if freq_a[e] == freq_b[e]:
                count += freq_a[e]
            else:
                diff = freq_a[e] if freq_a[e] < freq_b[e] else freq_b[e]
                count += diff
                
    if a_unique > 0:
        count += 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    result = beautifulPairs(A, B)
    fptr.write(str(result) + '\n')
    fptr.close()