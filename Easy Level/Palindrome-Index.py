#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 23:43:01 2020

@author: suryakantkumar
"""

'''
Problem : Given a string of lowercase letters in the range ascii[a-z], 
determine a character that can be removed to make the string a palindrome. 
There may be more than one solution, but any will do. For example, if your string is "bcbc", 
you can either remove 'b' at index 0 or 'c' at index 1. If the word is already a palindrome or there is no solution, return -1. 
Otherwise, return the index of a character to remove.
'''


import os

def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
        
def palindromeIndex(s, si, ei):
    if len(s) == 1:
        return -1
    elif len(s) == 2 and s[0] != s[1]:
        return 1
    
    while si <= ei:
        if s[si] == s[ei]:
            si += 1
            ei -= 1
        else:
            if isPalindrome(s[si+1:ei+1]) == True:
                return si
            else:
                return ei
    return -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        si = 0
        ei = len(s) - 1
        result = palindromeIndex(s, si, ei)
        fptr.write(str(result) + '\n')
    fptr.close()