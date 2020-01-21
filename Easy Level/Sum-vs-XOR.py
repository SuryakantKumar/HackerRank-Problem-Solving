#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 09:58:00 2020

@author: suryakantkumar
"""

'''
Problem : Given an integer n, find each x such that:
• 0 <= x <= n
• n + x = n ^ x
    
where ^ denotes the bitwise XOR operator. Print the number of x's satisfying the criteria.
'''


import os

def sumXor(n):
    if n == 0:
        return 1
        
    binary = bin(n)
    b_str = str(binary)
    b_str = b_str[2:]
    print(b_str)

    count_0 = 0
    for e in b_str:
        if e == '0':
            count_0 += 1
    
    return 2 ** count_0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = sumXor(n)
    fptr.write(str(result) + '\n')
    fptr.close()