#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:49:47 2020

@author: suryakantkumar
"""

'''
Problem : Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters. Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located. The format of Lisa's book is as follows:

° There are n chapters in Lisa's workbook, numbered from 1 to n.
° The ith chapter has arr[i] problems, numbered from 1 to arr[i].
° Each page can hold up to k problems. Only a chapter's last page of exercises may contain fewer than k problems.
° Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
° The page number indexing starts at 1.

Given the details for Lisa's workbook, can you count its number of special problems?

For example, Lisa's workbook contains arr[1] = 4 problems for chapter 1, and arr[2] = 2 problems for chapter 2.
Each page can hold k = 3 problems. The first page will hold 3 problems for chapter 1. Problem 1 is on page 1, so it is special.
Page 2 contains only Chapter 1, Problem 4, so no special problem is on page 2. Chapter 2 problems start on page 3 and there are 2 problems.
Since there is no problem 3 on page 3, there is no special problem on that page either. There is 1 special problem in her workbook.
'''


import os

def workbook(n, k, arr):
    li = []
    for ele in arr:
        i = 0
        a = []
        while i < k - 1 or i < ele:
            if i % k == 0 and i != 0:
                li.append(a)
                a = []
                
            if i < ele:
                a.append(i+1)
                i += 1
            else:
                i += 1
                
        li.append(a)
        
    count = 0
    page = 1
    for i in range(len(li)):
        if page in li[i]:
            count += 1
            page += 1
        else:
            page += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()