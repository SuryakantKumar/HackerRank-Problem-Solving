#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:05:06 2020

@author: suryakantkumar
"""

'''
problem : Given an array of stick lengths, use 3 of them to construct a non-degenerate triange with the maximum possible perimeter. 
Print the lengths of its sides as 3 space-separated integers in non-decreasing order.

If there are several valid triangles having the maximum perimeter:

1. Choose the one with the longest maximum side.
2. If more than one has that maximum, choose from them the one with the longest minimum side.
3. If more than one has that maximum as well, print any one them.
If no non-degenerate triangle exists, print -1.

For example, assume there are stick lengths sticks = [1, 2, 3, 4, 5, 10]. 
The triplet (1, ,2 ,3) will not form a triangle. Neither will (4, 5, 10) or (2, 3, 5), 
so the problem is reduced to (2, ,3, 4) and (3, 4, 5). The longer perimeter is 3 + 4 + 5 = 12.
'''


import os

def maximumPerimeterTriangle(sticks):
    sticks = sorted(sticks)
    result = []

    for i in range(len(sticks)- 2):
        for j in range(i +1, len(sticks) -1):
            for k in range(j +1, len(sticks)):
                l = [sticks[i], sticks[j], sticks[k]] 
                l = sorted(l)
                if l[0] + l[1] > l[2] and l not in result:
                    result.append(l)

    if len(result) == 0:
        return [-1]
    elif len(result) == 1:
        return result[0]
    else:
        max_par = [result[0]]
        summ = sum(result[0])
        for e in result[1:]:
            if sum(e) > summ:
                max_par = []
                max_par.append(e)
                summ = sum(e)
            elif sum(e) == summ:
                max_par.append(e)
        
        if len(max_par) == 1:
            return max_par[0]
        else:
            max_longer = max_par[0][2]
            max_long_li = [max_par[0]]
            for e in max_par[1:]:
                if e[2] == max_longer:
                    max_long_li.append(e)
                elif e[2] > max_longer:
                    max_long_li = []
                    max_long_li.append(e)
                    max_longer = e[2]

            if len(max_long_li) == 1:
                return max_long_li[0]
            else:
                max_shorter = max_long_li[0][0]
                max_short_li = [max_long_li[0]]
                for e in max_long_li[1:]:
                    if e[0] == max_shorter:
                        max_short_li.append(e)
                    elif e[2] > max_shorter:
                        max_short_li = []
                        max_short_li.append(e)
                        max_shorter = e[0]

                return max_short_li[0]
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()