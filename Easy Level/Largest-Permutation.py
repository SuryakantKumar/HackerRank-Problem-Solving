#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:27:38 2020

@author: suryakantkumar
"""

'''
Problem : You are given an unordered array of unique integers incrementing from 1. 
You can swap any two elements a limited number of times. 
Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.

For example, if arr = [1, 2, 3, 4] and the maximum swaps k = 1, the following arrays can be formed by swapping the 1 with the other elements:

[2,1,3,4]
[3,2,1,4]
[4,2,3,1]
The highest value of the four (including the original) is [4, 2, 3, 1]. If k >= 2, we can swap to the highest possible value: [4, 3, 2, 1].
'''


#### Solution 01 : Ordinary Approach

def largestPermutation(k, arr):
    if k >= len(arr) :
        arr = sorted(arr)
        return arr[::-1]

    else:
        i = 0
        while i < k:
            pos1 = i
            if arr[pos1] == len(arr) - pos1:
                k += 1
            else:
                pos2 = -1
                for j in range(pos1+1, len(arr)):
                    if arr[j] == len(arr) - pos1:
                        pos2 = j
                        break
                
                arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
            i += 1
        return arr

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)
    print(*result)
    


#### Solution 02: Optimal Approach
    
def largestPermutation(k, arr):
    freq = {V: I for I, V in enumerate(arr)}
    maxx = len(arr)
    i = 0
    while k and maxx:
        consider = arr[i]
        max_val_index = freq[maxx]
        
        if max_val_index != i:
            arr[i] = maxx
            arr[max_val_index] = consider
            freq[consider] = max_val_index
            freq[maxx] = freq[consider]
            k -= 1
            
        i += 1
        maxx -= 1

    return arr

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)
    print(*result)