#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 6 10:22:29 2020

@author: suryakantkumar
"""

'''
Problem : Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, 
awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet a = (a[0], a[1], a[2]), 
and the rating for Bob's challenge to be the triplet b = (b[0], b[1], b[2]).

Your task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.
Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.

For example, a = [1, 2, 3] and b = [3, 2, 1]. For elements 0, Bob is awarded a point because a[0] < b[0]. 
For the equal elements a[1] and b[1], no points are earned. Finally, for elements 2, a[2] > b[2] so Alice receives a point. 
Your return array would be [1, 1] with Alice's score first and Bob's second.
'''


import os

def compareTriplets(a, b):
    point_a = 0
    point_b = 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            point_a += 1
            
        elif a[i] < b[i]:
            point_b += 1
            
    return point_a, point_b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    
