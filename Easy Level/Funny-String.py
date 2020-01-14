#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:30:24 2020

@author: suryakantkumar
"""

'''
Problem : In this challenge, you will determine whether a string is funny or not. 
To determine whether a string is funny, create a copy of the string in reverse e.g. abc --> bca. 
Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. 
If the list of absolute differences is the same for both strings, they are funny.

Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

For example, given the string s = lmnop, the ordinal values of the charcters are [108, 109, 110, 111, 112]. 
S-reverse = ponml and the ordinals are [112, 111, 110, 109, 108]. 
The absolute differences of the adjacent elements for both strings are [1, 1, 1, 1], so the answer is Funny.
'''


import os

def absolute(a, b):
    if a - b < 0:
        return b - a
    return a - b

def funnyString(s):
    li_orig = []
    for i in range(len(s) -1):
        diff = absolute(ord(s[i+1]), ord(s[i]))
        li_orig.append(diff)

    rev_s = s[::-1]

    li_rev = []
    for i in range(len(rev_s) -1):
        diff = absolute(ord(rev_s[i+1]), ord(rev_s[i]))
        li_rev.append(diff)

    if li_orig == li_rev:
        return 'Funny'
    else:
        return 'Not Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
    fptr.close()