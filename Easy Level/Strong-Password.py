#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:30:26 2020

@author: suryakantkumar
"""

'''
Problem : Louise joined a social networking site to stay in touch with her friends. 
The signup page required her to input a name and a password. However, the password must be strong. 
The website considers a password to be strong if it satisfies the following criteria:

• Its length is at least 6.
• It contains at least one digit.
• It contains at least one lowercase English character.
• It contains at least one uppercase English character.
• It contains at least one special character. The special characters are: !@#$%^&*()-+

She typed a random string of length n in the password field but wasn't sure if it was strong. 
Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
'''


import os

def minimumNumber(n, password):
    digit = 0
    lower = 0
    upper = 0
    special = 0

    for e in password:
        if e >= '0' and e <= '9':
            digit += 1
        elif e >= 'a' and e <= 'z':
            lower += 1
        elif e >= 'A' and e <= 'Z':
            upper += 1
        elif e != ' ':
            special += 1

    count = 0
    if digit == 0:
        count += 1
    if lower == 0:
        count += 1
    if upper == 0:
        count += 1
    if special == 0:
        count += 1

    if n >= 6:
        return count
    else:
        req = 6 - n
        if count <= req:
            return req
        else:
            return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + '\n')
    fptr.close()