#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:59:46 2020

@author: suryakantkumar
"""

'''
Problem : Priyanka works for an international toy company that ships by container. 
Her task is to the determine the lowest cost way to combine her orders for shipping. 
She has a list of item weights. The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item. 
All items meeting that requirement will be shipped in one container.

What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?

For example, there are items with weights w = [1, 2, 3, 4, 5, 10, 11, 12, 13]. 
This can be broken into two containers: [1, 2, 3, 4, 5] and [10, 11, 12, 13]. 
Each container will contain items weighing within 4 units of the minimum weight item.
'''


import os

def toys(w):
    w = sorted(w)

    count = 1
    mini = w[0]
    for i in range(len(w)):
        if w[i] > mini + 4:
            count += 1
            mini = w[i]

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    fptr.write(str(result) + '\n')
    fptr.close()