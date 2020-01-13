#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:25:50 2020

@author: suryakantkumar
"""

'''
Problem : Bob has a strange counter. At the first second, it displays the number 3. 
Each second, the number displayed by the counter decrements by 1 until it reaches 1.

The counter counts down in cycles. In next second, the timer resets to "2 * the initial value of prior cycle" and continues counting down. 

Find and print the value displayed by the counter at time t.

Sample Input : 
4

Sample Output : 
6

Explanation : 
Time t = 4 marks the beginning of the second cycle. 
It is double the number displayed at the beginning of the first cycle: 2 * 3 = 6. 
'''


import os
import math

def strangeCounter(t):
    x = math.floor(math.log2(((t+2) * 4) / 3))
    value = int(2**x - 2**(x-2))
    time = value - 2

    print(value, t, time)
    return value - (t - time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    result = strangeCounter(t)
    fptr.write(str(result) + '\n')
    fptr.close()