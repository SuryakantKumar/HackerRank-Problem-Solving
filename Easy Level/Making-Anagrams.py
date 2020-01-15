#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:36:47 2020

@author: suryakantkumar
"""

'''
Problem : We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. 
In other words, both strings must contain the same exact letters in the same exact frequency. 
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice is taking a cryptography class and finding anagrams to be very useful. 
She decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. 
Can you help her find this number?

Given two strings, s1 and s2, that may not be of the same length, determine the minimum number of character deletions required to make s1 and s2 anagrams. 
Any characters can be deleted from either of the strings.

For example, s1 = abc and s2 = amnop. The only characters that match are the a's so we have to remove bc from s1 and mnop from s2 for a total of 6 deletions.
'''


import os

def modulous(a, b):
    if a < b:
        return b - a
    elif a == b:
        return 0
    else:
        return a - b

def makingAnagrams(s1, s2):

    map_f = {}
    for e in s1:
        if e in map_f:
            map_f[e] += 1
        else:
            map_f[e] = 1
    
    map_l = {}
    for e in s2:
        if e in map_l:
            map_l[e] += 1
        else:
            map_l[e] = 1

    common = 0
    for e in map_f:
        if e in map_l:
            diff = modulous(map_f[e], map_l[e])
            if diff == 0:
                common += map_f[e]
            elif diff > 0 and map_f[e] > map_l[e]:
                common += (map_f[e] - diff)
            elif diff > 0 and map_f[e] < map_l[e]:
                common += (map_l[e] - diff)
                
    return len(s1) + len(s2) - 2*common
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()