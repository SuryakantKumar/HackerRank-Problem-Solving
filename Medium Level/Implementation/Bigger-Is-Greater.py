#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:02:48 2020

@author: suryakantkumar
"""

'''
Problem : Lexicographical order is often known as alphabetical order when dealing with strings. 
A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. 
This new word must meet two criteria:
• It must be greater than the original word
• It must be the smallest word that meets the first condition

For example, given the word w = abcd, the next largest word is abdc.

Complete the function biggerIsGreater below to create and return the new string meeting the criteria. 
If it is not possible, return no answer.
'''

import os

def biggerIsGreater(string):
    for i in range(len(string)-1)[: : -1]:
        if string[i] < string[i+1]:
            for j in range(i+1, len(string))[: : -1]:
                if string[i] < string[j]:
                    li = list(string) 
                    li[i], li[j] = li[j], li[i]
                    return ''.join(li[: i+1] + li[i+1 :][: : -1])
    return 'no answer'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + '\n')
    fptr.close()