#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:21:12 2020

@author: suryakantkumar
"""

'''
Problem : Another sorting method, the counting sort, does not require comparison. 
Instead, you create an integer array whose index range covers the entire range of values in your array to sort. 
Each time a value occurs in the original array, you increment the counter at that index. 
At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

For example, consider an array arr = [1, 1, 3, 2, 1]. All of the values are in the range [0...3], 
so create an array of zeroes, result = [0, 0, 0, 0]. The results of each iteration follow:

i	arr[i]	result
0	1	    [0, 1, 0, 0]
1	1	    [0, 2, 0, 0]
2	3	    [0, 2, 0, 1]
3	2	    [0, 2, 1, 1]
4	1	    [0, 3, 1, 1]

Now we can print the list of occurrences, 0 3 1 1 or determine the sorted array: sorted = [1, 1, 1, 2, 3].

Challenge : 
    
Given a list of integers, count and output the number of times each value appears as a list of space-separated integers.
'''


import os

def countingSort(n, arr):
    maxx = max(arr)

    li = [0]*(maxx + 1)

    for i in range(len(arr)):
        val = arr[i]
        li[val] += 1

    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(n, arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()