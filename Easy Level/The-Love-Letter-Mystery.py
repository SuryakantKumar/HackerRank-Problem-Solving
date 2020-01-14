#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 23:12:33 2020

@author: suryakantkumar
"""

'''
Problem : James found a love letter that his friend Harry has written to his girlfriend. 
James is a prankster, so he decides to meddle with the letter. 
He changes all the words in the letter into palindromes.

To do this, he follows two rules:

1. He can only reduce the value of a letter by 1, i.e. he can change d to c, but he cannot change c to d or d to b.
2. The letter a may not be reduced any further.
Each reduction in the value of any letter is counted as a single operation. 
Find the minimum number of operations required to convert a given string into a palindrome.

For example, given the string s = cde, the following two operations are performed: cde → cdd → cdc.
'''


import os

def theLoveLetterMystery(s):
    li = [x for x in s]

    count = 0
    for i in range(len(s)//2):
        while li[i] != li[len(s) - i - 1]:
            if li[i] > li[len(s) - i - 1]:
                li[i] = chr(ord(li[i]) - 1)
                count += 1
                
            elif li[i] < li[len(s) - i - 1]:
                li[len(s) - i - 1] = chr(ord(li[len(s) - i - 1]) - 1)
                count += 1
                
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        fptr.write(str(result) + '\n')
    fptr.close()