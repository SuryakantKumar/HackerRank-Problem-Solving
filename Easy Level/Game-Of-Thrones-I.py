#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:44:42 2020

@author: suryakantkumar
"""

'''
Problem : Dothraki are planning an attack to usurp King Robert's throne. 
King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.

But, to lock the door he needs a key that is an anagram of a palindrome. 
He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome.

For example, given the string s = [aabbccdd], one way it can be arranged into a palindrome is abcddcba.
'''


import os

def gameOfThrones(s):
    if len(s) == 1:
        return 'YES'

    if len(s) == 2:
        if s[0] == s[1]:
            return 'YES'
        else:
            return 'NO'

    freq = {}
    for e in s:
        if e in freq:
            freq[e] += 1
        else:
            freq[e] = 1

    freq_val = [freq[e] for e in freq]

    even_val = 0
    odd_val = 0
    ones = 0
    for e in freq_val:
        if e % 2 == 0:
            even_val += 1
        elif  e == 1:
            ones += 1
        else:
            odd_val += 1

    if ones == 0:
        if even_val > 0 and (odd_val == 0 or odd_val == 1):
            return 'YES'
        elif even_val == 0 and odd_val == 1:
            return 'YES'
        else:
            return 'NO'
    elif ones == 1:
        if even_val > 0 and odd_val == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = gameOfThrones(s)
    fptr.write(result + '\n')
    fptr.close()