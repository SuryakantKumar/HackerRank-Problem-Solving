#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 6 11:10:07 2020

@author: suryakantkumar
"""

'''
Problem : You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.

For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4, 4, 1, 3 she will be able to blow out 2 candles successfully, since the tallest candles are of height 4 and there are 2 such candles.
'''


import os

def birthdayCakeCandles(ar_count, ar):
    count = 0
    max_height = 0
    
    for i in range(ar_count):
        if ar[i] > max_height:
            max_height = ar[i]
            count = 1
            
        else:
            if ar[i] == max_height:
                count += 1
                
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar_count, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
    
