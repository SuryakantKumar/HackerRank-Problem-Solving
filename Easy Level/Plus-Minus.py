#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 6 10:50:34 2020

@author: suryakantkumar
"""

'''
Problem : Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to (10)**(-4) are acceptable.

For example, given the array arr = [1, 1, 0, -1, -1] there are 5 elements, two positive, two negative and one zero. Their ratios would be 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. It should be printed as

0.400000
0.400000
0.200000
'''


def plusMinus(arr):
    positive = 0
    negative = 0
    zeroes = 0
    
    for i in arr:
        if i > 0:
            positive += 1
            
        elif i < 0:
            negative += 1
            
        else:
            zeroes += 1
            
    positive_f = positive / n
    negative_f = negative / n
    zeroes_f = zeroes / n
    
    return positive_f, negative_f, zeroes_f

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    x, y, z = plusMinus(arr)
    print("%.6f" % x)
    print("%.6f" % y)
    print("%.6f" % z)