#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:42:59 2020

@author: suryakantkumar
"""

'''
Problem : Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.
1. Swap two elements.
2. Reverse one sub-segment.

Determine whether one, both or neither of the operations will complete the task. If both work, choose swap. For instance, given an array [2, 3, 5, 4] either swap the 4 and 5, or reverse them to sort the array. 
Choose swap. The Output Format section below details requirements.
'''


def sorted_li(li):
    if li == sorted(li):
        return True
    return False

def almostSorted(arr):
    l = arr

    i = 0
    start = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            start = i
            break
        i += 1
    
    j = start + 1
    mini = 12345678
    while j < len(arr):
        if arr[j] < arr[start]:
            mini = j
        j += 1

    l[start], l[mini] = l[mini], l[start]
    if sorted_li(l) == True:
        print('yes')
        print('swap', start + 1, mini +1)
        
    elif sorted_li(l) == False:
        l[start + 1 : mini] = l[mini - 1 : start: -1]
        if sorted_li(l) == True:
            print('yes')
            print('reverse', start + 1, mini + 1)  
            
        else:
            print('no')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    almostSorted(arr)