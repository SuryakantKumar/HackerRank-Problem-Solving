#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:39:02 2020

@author: suryakantkumar
"""

'''
problem : The median of a list of numbers is essentially it's middle element after sorting. The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, can you find the median?

For example, the median of arr = [1, 2, 3, 4, 5] is 3, the middle element in the sorted array.
'''


import os

def partition(li, si, ei):
    pivot = li[si]

    count = 0
    for i in range(si, ei+1):
        if li[i] < pivot:
            count += 1
    
    pivot_index = si + count

    li[si], li[si + count] = li[si + count], li[si]

    i = si
    j = ei
    while i < j:
        if li[i] < pivot:
            i += 1
        elif li[j] >= pivot:
            j -= 1
        else:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
    
    return pivot_index

def QuickSort(li, si, ei):
    if si >= ei:
        return
    
    pivot_index = partition(li, si, ei)

    QuickSort(li, si, pivot_index - 1)
    QuickSort(li, pivot_index + 1, ei)

    return li

def findMedian(a):
    a = QuickSort(a, 0, len(a)-1)

    return a[len(a)//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)
    fptr.write(str(result) + '\n')
    fptr.close()