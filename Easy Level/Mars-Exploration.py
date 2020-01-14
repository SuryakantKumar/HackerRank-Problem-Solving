#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:35:28 2020

@author: suryakantkumar
"""

'''
Problem : Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help.

Letters in some of the SOS messages are altered by cosmic radiation during transmission. 
Given the signal received by Earth as a string,s , determine how many letters of Sami's SOS have been changed by radiation.

For example, Earth receives SOSTOT. Sami's original message was SOSSOS. Two of the message characters were changed in transit.
'''


import os

def marsExploration(s):
    count = 0
    for i in range(0, len(s), 3):
        string = s[i:i+3]
        if string[0] != 'S':
            count += 1
            
        if string[1] != 'O':
            count += 1
            
        if string[2] != 'S':
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = marsExploration(s)
    fptr.write(str(result) + '\n')
    fptr.close()