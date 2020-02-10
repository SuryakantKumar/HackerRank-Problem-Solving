#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:41:54 2020

@author: suryakantkumar
"""

'''
Problem : An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:
    
    floor(sqrt(L)) <= row <= columns <= ceil(sqrt(L))

For example, the sentence s = 'if man was eant to stay on the ground god would have given us roots', 
after removing spaces is 54 characters long. sqrt(54) is between 7 and 8, so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots

• Ensure that rows * columns >= L
• If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows * columns.
The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message to encode and print.
'''


import math
import os

def encryption(s):
    length = 0
    string = ''
    for e in s:
        if e != ' ':
            length += 1
            string += e        

    row = math.floor(math.sqrt(length))
    column = math.ceil(math.sqrt(length))
    
    if row * column < length:
        row += 1

    li = [['' for j in range(column)] for i in range(row)]
    
    k = 0
    for i in range(row):
        for j in range(column):
            if k < length:
                li[i][j] = string[k]
                k += 1
                
    result = ''
    for i in range(column):
        for j in range(row):
            result += li[j][i]
        result += ' '
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = encryption(s)
    fptr.write(result + '\n')
    fptr.close()