#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 15:41:04 2020

@author: suryakantkumar
"""

'''
Problem : Little Bobby loves chocolate. He frequently goes to his favorite 5 & 10 store, Penny Auntie, to buy them.
They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.

For example, Bobby has n = 15 to spend on bars of chocolate that cost c = 3 each.
He can turn in m = 2 wrappers to receive another bar. Initially, he buys 5 bars and has 5 wrappers after eating them. 
He turns in 4 of them, leaving him with 1, for 2 more bars. After eating those two, he has 3 wrappers, turns in 2 leaving him with 1 wrapper 
and his new bar. Once he eats that one, he has 2 wrappers and turns them in for another bar. 
After eating that one, he only has 1 wrapper, and his feast ends. Overall, he has eaten 5 + 2 + 1 + 1 = 9 bars.
'''


import os

def chocolateFeast(n, c, m):
    bar = n // c
    wrapper = bar
    new = wrapper // m
    bar += new
    wrapper -= new * m
    
    while new + wrapper >= m:
        wrapper = new + wrapper
        new = 0
        new  = (wrapper + new) // m
        bar += new
        wrapper -= new * m
        
    return bar

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        ncm = input().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])
        result = chocolateFeast(n, c, m)
        fptr.write(str(result) + '\n')
    fptr.close()