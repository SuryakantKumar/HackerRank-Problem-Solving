#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 15:46:01 2020

@author: suryakantkumar
"""

'''
Problem : Calvin is driving his favorite vehicle on the 101 freeway. 
He notices that the check engine light of his vehicle is on, 
and he wants to service it immediately to avoid any risks. Luckily, a service lane runs parallel to the highway. 
The service lane varies in width along its length.

You will be given an array of widths at points along the road (indices), 
then a list of the indices of entry and exit points. 
Considering each entry and exit point pair, calculate the maximum size vehicle that can travel that segment of the service lane safely.

For example, there are n = 4 measurements yielding width = [2, 3, 2, 1]. 
If our entry index, i = 1 and our exit, j = 2, there are two segment widths of 2 and 3 respectively. 
The widest vehicle that can fit through both is 2. If i = 2 and j = 4, our widths are [3, 2, 1] which limits vehicle width to 1.
'''



import os

def serviceLane(n, cases, width):
    li = []
    for ele in cases:
        start = int(ele[0])
        end = int(ele[1])

        widest = 123456789
        for i in range(start, end + 1):
            if width[i] < widest:
                widest = width[i]
        li.append(widest)
        
    return li
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nt = input().split()
    n = int(nt[0])
    t = int(nt[1])
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(str, input().rstrip().split())))
    result = serviceLane(n, cases, width)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()