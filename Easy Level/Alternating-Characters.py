#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:05:41 2020

@author: suryakantkumar
"""

'''
Problem : You are given a string containing characters A and B only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string s = AABAAB, remove an A at positions 0 and 3 to make s = ABAB in 2 deletions.
'''


import os

def alternatingCharacters(s):
    new_str = ''
    
    i = 0
    while i < len(s) -1:
        if s[i] == s[i + 1]:
            i += 1
        else:
            new_str += s[i]
            i += 1
    new_str += s[len(s) - 1]

    return len(s) - len(new_str)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()