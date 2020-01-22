#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:16:53 2020

@author: suryakantkumar
"""

'''
Problem : The factorial of the integer n, written n!, is defined as:
    n! = n * (n - 1) * (n - 2) * .....* 3 * 2 * 1

Calculate and print the factorial of a given integer.
'''


def extraLongFactorials(n):
    if n == 0 or n == 1:
        return 1
    
    return n * extraLongFactorials(n-1)

if __name__ == '__main__':
    n = int(input())
    x = extraLongFactorials(n)
    print(x)