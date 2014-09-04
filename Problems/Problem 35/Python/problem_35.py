#|/bin/python
from math import sqrt
'''
Problem 35 from Project Euler

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

REGARDING THE PERFORMANCE
This is not the final version of the Algorithm, anyone can improve it.
If you have a better solution please submit a pull request, or an issue,
on github.

@author Claudio Ludovico Panetta (@Ludo237)

@versio 1.0.0
'''
MAX = 10**6;
# Get next prime from a given number
def next_prime(n):
    if(is_prime(n)):
        n += 1
    if(n % 2 == 0) and (n != 2):
        n += 1
    while True:
        if(is_prime(n)):
            break;
        n += 2
    return n
# Check if a number is prime
def is_prime(n):
    if(n == 2) or (n == 3):
        return True
    elif(n < 2) or (n % 2 == 0):
        return False
    elif(n % 3 == 0):
        return False
    maximum = n**0.5+1
    start = 3
    while start < maximum:
        if(n % i == 0):
            return False
        i+=2
    return True

# Define a function that rotate the given number
def rotated(n):
    digits = list(str(n))
    for i in range(len(digits)):
        digits.insert(0, digits.pop())
        yield int(''.join(digits))

# Define a new exception to pass
class Skip(Exception): pass

count = 0
i = 0
print "Algorithm starts please wait...\n"
# Starts
while i < MAX:
    try:
        for j in rotated(i):
            if not is_prime(j):
                # We do not care if is not prime
                raise Skip
        count += 1
    except Skip:
        pass
        i = next_prime(i)
# Finish
print "Algorithm end.\n"
print count
