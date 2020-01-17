#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:35:15 2020

@author: suryakantkumar
"""

'''
Problem : Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. 
Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. 
Each contest is described by two integers, L[i] and T[i]:

• L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i]; 
if she loses it, her luck balance will increase by L[i].
• T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.

If Lena loses no more than k important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? 
This value may be negative.

For example, k = 2 and:

Contest	L[i]	 T[i]
1		5	 1
2		1	 1
3		4	 0

If Lena loses all of the contests, her will be 5 + 4 + 1 = 10. Since she is allowed to lose 2 important contests, 
and there are only 2 important contests. She can lose all three contests to maximize her luck at 10. 
If k = 1, she has to win at least 1 of the 2 important contests. 
She would choose to win the lowest value important contest worth 1. Her final luck will be 5 + 4 - 1 = 8.
'''


import os

def luckBalance(k, contests):
    imp_luck = []
    total_point = 0
    for i in range(len(contests)):
        if contests[i][1] == 1:
            imp_luck.append(contests[i][0])
            total_point += contests[i][0]
        elif contests[i][1] == 0:
            total_point += contests[i][0]        
    
    imp_luck = sorted(imp_luck)

    for i in range(len(imp_luck) - k):
        total_point -= 2*imp_luck[i]

    return total_point

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()