#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:34:15 2020

@author: suryakantkumar
"""

'''
Problem : The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm with a running time of O(n). 
In these next few challenges, we're covering a divide-and-conquer algorithm called Quicksort (also known as Partition Sort). 
This challenge is a modified version of the algorithm that only addresses partitioning. It is implemented as follows:

Step 1: Divide
Choose some pivot element, p, and partition your unsorted array, arr, into three smaller arrays: left, right, and equal, 
where each element in left < p, each element in right > p, and each element in equal = p.

Given arr and p = arr[0], partition arr into left, right, and equal using the Divide instructions above. 
Then print each element in left followed by each element in equal, followed by each element in right on a single line. 
Your output should be space-separated and does not have to maintain ordering of the elements within the three categories.
'''


import os

def quickSort(arr):
    pivot = arr[0]

    left = []
    right = [pivot]
    equal = []
    for e in arr[1:]:
        if e < pivot:
            left.append(e)
        elif e > pivot:
            right.append(e)
        else:
            equal.append(e)
    
    final = left + equal + right
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()