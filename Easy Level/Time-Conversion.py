#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 6 12:24:21 2020

@author: suryakantkumar
"""

'''
Problem : Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
'''


import os

def timeConversion(s):
    military_time = ''

    if s[-2] == 'A' or s[-2] == 'a':
        if int(s[0:2]) == 12:
            military_time = '00' + s[2:-2]
            
        else:
            military_time = s[0:-2]
            
    else:
        if int(s[0:2]) != 12:
            military_time = str(int(s[0:2]) + 12) + s[2:-2]
            
        else:
            military_time = '12' + s[2:-2]
            
    return military_time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
