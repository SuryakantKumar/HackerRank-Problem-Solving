#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:40:07 2020

@author: suryakantkumar
"""

'''
Problem : Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. 
The game uses Dense Ranking, so its leaderboard works like this:
• The player with the highest score is ranked number 1 on the leaderboard.
• Players who have equal scores receive the same ranking number, 
and the next player(s) receive the immediately following ranking number.

For example, the four players on the leaderboard have high scores of 100, 90, 90, and 80. 
Those players will have ranks 1, 2, 2, and 3, respectively. 
If Alice's scores are 70, 80 and 105, her rankings after each game are 4th, 3rd and 1st.
'''


import os

def climbingLeaderboard(score, alice):
    scores = [score[0]]
    for i in range(len(score)):
        if score[i] != scores[-1]:
            scores.append(score[i])
            
    result = []
    index = len(scores)-1
    for i in range(len(alice)):
        count = 0
        for j in range(index, -1, -1):
            if alice[i] > scores[0]:
                result.append(1)
                break
            elif alice[i] < scores[j]:
                count = j + 1
                index = j
                result.append(count + 1)
                break
            elif alice[i] == scores[j]:
                count = j
                index = j
                result.append(count + 1)
                break
            elif alice[i] > scores[j]:
                continue
        
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()