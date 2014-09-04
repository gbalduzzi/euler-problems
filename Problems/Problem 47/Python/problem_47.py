'''
Problem 47 from Project Euler
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''
print "Algorithm starts please wait..."
max_numbers = 1000000
factors = [0] * max_numbers;
for i in range(2, max_numbers):
    if factors[i] == 0:
        for j in range(2*i, max_numbers, i):
            factors[j] += 1

total = [4] * 4;

for i in range(2, max_numbers):
    if factors[i:i+4] == total:
        print i
        break
print "Algorithm end"
