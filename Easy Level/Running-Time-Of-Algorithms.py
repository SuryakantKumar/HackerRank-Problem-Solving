#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:32:21 2020

@author: suryakantkumar
"""

'''
Problem : Can you modify your previous Insertion Sort implementation to keep track of the number of shifts it makes while sorting? 
The only thing you should print is the number of shifts made by the algorithm to completely sort the array. 
A shift occurs when an element's position changes in the array. Do not shift an element if it is not necessary.
'''


import os

def runningTime(arr):
    count_shift = 0
    for i in range(1, len(arr)):
        consider = arr[i]
        
        j = i - 1
        while j >= 0 and arr[j] > consider:
            arr[j+1] = arr[j]
            count_shift += 1
            j -= 1
            
        arr[j+1] = consider

    return count_shift


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = runningTime(arr)
    fptr.write(str(result) + '\n')
    fptr.close()