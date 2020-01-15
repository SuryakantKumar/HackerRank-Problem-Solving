#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:53:47 2020

@author: suryakantkumar
"""

'''
Problem : Amanda has a string of lowercase letters that she wants to copy to a new string. 
She can perform the following operations with the given costs. She can perform them any number of times to construct a new string p:

• Append a character to the end of string p at a cost of 1 dollar.
• Choose any substring of p and append it to the end of p at no charge.

Given n strings s[i], find and print the minimum cost of copying each s[i] to p[i] on a new line.

For example, given a string s = abcabc, it can be copied for 3 dollars. 
Start by copying a, b and c individually at a cost of 1 dollar per character. 
String p = abc at this time. Copy p[0 : 2] to the end of p at no cost to complete the copy.
'''


import os

def stringConstruction(s):
    freq = {}
    for e in s:
        if e in freq:
            freq[e] += 1 
        else:
            freq[e] = 1
    
    return len(freq)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = stringConstruction(s)
        fptr.write(str(result) + '\n')
    fptr.close()