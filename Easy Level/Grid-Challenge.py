#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:18:20 2020

@author: suryakantkumar
"""

'''
Problem : Given a square grid of characters in the range ascii[a-z], 
rearrange elements of each row alphabetically, ascending. 
Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

For example, given:
a b c
a d e
e f g

The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, 
so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.
'''


def gridChallenge(n, grid):
    for i in range(n):
        string = grid[i]
        li = [x for x in string]
        li = sorted(li)
        new = ''
        for e in li:
            new += e
        grid[i] = new

    for j in range(len(grid[0])):
        for i in range(n - 1):
            if grid[i][j] > grid[i+1][j]:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        result = gridChallenge(n, grid)
        print(result)