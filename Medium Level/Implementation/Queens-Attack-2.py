#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:59:08 2020

@author: suryakantkumar
"""

'''
Problem : You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.

A queen is standing on an n * n chessboard. The chess board's rows are numbered from 1 to n, going from bottom to top. 
Its columns are numbered from 1 to n, going from left to right. 
Each square is referenced by a tuple, (r, c), describing the row, r, and column, c, where the square is located.

The queen is standing at position (rq, cq). In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals).
'''


#### Solution 01: Oordinary Approach
import os

def queensAttack(n, k, r_q, c_q, obstacles):
    if n == 1:
        return 0

    count = 0
    rq, cq = r_q + 1, c_q
    while rq <= n:                  # Upper Row
        if [rq, cq] in obstacles:
            break
        else:
            rq += 1
            count += 1
    
    rq, cq = r_q - 1, c_q
    while rq > 0:                   # Lower Row
        if [rq, cq] in obstacles:
            break
        else:
            rq -= 1
            count += 1    

    rq, cq = r_q, c_q - 1
    while cq > 0:                   # Left column
        if [rq, cq] in obstacles:
            break
        else:
            cq -= 1
            count += 1
    
    rq, cq = r_q, c_q + 1
    while cq <= n:                 # Right Column
        if [rq, cq] in obstacles:
            break
        else:
            cq += 1
            count += 1

    rq, cq = r_q + 1, c_q - 1
    while rq <= n and cq > 0:       # Upper left diagonally
        if [rq, cq] in obstacles:
            break
        else:
            rq += 1
            cq -= 1
            count += 1

    rq, cq = r_q - 1, c_q + 1
    while rq > 0 and cq <= n:       # lower right diagonally
        if [rq, cq] in obstacles:
            break
        else:
            rq -= 1
            cq += 1
            count += 1

    rq, cq = r_q - 1, c_q - 1
    while rq > 0 and cq > 0:       # lower left diagonally
        if [rq, cq] in obstacles:
            break
        else:
            rq -= 1
            cq -= 1
            count += 1

    rq, cq = r_q + 1, c_q + 1
    while rq <= n and  cq <= n:       # Upper right diagonally
        if [rq, cq] in obstacles:
            break
        else:
            rq += 1
            cq += 1
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')
    fptr.close()
    
    

#### Solution 02 : Optimal Approach
import os

def queensAttack(n, k, r_q, c_q, obstacles):
    up = n - r_q        # Up
    down = r_q - 1      # Down
    right = n - c_q     # Right
    left = c_q - 1      # Left
    
    ru = min(up, right)     # RightUp
    rd = min(right, down)   # RightDown
    lu = min(left, up)      # leftUp
    ld = min(left, down)    # LeftDown
    
    for o in obstacles:
        if o[1] == c_q:
            if o[0] < r_q:
                down = min(down, r_q - 1 - o[0])
            else:
                up = min(up, o[0] - r_q - 1)
                
        elif o[0] == r_q:
            if o[1] < c_q: 
                left = min(left, c_q - 1 - o[1])
            else:
                right = min(right, o[1] - c_q - 1)
                
        elif abs(o[0] - r_q) == abs(o[1]-c_q):
            if o[1] > c_q:
                if o[0] > r_q:
                    ru = min(ru, o[1] - c_q - 1)
                else:
                    rd = min(rd, o[1] - c_q - 1)
                
            else:
                if o[0] > r_q:
                    lu = min(lu, c_q - 1 - o[1])
                else:
                    ld = min(ld, c_q - 1 - o[1])
                
    return up + down + right + left + ru + rd + lu + ld

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    fptr.write(str(result) + '\n')
    fptr.close()