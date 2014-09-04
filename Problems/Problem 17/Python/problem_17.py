'''
Problem 17 from Project Euler

If the numbers 1 to 5 re written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.0
'''
MAX = 1000
# First we need to build the dictionary
dictionary = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
# Used to store the sum
summatory = 0;
print "Algorithm start, plase wait..."
# Now we can iterate trough it
for i in range (1,MAX):
    if(not i in dictionary.keys()):
        if(i < (MAX / 10)): # Build every number under 100
            dictionary[i] = dictionary[i / 10 * 10] + dictionary[i % 10]
        else: # Build every number over 100
            dictionary[i] = dictionary[i / (MAX / 10)] + "hundred"
            if(i % (MAX / 10)):
                dictionary[i] += "and" + dictionary[i % (MAX / 10)]
dictionary[MAX] = "onethousand"
for i in dictionary.values():
    summatory += len(i)
# Algorithm end
print "Algorithm end"
