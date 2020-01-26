#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:53:39 2020

@author: suryakantkumar
"""

'''
Problem : Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.

For example, the array S = [19, 10, 12, 24, 25, 22] and k = 4. One of the arrays that can be created is S'[0] = [10, 12, 25]. 
Another is S'[1] = [19, 22, 24]. After testing all permutations, the maximum length solution array has 3 elements.
'''


#### Solution 01 : Ordinary Approach

import os

def AllSet(ele, x, k):
    for i in x:
        if (i + ele) % k == 0:
            return False
    return True
    
def nonDivisibleSubset(k, s):
    f = {}
    for e in s:
        f[e] = [e]
        
    for ele in s:
        for e in f:
            if ele != e and AllSet(ele, f[e], k) == True:
                f[e].append(ele)

    maxx = 0
    for e in f:
        if len(f[e]) > maxx:
            maxx = len(f[e])
    
    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, s)
    fptr.write(str(result) + '\n')
    fptr.close()


#### Solution 02 : Optimal Approach
    
import os

def nonDivisibleSubset(k, s):
    new = [i % k for i in s]
    counter = [0] * k
    for r in new:
        counter[r] += 1
        
    count = min(counter[0], 1)

    for i in range(1, (k//2)+1):
        if i != k-i:
            count += max(counter[i], counter[k-i])
        else:
            count += min(counter[i], 1)
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, s)
    fptr.write(str(result) + '\n')
    fptr.close()