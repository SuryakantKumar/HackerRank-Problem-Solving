#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:27:42 2020

@author: suryakantkumar
"""

'''
Problem : Flatland is a country with a number of cities, some of which have space stations. 
Cities are numbered consecutively and each has a road of 1 km length connecting it to the next city. 
It is not a circular route, so the first city doesn't connect with the last city. 
Determine the maximum distance from any city to it's nearest space station.

For example, there are n = 3 cities and m = 1 of them has a space station, city 1. 
They occur consecutively along a route. City 2 is 2 - 1 = 1 unit away and city 3 is 3 - 1 = 2 units away. 
City 1 is 0 units from its nearest space station as one is located there. The maximum distance is 2.
'''


#### Solution 01: Ordinary Approach

import os

def flatlandSpaceStations(n, c):
    maxx = 0
    for i in range(n):
        mini = 123456789
        for ele in c:
            diff = ele - i
            if diff < 0:
                diff *= -1    
            if diff < mini:
                mini = diff  
                
        if mini >= maxx:
            maxx = mini
            
    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    fptr.write(str(result) + '\n')
    fptr.close()
    
    

#### Solution 02 : Optimal Approach
    
import os

def flatlandSpaceStations(n, c):
    if n == len(c):
        return 0

    c = sorted(c)
    front = (c[0] - 0)
    back = (n-1 - c[len(c) - 1])

    maxx  = front if front >= back else back
    
    for i in range(len(c) - 1):
        dis = (c[i+1] - c[i]) // 2
        if dis > maxx:
            maxx = dis
            
    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    fptr.write(str(result) + '\n')
    fptr.close()