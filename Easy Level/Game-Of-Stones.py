#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:02:43 2020

@author: suryakantkumar
"""

'''
Problem : Two players called P1 and P2 are playing a game with a starting number of stones. 
Player 1 always plays first, and the two players move in alternating turns. 
The game's rules are as follows:
• In a single move, a player can remove either 2, 3, or 5 stones from the game board.
• If a player is unable to make a move, that player loses the game.

Given the starting number of stones, find and print the name of the winner. 
P1 is named First and P2 is named Second. Each player plays optimally, meaning they will not make a move that causes them to lose the game if a winning move exists.

For example, if n = 4, P1 can make the following moves:
• P1 removes 2 stones leaving 2. P2 will then remove 2 stones and win.
• P1 removes 3 stones leaving 1. P2 cannot move and loses.

P1 would make the second play and win the game.
'''


import os

def gameOfStones(n):
    maxx = 100
    position = [0] * (maxx + 1)

    position[0] = 0
    position[1] = 0
    position[2] = 1
    position[3] = 1
    position[4] = 1
    position[5] = 1

    for i in range(6, maxx + 1):
        if position[i - 2] !=  1 or position[i - 3] != 1 or position[i - 5] != 1:
            position[i] = 1
        else:
            position[i] = 0

    if position[n] == 1:
        return 'First'
    else:
        return 'Second'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = gameOfStones(n)
        fptr.write(result + '\n')
    fptr.close()