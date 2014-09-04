#!/usr/bin/env python
'''
Problem 18 from Project Euler

By starting at the top of the triangle below and moving to adjacent
number on the row below, the maximum total from top to bottom is 23

[ Please se TASK.md for futher details about the triangle ]

That is, 3 + 7 + 4 + 9 = 23.

Fint he maximum total from top to bottom of the triangle below:

[ Please se TASK.md for futher details about the triangle ]

@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.0
'''
# Starting
print "Algorithm starts, plase wait..."
# First we need to define our triangle
# using a simple txt file, we read every lines as a row
triangle = open('numbers.txt').readlines()
# For every row that we founded...
for i in range(0, len(triangle)):
    # ...we need to split every number on each row...
    triangle[i] = triangle[i].replace('\n','').split(' ')
    for j in range(0, len(triangle[i])):
        # ...and convert it into an integer in order to
        # work with it
        triangle[i][j] = int(triangle[i][j])
# Now we can read the triangle from the bottom
# to the top, that's give us a bit performance
for i in range(len(triangle) - 1, 0, -1):
    rowTwo = triangle[i] # Actual row
    rowOne = triangle[i - 1] # Past row
    for j in range(0, len(rowOne)):
        # Sum the numbers that we found
        rowOne[j] += max(rowTwo[j], rowTwo[j + 1])
    triangle[i - 1] = rowOne
# End
print "Algorithm end."
