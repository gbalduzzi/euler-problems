from operator import mul
'''
Problem 40 from Project Euler

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

REGARDING THE PERFORMANCE
This is not the final version of the Algorithm, anyone can improve it.
If you have a better solution please submit a pull request, or an issue, on Github.

@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.0
'''
# Very easy, and lazy, solution with Python
# Defining a simple summatory for d(n)
def summatory(k):
    # The number of digits from 1 to 9 is 9,
    # the number of digits from 1 to 99 is 189,
    # the number of digits from 1 to 999 is 2889, etc.
    return (10**k * (9 * k - 1) + 1) / 9

def d(n):
    k = 0
    while 1:
        if(summatory(k + 1) >= n): break
        k += 1
    k += 1
    number = 10**(k - 1) + (n - summatory(k - 1)) // k - 1
    reminder = (n - summatory(k - 1)) % k
    if(reminder == 0):
        return int(str(number)[-1])
    else:
        return int(str(number + 1)[reminder - 1])

print reduce(mul,[d(10**i) for i in range(7)]) # 1000
