#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:35:56 2020

@author: suryakantkumar
"""


'''
problem : Happy Ladybugs is a board game having the following properties:

° The board is represented by a string b, of length n. The ith character of the string, b[i] , denotes the ith cell of the board.
    ° If b[i] is an underscore (i.e., _), it means the ith cell of the board is empty.
    ° If b[i] is an uppercase English alphabetic letter (ascii[A-Z]), it means the ith cell contains a ladybug of color b[i].
    ° String b will not contain any other characters.
° A ladybug is happy only when its left or right adjacent cell (i.e., b[i+1] or b[i-1]) is occupied by another ladybug having the same color.
° In a single move, you can move a ladybug from its current position to any empty cell.
Given the values of n and b for g games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For each game, print YES on a new line if all the ladybugs can be made happy through some number of moves. Otherwise, print NO.


As an example, b = [YYR_B_BR]. You can move the rightmost B and R to make  b = [YYRRBB__] and all the ladybugs are happy.
'''

import os

def frequency(f):
    for ele in f:
        if f[ele] <= 1:
            return False
    return True

def CheckNext(s):
    flag = True
    for i in range(1, len(s) -1):
        if s[i] == s[i -1] or s[i] == s[i + 1]:
            flag = True
        else:
            flag = False
            return flag
    return True

def happyLadybugs(b):
    freq = {}
    for e in b:
        if e in freq:
            freq[e] += 1
        else:
            freq[e] = 1
    
    if '_' in freq:
        count_ = freq['_']
        del freq['_']
    else:
        count_ = 0
    
    if len(freq) == 0:
        return 'YES'

    for ele in freq:
        if frequency(freq) == False :
            return 'NO'

        else:
            if CheckNext(b) == True:
                return 'YES'
            elif count_ >= 1:
                return 'YES'
            else:
                return 'NO'
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    g = int(input())
    for g_itr in range(g):
        n = int(input())
        b = input()
        result = happyLadybugs(b)
        fptr.write(result + '\n')
    fptr.close()