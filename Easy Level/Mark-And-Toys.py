#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:23:11 2020

@author: suryakantkumar
"""

'''
Problem : Mark and Jane are very happy after having their first child. 
Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, 
tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.

Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? 
For example, if prices = [1, 2, 3, 4] and Mark has k = 7 to spend, he can buy items [1, 2, 3] for 6, or [3, 4] for 7 units of currency. 
He would choose the first group of 3 items.
'''


import os

def maximumToys(prices, k):
    prices = sorted(prices)
    count = 0
    for i in range(len(prices)):
        if prices[i] <= k:
            count += 1
            k -= prices[i]

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()