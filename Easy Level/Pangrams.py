#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:18:42 2020

@author: suryakantkumar
"""

'''
Problem : Roy wanted to increase his typing speed for programming contests. 
His friend suggested that he type the sentence "The quick brown fox jumps over the lazy dog" repeatedly. 
This sentence is known as a pangram because it contains every letter of the alphabet.

After typing the sentence several times, Roy became bored with it so he started to look for other pangrams.

Given a sentence, determine whether it is a pangram. Ignore case.
'''


import os

def pangrams(s):
    s = s.lower()

    f1 = {}
    for e in s:
        if e in f1:
            f1[e] = 0
        else:
            f1[e] = 0
    
    string = 'abcdefghijklmnopqrstuvwxyz'
    
    f2 = {}
    for e in string:
        if e in f2:
            f2[e] = 0
        else:
            f2[e] = 0

    if f1 == f2:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = pangrams(s)
    fptr.write(result + '\n')
    fptr.close()