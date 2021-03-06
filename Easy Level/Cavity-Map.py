#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:49:25 2020

@author: suryakantkumar
"""

'''
Problem : You are given a square map as a matrix of integer strings. 
Each cell of the map has a value denoting its depth. 
We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. 
Two cells are adjacent if they have a common side, or edge.

Find all the cavities on the map and replace their depths with the uppercase character X.

For example, given a matrix:
989
191
111

You should return:
989
1X1
111

The center cell was deeper than those on its edges: [8,1,1,1]. The deep cells in the top two corners don't share an edge with the center cell.
'''


import os

def cavityMap(n, grid):
    if n < 3:
        return grid
    
    for i in range(1, n - 1):
        new_str = ''
        new_str += grid[i][0]
        for j in range(1, n - 1):
            if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j+1]:
                new_str += 'X'
            else:
                new_str += grid[i][j]
                
        new_str += grid[i][n-1]
        grid[i] = new_str
    
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(n, grid)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()