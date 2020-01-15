#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:44:53 2020

@author: suryakantkumar
"""

'''
Problem : In the InsertionSort code below, there is an error. 
Can you fix it? Print the array only once, when it is fully sorted.
'''


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
        
    return

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))