#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 17:25:42 2020

@author: suryakantkumar
"""

'''
Problem : In this challenge, you will be given a string. You must remove characters until the string is made up of any two alternating characters. 
When you choose a character to remove, all instances of that character must be removed. Your goal is to create the longest string possible that contains just two alternating letters.

As an example, consider the string abaacdabd. If you delete the character a, you will be left with the string bcdbd. 
Now, removing the character c leaves you with a valid string bdbd having a length of 4. Removing either b or d at any point would not result in a valid string.

Given a string s, convert it to the longest possible string t made up only of alternating characters. 
Print the length of string t on a new line. If no string t can be formed, print 0 instead.

Sample Input : 
10
beabeefeab

Sample Output :
5

Explanation :
The characters present in s are a, b, e, and f. This means that t must consist of two of those characters and we must delete two others. 
Our choices for characters to leave are [a,b], [a,e], [a, f], [b, e], [b, f] and [e, f].

If we delete e and f, the resulting string is babab. This is a valid t as there are only two distinct characters (a and b), and they are alternating within the string.

If we delete a and f, the resulting string is bebeeeb. This is not a valid string t because there are consecutive e's present. Removing them would leave consecutive b's, so this fails to produce a valid string t.

babab is the longest string we can create.
'''


import os

def alternate(s):
    unique = set()
    for e in s:
        unique.add(e)

    li = sorted(list(unique))

    freq = {}
    for i in range(len(li) -1):
        for j in range(i+1, len(li)):
            key = li[i] + li[j]
            freq[key] = ''

    for ele in s:
        for x in freq:
            if ele in x:
                if len(freq[x]) == 0:
                    freq[x] += ele
                else:
                    if freq[x][-1] == ele :
                        freq[x] += '1'
                    elif freq[x][-1] != '1' and freq[x][-1] != ele :
                        freq[x] += ele
            
    maxx = 0
    for ele in freq:
        if len(freq[ele]) > 0:
            if  freq[ele][-1] != '1' and len(freq[ele] ) > maxx:
                maxx = len(freq[ele])
            elif freq[ele][-1] == '1':
                freq[ele] = ''
    
    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input().strip())
    s = input()
    result = alternate(s)
    fptr.write(str(result) + '\n')
    fptr.close()