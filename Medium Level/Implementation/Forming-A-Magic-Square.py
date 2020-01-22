#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:52:53 2020

@author: suryakantkumar
"""

'''
Problem : We define a magic square to be an n * n matrix of distinct positive integers from 1 to n^2 
where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

You will be given a 3 * 3 matrix s of integers in the inclusive range [1, 9]. 
We can convert any digit a to any other digit b in the range [1, 9] at cost of |a - b|. 
Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range [1, 9].

For example, we start with the following matrix s:
5 3 4
1 5 8
6 4 2

We can convert it to the following magic square:
8 3 4
1 5 9
6 7 2

This took three replacements at a cost of |5 - 8| + |8 - 9| + |4 - 7| = 7.
'''


import os

def formingMagicSquare(s):
    n = [s[i][j] for i in range(3) for j in range(3)]
    
    all_n = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
             [6, 1, 8, 7, 5, 3, 2, 9, 4],
             [4, 9, 2, 3, 5, 7, 8, 1, 6],
             [2, 9, 4, 7, 5, 3, 6, 1, 8],
             [8, 3, 4, 1, 5, 9, 6, 7, 2],
             [4, 3, 8, 9, 5, 1, 2, 7, 6],
             [6, 7, 2, 1, 5, 9, 8, 3, 4],
             [2, 7, 6, 9, 5, 1, 4, 3, 8]]
    
    allsum = []
    
    for l in all_n:
        allsum.append(sum([abs(n[i]-l[i]) for i in range(9)]))
        
    return min(allsum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()