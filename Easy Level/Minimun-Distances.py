#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:34:54 2020

@author: suryakantkumar
"""

'''
Problem : We define the distance between two array values as the number of indices between the two values.
Given a, find the minimum distance between any pair of equal elements in the array. If no such value exists, print -1.

For example,if a = [3, 2, 1, 2, 3], there are two matching pairs of values: 3 and 2. The indices of the 3's are i = 0 and j = 4, so their distance is d[i, j] = |j - i| = 4.
The indices of the 2's are i = 1 and j = 3, so their distance is d[i, j] = |j - i| = 2.
'''


import os

def minimumDistances(a):
    min_distance  = 12345678 
    flag = False
    
    for i in range(len(a) - 1):
        for j in range(i +1, len(a)):
            if a[i] == a[j]:
                flag = True
                distance = j - i
                if distance < min_distance:
                    min_distance = distance

    if flag == True:
        return min_distance
    else:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
