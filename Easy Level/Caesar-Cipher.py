#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:14:31 2020

@author: suryakantkumar
"""

'''
Problem : Julius Caesar protected his confidential information by encrypting it using a cipher. 
Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, 
just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
'''


import os

def caesarCipher(s, k):
    new_str = ''
    if k > 26 :
        k = k % 26
        
    for e in s:
        if e >= 'a' and e <= 'z':
            val = ord(e) + k
            if val > ord('z'):
                val = (val - ord('a') + 1) % 26
                char = chr(ord('a') + val -1)
                new_str += char
            else:
                new_str += chr(val)

        elif e >= 'A' and e <= 'Z':
            val = ord(e) + k
            if val > ord('Z'):
                val = (val - ord('A') + 1) % 26
                char = chr(ord('A') + val -1)
                new_str += char
            else:
                new_str += chr(val)
        else:
            new_str += e

    return new_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    k = int(input())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()