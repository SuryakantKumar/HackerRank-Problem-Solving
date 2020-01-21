#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:34:53 2020

@author: suryakantkumar
"""

'''
Problem : You will be given a list of 32 bit unsigned integers. 
Flip all the bits (1 --> 0 and 0 --> 1) and print the result as an unsigned integer.
'''


import os 

def flippingBits(n):
    binary = bin(n)                 # Converting number into binary
    b_str = str(binary)
    b_str = b_str[2:]               # removing '0b' from binary number
        
    l = len(b_str)
    li = ['0']*32                   # Created 32 bit array
    
    j = 0
    for i in range(32-l, 32):       # Upadated array with the binay value of number
        li[i] = b_str[j]
        j += 1
    
    for i in range(len(li)):        # Replace 0 with 1 and 1 with 0
        if li[i] == '0':
            li[i] = '1'
        else:
            li[i] = '0'
            
    number = 0
    k = 0
    for i in range(len(li)-1, -1, -1):  # iterating over the array in reverse and counting the number bit by bit
        if li[i] == '1':
            number += 2 ** k
            k += 1
        else:
            k += 1
    
    return number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        result = flippingBits(n)
        fptr.write(str(result) + '\n')
    fptr.close()