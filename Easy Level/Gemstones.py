#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:51:11 2020

@author: suryakantkumar
"""

'''
Problem : John has collected various rocks. Each rock has various minerals embeded in it. 
Each type of mineral is designated by a lowercase letter in the range ascii[a - z]. 
There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in each of the rocks in John's collection.

Given a list of minerals embedded in each of John's rocks, display the number of types of gemstones he has in his collection.

For example, the array of mineral composition strings arr = [abc, abc, bc]. 
The minerals b and c appear in each composite, so there are 2 gemstones.
'''


import os

def gemstones(arr):
    count = 0
    for i in range(ord('a'), ord('z') +1):
        flag = True
        for e in arr:
            if chr(i) not in e:
                flag = False
        if flag == True:
            count += 1

    return count
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    fptr.write(str(result) + '\n')
    fptr.close()