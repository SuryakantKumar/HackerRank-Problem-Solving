#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 00:27:34 2020

@author: suryakantkumar
"""

'''
Problem : Given the time in numerals we may convert it into words, as shown below:
    05:00 --> 5 o' clock
    05:01 --> one minute past five
    05:10 --> ten minutes past five
    05:15 --> quarter past five
    05:30 --> half past five
    05:40 --> twenty minutes to six
    05:45 --> quarter to six
    05:59 --> one minute to six

At minutes = 0, use o' clock. For 1 <= minutes <= 30, use past, and for minutes > 30 use to. 
Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.
'''


import os

def timeInWords(h, m):
    words = {1 : "one", 2: "two", 3: "three", 4: "four", 5: "five",
             6 : "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
             11 : "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "quarter",
             16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 
             20: "twenty", 21: "twenty one", 22: "twenty two", 23: "twenty three",
             24: "twenty four", 25: "twenty five", 26: "twenty six", 27: "twenty seven",
             28: "twenty eight", 29: "twenty nine", 30: 'half'
            }

    if m == 0:
        return words[h] + " o' clock"
    
    elif m > 0 and m <= 30:
        if m == 1:
            return words[m] + ' minute past ' + words[h]
        elif m == 15 or m == 30:
            return words[m] + ' past ' + words[h]
        else:
            return words[m] + ' minutes past ' + words[h]
    else:
        if m == 1:
            return words[60 - m] + ' minute to ' + words[h + 1]
        elif m == 45:
            return words[60 - m] + ' to ' + words[h + 1]
        else:
            return words[60 - m] + ' minutes to ' + words[h + 1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = int(input())
    m = int(input())
    result = timeInWords(h, m)
    fptr.write(result + '\n')
    fptr.close()