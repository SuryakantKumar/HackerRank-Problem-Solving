#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 00:46:47 2020

@author: suryakantkumar
"""

'''
Problem : You will be given an array of integers. All of the integers except one occur twice. 
That one is unique in the array.

Given an array of integers, find and print the unique element.

For example, a = [1, 2, 3, 4, 3, 2, 1], the unique element is 4.
'''


import os

def lonelyinteger(a):
    freq = {}

    for e in a:
        if e in freq:
            freq[e] += 1
        else:
            freq[e] = 1

    for e in freq:
        if freq[e] == 1:
            return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    fptr.write(str(result) + '\n')
    fptr.close()