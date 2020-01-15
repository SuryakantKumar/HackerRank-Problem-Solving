#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:42:27 2020

@author: suryakantkumar
"""

'''
Program : In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. 
Using the same approach repeatedly, can you sort an entire array?

Guideline: You already can place an element into a sorted array. 
How can you use that code to build up a sorted array, one element at a time? 
Note that in the first step, when you consider an array with just the first element, 
it is already sorted since there's nothing to compare it to.

In this challenge, print the array after each iteration of the insertion sort, 
i.e., whenever the next element has been inserted at its correct position. 
Since the array composed of just the first element is already sorted, begin printing after placing the second element.

For example, there are n = 7 elements in arr = [3, 4, 7, 5, 6, 2, 1]. Working from left to right, we get the following output:

3 4 7 5 6 2 1
3 4 7 5 6 2 1
3 4 5 7 6 2 1
3 4 5 6 7 2 1
2 3 4 5 6 7 1
1 2 3 4 5 6 7
'''


def insertionSort2(n, arr):
    
    for i in range(1, n):
        consider = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > consider:
            if arr[j] > consider:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = consider
        print(*arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)