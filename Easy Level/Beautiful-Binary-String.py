#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:46:50 2020

@author: suryakantkumar
"""

'''
Problem : Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring "010".

In one step, Alice can change a 0 to a 1 or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

For example, if Alice's string is b = 010 she can change any one element and have a beautiful string.
'''


import os

def beautifulBinaryString(b):
    if len(b) < 3:
        return 0
    
    li = [x for x in b]

    count = 0
    for i in range(1, len(li) -1):
        if li[i-1] == '0' and li[i] == '1' and li[i+1] == '0':
            li[i+1] = '1'
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    b = input()
    result = beautifulBinaryString(b)
    fptr.write(str(result) + '\n')
    fptr.close()