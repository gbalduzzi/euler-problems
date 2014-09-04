import time
import string
'''
Problem 22 from Project Euler

Using names.txt, a 45K text file contains over five thousands first names, begin by sorting it
into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position
in the list to obtain a name score

For example, when the list is osrted into alphabetical order, COLIN, shich is worth 3 + 15 + 12 + 9 + 14 = 53 is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.0
'''
# Simple function to sum a single name score
# in order to keep the code a bit clean
def checkPivotScore(name):
    summatory = 0
    for i in name:
        summatory += ord(i) - 64 # Another awesome python function here :P
    return summatory
print "Algorithm starts, please wait..."
start = time.time()
# First we need to open the file
currentFile = open("names.txt")
names = currentFile.read()
names = names.replace('"','').split(",") # A bit of adjustment
names.sort() # Sorting names
currentFile.close()

# Now that we have our list sorted we need to create scores
score = 0 # Our final score
for i in range (0, len(names)):
    score += (i + 1) * checkPivotScore(names[i])
end = time.time()
print "Algorithm end."
print "Total time:", (end - start)
