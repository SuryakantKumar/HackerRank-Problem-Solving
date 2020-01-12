#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 6 10:56:19 2020

@author: suryakantkumar
"""

'''
Problem : Consider a staircase of size n = 4:
    
   #
  ##
 ###
####
 
Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.
'''


def staircase(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = '')
            
        for k in range(i):
            print('#', end = '')
                  
        print()
        
n = int(input())
staircase(n)
