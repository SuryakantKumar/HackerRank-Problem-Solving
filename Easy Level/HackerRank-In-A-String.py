#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:57:23 2020

@author: suryakantkumar
"""

'''
Problem : We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. 
For example, if string s = haacckkerrnnkk it does contain hackerrank, but s = haacckkerankk does not. 
In the second case, the second r is missing. If we reorder the first string as hccaakkerrannkk, it no longer contains the subsequence due to ordering.

More formally, let p[0], p[1]...p[9] be the respective indices of h, a, c, k, e, r, r, a, n, k in string s. 
If p[0] < p[1] < p[2] ... < p[9] is true, then s contains hackerrank.

For each query, print YES on a new line if the string contains hackerrank, otherwise, print NO.

Sample Input :
2
hereiamstackerrank
hackerworld

Sample Output :
YES
NO

Explanation :
We perform the following q = 2 queries:

1. s = hereiamstackerrank
The characters of hackerrank are bolded in the string above. 
Because the string contains all the characters in hackerrank in the same exact order as they appear in hackerrank, we print YES on a new line.

2. s = hackerworld does not contain the last three characters of hackerrank, so we print NO on a new line.
'''


import os

def hackerrankInString(s):
    string = 'hackerrank'

    i = 0
    j = 0
    while i < len(s) and j < len(string):
        if string[j] == s[i]:
            i += 1
            j += 1
        elif string[j] != s[i]:
            i += 1
    
    if j == len(string):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        fptr.write(result + '\n')
    fptr.close()