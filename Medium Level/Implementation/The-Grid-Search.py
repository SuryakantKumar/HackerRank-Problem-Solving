#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 00:32:44 2020

@author: suryakantkumar
"""

'''
Problem : Given a 2D array of digits or grid, try to find the occurrence of a given 2D pattern of digits. 
For example, consider the following grid:

1234567890  
0987654321  
1111111111  
1111111111  
2222222222  

Assume we need to look for the following 2D pattern array:

876543  
111111  
111111

The 2D pattern begins at the second row and the third column of the grid. 
The pattern is said to be present in the grid.
'''


import os

def gridSearch(G, P):
    Gi, Gj = len(G), len(G[0])
    Pi, Pj = len(P), len(P[0])
    for i in range(Gi - Pi + 1):
        for j in range(Gj - Pj + 1):
            flag = True
            for ii in range(Pi):
                for jj in range(Pj):
                    if flag:
                        flag = (G[i + ii][j + jj] == P[ii][jj])
                    else:
                        break
                if not flag:
                    break
            if flag:
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])
        C = int(RC[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        rc = input().split()
        r = int(rc[0])
        c = int(rc[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        result = gridSearch(G, P)
        fptr.write(result + '\n')
    fptr.close()
