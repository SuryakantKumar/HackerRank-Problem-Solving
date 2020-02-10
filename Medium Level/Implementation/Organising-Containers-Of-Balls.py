#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:48:10 2020

@author: suryakantkumar
"""

'''
Problem : David has several containers, each with a number of balls in it. 
He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.

As an example, David has n = 2 containers and 2 different types of balls, both of which are numbered from 0 to n-1 = 1. 
The distribution of ball types per container are described by an n * n matrix of integers, M[container][type].
'''


import os

def organizingContainers(container):
    n = len(container)
    ball_type = [0] * n
    container_type = [0] * n

    for i in range(n):
        ball_count = 0
        container_capacity = 0
        for j in range(n):
            ball_count += container[j][i]
            container_capacity += container[i][j]
            
        ball_type[i] = ball_count
        container_type[i] = container_capacity

    if sorted(ball_type) == sorted(container_type):
        return 'Possible'
    else:
        return 'Impossible'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        result = organizingContainers(container)
        fptr.write(result + '\n')
    fptr.close()