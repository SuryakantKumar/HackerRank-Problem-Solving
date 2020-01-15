#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:28:58 2020

@author: suryakantkumar
"""

'''
Problem : Given two strings, determine if they share a common substring. 
A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring a. 
The words "be" and "cat" do not share a substring.
'''


import os

def twoStrings(s1, s2):
    if len(s1) == 1 and len(s2) == 1 :
        if s1 == s2:
            return 'Yes'
        else:
            return 'NO'

    f1 = {}
    for e in s1:
        if e in f1:
            f1[e] += 1
        else:
            f1[e] = 1
    
    f2 = {}
    for e in s2:
        if e in f2:
            f2[e] += 1
        else:
            f2[e] = 1

    flag = False
    for e in f1:
        if e in f2:
            flag = True
            return 'YES'

    if flag == False:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        fptr.write(result + '\n')
    fptr.close()