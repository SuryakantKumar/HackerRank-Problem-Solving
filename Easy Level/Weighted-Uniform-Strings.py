#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:20:52 2020

@author: suryakantkumar
"""


'''
Problem : A weighted string is a string of lowercase English letters where each letter has a weight. 
Character weights are 1 to 26 from 1 to z.

We define the following terms:

• The weight of a string is the sum of the weights of all the string's characters. 

• A uniform string consists of a single character repeated zero or more times. 
For example, ccc and a are uniform strings, but bcb and cd are not.

Given a string, s, let U be the set of weights for all possible uniform contiguous substrings of string s. 
You have to answer n queries, where each query i consists of a single integer, x[i]. 
For each query, print Yes on a new line if x[i] ¢ U; otherwise, print No instead.
'''

import os

def CountSame(s, si):           # To count the repeated character every time and return count of repeated characters and next index to work
    j = si
    count = 1
    while j < len(s) - 1 and s[j] == s[j+1]:
        j += 1
        count += 1
    
    return j+1, count

def weightedUniformStrings(s, queries):
    freq = {}
    i = 0
    while i < len(s):
        if s[i] in freq:
            x2 = CountSame(s, i)
            if x2[1] > freq[s[i]]:
                freq[s[i]] = x2[1]
            i = x2[0]
        else:
            x = CountSame(s, i)
            freq[s[i]] = x[1]
            i = x[0]

    values = set()
    for ele in freq:
        ele_val = (ord(ele) - ord('a') + 1 )
        for i in range(1, freq[ele] + 1):
            local_ev = (ord(ele) - ord('a') + 1 )
            values.add(ele_val)
            ele_val += local_ev

    li = []
    for ele in queries:
        if ele in values:
            li.append('Yes')
        else:
            li.append('No')
    
    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)
    result = weightedUniformStrings(s, queries)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
