#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:23:38 2020

@author: suryakantkumar
"""

'''
Problem : Numeros the Artist had two lists that were permutations of one another. 
He was very proud. Unfortunately, while transporting them from one exhibition to another, 
some numbers were lost out of the first list. Can you find the missing numbers?

As an example, the array with some numbers missing, arr = [7, 2, 5, 3, 5, 3]. 
The original array of numbers brr = [7, 2, 5, 4, 6, 3, 5, 3]. The numbers missing are [4, 6].

Notes : 
• If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. 
If that is not the case, then it is also a missing number.

• You have to print all the missing numbers in ascending order.
• Print each missing number once, even if it is missing multiple times.
• The difference between maximum and minimum number in the second list is less than or equal to .
'''


import os

def missingNumbers(arr, brr):
    fa = {}
    for e in arr: 
        if e in fa:
            fa[e] += 1
        else:
            fa[e] = 1

    fb = {}
    for e in brr:
        if e in fb:
            fb[e] += 1
        else:
            fb[e] = 1

    li = []

    for x in fb:
        if x in fa:
            if fb[x] > fa[x]:
                li.append(x)
        else:
            li.append(x)
    
    return sorted(li)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    m = int(input())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()