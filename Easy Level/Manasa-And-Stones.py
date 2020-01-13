#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:26:14 2020

@author: suryakantkumar
"""

'''
Problems : Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. 
She starts following the trail and notices that any two consecutive stones' numbers differ by one of two values. 
Legend has it that there is a treasure trove at the end of the trail. 
If Manasa can guess the value of the last stone, the treasure will be hers.

For example, assume she finds 2 stones and their differences are a = 2 or b = 3. 
We know she starts with a 0 stone not included in her count. 
The permutations of differences for the two stones would be [2, 2], [2, 3], [3,2] or [3, 3]. 
Looking at each scenario, stones might have [2, 4], [2, 5], [3, 5] or [3, 6] on them. 
The last stone might have any of 4, 5 or 6 on its face.

Compute all possible numbers that might occur on the last stone given a starting stone with a 0 on it, 
a number of additional stones found, and the possible differences between consecutive stones. Order the list ascending.
'''


import os

def stones(n, a, b):
    final = [a, b]
    if n <= 2:
        return set(final)
        
    for i in range(n - 2):
        pre = set()
        for ele in final:
            pre.add(ele + a)
            pre.add(ele + b)
        final = list(pre)
    
    return sorted(final)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input())
    for T_itr in range(T):
        n = int(input())
        a = int(input())
        b = int(input())
        result = stones(n, a, b)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()