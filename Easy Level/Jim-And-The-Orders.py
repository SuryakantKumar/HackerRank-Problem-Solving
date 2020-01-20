#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:30:11 2020

@author: suryakantkumar
"""


'''
Problem : Jim's Burgers has a line of hungry customers. 
Orders vary in the time it takes to prepare them. Determine the order the customers receive their orders. 
Start by numbering each of the customers from 1 to n, front of the line to the back. 
You will then be given an order number and a preparation time for each customer.

The time of delivery is calculated as the sum of the order number and the preparation time. 
If two orders are delivered at the same time, assume they are delivered in ascending customer number order.

For example, there are n = 5 customers in line. They each receive an order number order[i] and a preparation time prep[i].:

Customer	    1	2	3	4	5
Order #		8	5	6	2	4
Prep time	3	6	2	3	3
Calculate:
Serve time	11	11	8	5	7

We see that the orders are delivered to customers in the following order:

Order by:
Serve time	5	7	8	11	11
Customer	    4	5	3	1	2
'''


import os

def jimOrders(orders):
    time = []
    for e in orders:
        time.append(e[0] + e[1])

    freq = {v : i +1 for i, v in enumerate(sorted(time))}
        
    li = []
    for ele in freq:
        for i in range(len(time)):
            if time[i] == ele:
                li.append(i + 1)
                time[i] = -1
        
    return  li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))
    result = jimOrders(orders)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()