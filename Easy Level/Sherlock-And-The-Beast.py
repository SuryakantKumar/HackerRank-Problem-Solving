#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:36:12 2020

@author: suryakantkumar
"""

'''
Problem : Sherlock Holmes suspects his archenemy Professor Moriarty is once again plotting something diabolical. 
Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, The Beast.

Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast with a virus. 
He also gives him a clue: an integer. Sherlock determines the key to removing the virus is to find the largest Decent Number having that number of digits.

A Decent Number has the following properties:
1. Its digits can only be 3's and/or 5's.
2. The number of 3's it contains is divisible by 5.
3. The number of 5's it contains is divisible by 3.
4. It is the largest such number for its length.

Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. 
Your task is to help Sherlock find the key before The Beast is destroyed!

For example, the numbers 555333333 and 555555 are both decent numbers because there are 3 5's and 5 3's in the first, and 6 5's in the second. 
They are the largest values for those length numbers that have proper divisibility of digit occurrences.
'''


def decentNumber(n):
    if n < 3:
        print(-1)
        return
    
    if n % 3 == 0:
        print(int('5'*n))
        return

    elif n % 3 == 2:
        print(int('5'*(n-5) + '3'*5))
        return
    
    elif n % 3 == 1:
        if n < 10:
            print(-1)
            return
        else:
            print(int('5'*(n-10) + '3'*10))
            return

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        decentNumber(n)