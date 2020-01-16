#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:18:31 2020

@author: suryakantkumar
"""

'''
Problem : Sunny and Johnny like to pool their money and go to the ice cream parlor. 
Johnny never buys the same flavor that Sunny does. The only other rule they have is that they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

For example, they have m = 6 to spend and there are flavors costing cost = [1, 3, 4 ,5 ,6]. 
The two flavors costing 1 and 5 meet the criteria. Using 1-based indexing, they are at indices  and .
'''


import os

def icecreamParlor(m, arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                return [i+1, j+1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        m = int(input())
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()