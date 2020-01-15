#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:44:17 2020

@author: suryakantkumar
"""

'''
Problem : Two words are anagrams of one another if their letters can be rearranged to form the other word.

In this challenge, you will be given a string. You must split it into two contiguous substrings, 
then determine the minimum number of characters to change to make the two substrings into anagrams of one another.

For example, given the string 'abccde', you would break it into two parts: 'abc' and 'cde'. 
Note that all letters have been used, the substrings are contiguous and their lengths are equal. 
Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. 
Two changes were necessary.
'''


import os

def modulous(a, b):
    if a < b:
        return b - a
    elif a == b:
        return 0
    else:
        return a - b

def anagram(s):
    if len(s) % 2 == 1 or len(s) == 0:
        return -1
    
    half_len = len(s) // 2

    if s[:half_len] == s[half_len:]:
        return 0
    
    map_f = {}
    for e in s[:half_len]:
        if e in map_f:
            map_f[e] += 1
        else:
            map_f[e] = 1
    
    map_l = {}
    for e in s[half_len:]:
        if e in map_l:
            map_l[e] += 1
        else:
            map_l[e] = 1

    count = 0
    for e in map_f:
        if e in map_l:
            diff = modulous(map_f[e], map_l[e])
            if diff > 0 and map_f[e] > map_l[e]:
                count += diff
        else:
            count += map_f[e]
    
    return count    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')
    fptr.close()