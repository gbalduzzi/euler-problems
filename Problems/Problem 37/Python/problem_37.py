'''
Problem 37 from Project Euler

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

REGARDING THE PERFORMANCE
This is not the final version of the script, anyone can improve it.
If you have a better solution please submit a pull request, or an issue, on Github.

@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.0
'''
# Algorithm limit
LIMIT = 1 * (10**6)
# Primes number in a fancy array with all True
primes = [True for i in range(LIMIT)]
# Except for the first 2 position
primes[0] = primes[1] = False
# Start
print "Algorithm starts, please wait.."
# Filter every other non-prime numbers from the array
for i in range (2, LIMIT):
    if primes[i]:
        for j in range (2 * i, LIMIT, i):
            primes[j] = False

# We have now a fancy array with i-position for prime (True) and not prime (False)
# Helper variables
total = 0
for i in range (10, LIMIT):
    if primes[i]:
        # Other helpers
        left, right, multiplier, flag = i,0,1,True
        while(flag and left > 0):
            right += (left % 10) * multiplier
            flag = primes[right] and primes[left]
            multiplier *= 10
            left /= 10

        if flag:
            total += i

print "Algorithm end.\n"
