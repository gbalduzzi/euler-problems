'''
Problem 32 from Project Euler

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.i
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

REGARDIND THE PERFORMANCE
This is not the final version of the Algorithm, anyone can improve it.
If you have a better solution please submit a pull request, or an issue, on Github.

@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.0
'''
# "Costants" for our algorithm
MAX = 10000
LOOP = 100

# Creating a simple function so we can keep the code a bit clear
def pand_digital(i, j):
    product = i *j
    summatory = str(i) + str(j) + str(product)
    digits = set(summatory)
    if '0' in summatory:
        return False
    if len(digits) == 9 and len(summatory) == 9:
        return True
    else:
        return False
# The core of our algorithm
print "Algorithm starts, plase wait...\n"
# Using a simple list, lazy boy
digits = set()
# Looping
for i in range(0, LOOP):
    for j in range(i, MAX):
        # If we found a pandigital number
        if(pand_digital(i, j)):
            # Add it
            digits.add(i *j)

print "Algorithm End\n"
