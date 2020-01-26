#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:46:09 2020

@author: suryakantkumar
"""

'''
Problem : Two players are playing a game on a 15 * 15 chessboard. 
The rules of the game are as follows:
• The game starts with a single coin located at some x, y coordinates. 
  The coordinates of the upper left cell are (1, 1), and of the lower right cell are (15, 15).

• In each move, a player must move the coin from cell (x, y) to one of the following locations:
  (x - 2, y + 1)
  (x - 2, y - 1)
  (x + 1, y - 2)
  (x - 1, y - 2)
    
Note: The coin must remain inside the confines of the board.

• Beginning with player 1, the players alternate turns. The first player who is unable to make a move loses the game.

Given the initial coordinates of the players' coins, assuming optimal play, determine which player will win the game.
'''


import os

def chessboardGame(x, y):
    x = x % 4
    y = y % 4
    if x == 0 or x == 3 or y == 0 or y == 3:
        return 'First'
    else:
        return 'Second'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        result = chessboardGame(x, y)
        fptr.write(result + '\n')
    fptr.close()