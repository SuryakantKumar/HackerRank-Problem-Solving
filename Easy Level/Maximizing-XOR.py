#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 09:50:49 2020

@author: suryakantkumar
"""

'''
Problem : Given two integers, l and r, find the maximal value of a xor b, 
written a ^ b, where a and b satisfy the following condition:
l <= a <= b <= r

For example, if l = 11 and r = 12, then
11 ^ 11 = 0
11 ^ 12 = 7
12 ^ 12 = 0

Our maximum value is 7.
'''


import os

def maximizingXor(l, r):
    maxx = -12345678
    for i in range(l, r+1):
        for j in range(i, r+1):
            if i^j > maxx:
                maxx = i^j

    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input())
    r = int(input())
    result = maximizingXor(l, r)
    fptr.write(str(result) + '\n')
    fptr.close()
