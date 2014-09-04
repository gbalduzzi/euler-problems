'''
Problem 42 from Project Euler

The nth term of the sequence of triangle numbers is given by, tn = $n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

REGARDING THE PERFORMANCE
This is not the final version of the Algorithm, anyone can improve it.
If you have a better solution please submit a pull request, or an issue, on Github.

@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.0
'''
# Start
print "Algorithm starts, please wait...\n"
# Opening the .txt file
with open('words.txt') as currentFile:
    words = currentFile.read().replace('"', '').split(',')

# Using lambda function
# To convert any letter in a word to a number corresponding
summatories = sorted(map(lambda w: sum([ord(i) - 64 for i in list(w)]), words))
temp = lambda x: 0.5 * x * (x + 1)

# Check if the word value is a triangle number
triangle = [int(temp(x)) for x in range(1,20) if temp(x) <= max(summatories)]
## Print triangle ##
total = sum([1 for x in summatories if x in triangle])
# End
print "Algorithm end.\n"
