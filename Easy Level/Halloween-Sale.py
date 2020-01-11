#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:42:48 2020

@author: suryakantkumar
"""

'''
Problem : You wish to buy video games from the famous online video game store Mist.

Usually, all games are sold at the same price, p dollars.
However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. 
Specifically, the first game you buy during the sale will be sold at p dollars,
but every subsequent game you buy will be sold at exactly d dollars less than the cost of the previous one you bought. 
This will continue until the cost becomes less than or equal to m dollars, after which every game you buy will cost m dollars each.

For example, if p = 20, d = 3 and m = 6, then the following are the costs of the first 11 games you buy, in order:
    20 17 14 11 8 6 6 6 6 6 6
                            
You have s dollars in your Mist wallet. How many games can you buy during the Halloween Sale?
'''


import os

def howManyGames(p, d, m, s):
    games = 0
    while s >= m:
        if games == 0:
            if s >= p:
                games += 1
                s -= p
                p -= d
            else:
                return 0
            
        elif games > 0 and p >= m:
            if s >= p:
                s -= p
                p = p - d
                games += 1
            else:
                return games
            
        else:
            games += 1
            s -= m
            
    return games

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    pdms = input().split()
    p = int(pdms[0])
    d = int(pdms[1])
    m = int(pdms[2])
    s = int(pdms[3])
    answer = howManyGames(p, d, m, s)
    fptr.write(str(answer) + '\n')
    fptr.close()