#! /usr/bin/env python
'''
Problem 13 from Project Euler

Work out the first ten digits of the sum of the following on hundred 50-digit numbers
( see the "../numbers.txt" )

PLEASE NOTE
In order interpetate you must have at least Python 2.5+ installed

REGARDING THE PERFORMANCE
This is not he final versione of the script, everyone can improve it. If you have a better solution
please submit a pull request or an issue on Github

@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.0
'''
print "Algorithm start, please wait..."
# Open the file, I don't understand why I must be at the same level...
file = open('numbers.txt', 'r')
# Get the lenght of the file
fileLenght = file.readlines()
# Helpers variable
number = 0
summatory = 0
# Iterate trough the lines
for i in fileLenght:
    # Build the summatory
    summatory += int(fileLenght[number])
    number += 1
# Finish
print "Algorithm end."
