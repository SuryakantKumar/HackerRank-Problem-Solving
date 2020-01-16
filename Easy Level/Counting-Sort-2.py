#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:44:17 2020

@author: suryakantkumar
"""

'''
Problem : Often, when a list is sorted, the elements being sorted are just keys to other values. 
For example, if you are sorting files by their size, the sizes need to stay connected to their respective files. 
You cannot just take the size numbers and output them in order, you need to output all the required file information.

The counting sort is used if you just need to sort a list of integers. 
Rather than using a comparison, you create an integer array whose index range covers the entire range of values in your array to sort. 
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

Now we can print the sorted array: sorted = [1, 1, 1, 2, 3].

Challenge : 
Given an unsorted list of integers, use the counting sort method to sort the list and then print the sorted list.

Hint: You can use your previous code that counted the items to print out the actual values in order.
'''


import os

def countingSort(arr):
    maxx = max(arr)
    li = [0]*(maxx + 1)

    for i in range(len(arr)):
        val = arr[i]
        li[val] += 1

    result = []
    for i in range(len(li)):
        if li[i] != 0:
            for j in range(li[i]):
                result.append(i)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()