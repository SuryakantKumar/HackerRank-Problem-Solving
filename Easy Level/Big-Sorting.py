#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:54:06 2020

@author: suryakantkumar
"""

'''
Problem : Consider an array of numeric strings where each string is a positive number with anywhere from 1 to 10^6 digits. 
Sort the array's elements in non-decreasing, or ascending order of their integer values and print each element of the sorted array on a new line.
'''

import os

def compare(a, b):
    if len(a) < len(b):
        return True
    
    elif len(a) > len(b):
        return False
    
    else:
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
                
            elif a[i] > b[j]:
                return False
            
            elif a[i] < b[j] :
                return True
            
        return True
    
def Merge(li1, li2, li):
    i = 0
    j = 0
    k = 0
    while i < len(li1) and j < len(li2):
        if compare(li1[i], li2[j]) == True:
            li[k] = li1[i]
            k += 1
            i += 1
        else:
            li[k] = li2[j]
            k += 1
            j += 1
    
    while i < len(li1):
        li[k] = li1[i]
        k += 1
        i += 1
    
    while j < len(li2):
        li[k] = li2[j]
        k += 1
        j += 1 

def bigSorting(li):
    if len(li) == 0 or len(li) == 1:
        return 
    
    mid = len(li)//2
    
    li1 = li[0:mid] 
    li2 = li[mid:]
    
    bigSorting(li1) 
    bigSorting(li2)
    
    Merge(li1, li2, li)                    

    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    result = bigSorting(unsorted)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()