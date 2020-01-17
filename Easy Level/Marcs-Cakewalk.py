#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:42:03 2020

@author: suryakantkumar
"""

'''
Problem : Marc loves cupcakes, but he also likes to stay fit. 
Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. 
If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk at least (2^j)*c miles to maintain his weight.

For example, if he eats 3 cupcakes with calorie counts in the following order: [5, 10, 17], 
the miles he will need to walk are (2^0)*5 + (2^1)*10 + (2^2)*7 = 5 + 20 + 28 = 53. 
This is not the minimum, though, so we need to test other orders of consumption. 
In this case, our minimum miles is calculated as (2^0)*10 + (2^1)*7 + (2^2)*5 = 10 + 14 + 20 = 44.

Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. 
Note that he can eat the cupcakes in any order.
'''


import os

def marcsCakewalk(calorie):
    miles = 0
    calorie = sorted(calorie)
    calorie = calorie[::-1]

    for i in range(len(calorie)):
        miles += (2 ** i)*(calorie[i])
    
    return miles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)
    fptr.write(str(result) + '\n')
    fptr.close()