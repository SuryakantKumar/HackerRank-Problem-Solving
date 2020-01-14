#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:27:59 2020

@author: suryakantkumar
"""

'''
Problem : A numeric string, s, is beautiful if it can be split into a sequence of two or more positive integers, a[1], a[2]....a[n], 
satisfying the following conditions:

1. a[i] - a[i-1] = 1, for any 1 < i <= n (i.e., each element in the sequence is 1 more than the previous element).
2. No a[i] contains a leading zero. For example, we can split s = 10203 into the sequence {1, 02, 03}, but it is not beautiful because 02 and 03 have leading zeroes.
3. The contents of the sequence cannot be rearranged. For example, we can split s = 312 into the sequence {3, 1, 2}, but it is not beautiful because it breaks our first constraint (i.e., 1 - 3 ≠ 1 ).

You must perform q queries where each query consists of some integer string s. 
For each query, print whether or not the string is beautiful on a new line. 
If it's beautiful, print YES x, where x is the first number of the increasing sequence. 
If there are multiple such values of x, choose the smallest. Otherwise, print NO.
'''


def separateNumbers(s):
    if len(s) <= 1 or int(s[0]) == 0:
        print('NO') 
    
    elif len(s) == 2:
        if int(s[1]) - int(s[0]) == 1:
            print('YES')
        else:
            print('NO')
            
    else:
        flag = False
        
        for i in range(0, len(s)-1):
            start = s[0:i+1]
            
            ns = s[0:i+1]
            first = s[0:i+1]
            while len(ns) < len(s):
                next_ = str(int(first) + 1)
                first = next_
                ns += next_

            if s == ns:
                flag = True
                print('YES', start)

        if flag == False:
            print('NO')
    
if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)