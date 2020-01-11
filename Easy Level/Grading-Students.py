#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 6 12:28:46 2020

@author: suryakantkumar
"""

'''
Problem : HackerLand University has the following grading policy:

° Every student receives a grade in the inclusive range from 0 to 100.
° Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

° If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
° If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

For example, grade = 84 will be rounded to 85 but grade = 29 will not be rounded because the rounding would result in a number that is less than 40.

Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.
'''


def gradingStudents(grades):
    n = len(grades)
    final_grades = [0]*n

    for i in range(n):
        ele = grades[i]
        nearest_multiple = ele + 5 - (ele % 5)

        if (ele < 40):
            if ((nearest_multiple - ele) < 3) and (nearest_multiple == 40):
                final_grades[i] = nearest_multiple
            else:
                final_grades[i] = ele            
        else:
            if (nearest_multiple - ele) < 3:
                final_grades[i] = nearest_multiple

            if (nearest_multiple - ele) >= 3:
                final_grades[i] = ele

    return final_grades

grades_count = int(input())

grades = []
for i in range(grades_count):
    grades_item = int(input())
    grades.append(grades_item)
    
result = gradingStudents(grades)
for ele in result:
    print(ele)