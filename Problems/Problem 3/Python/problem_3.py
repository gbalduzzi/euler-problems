'''
Problem 3 from Project Euler

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

This file is made with Sublime Text using Python 2.7.4 on Linux.

PLEASE NOTE
In order to work you should have at least Python 2.5.x+ (Python 2.7.x+ is better)

REGARDING THE PERFORMANCE
This is not the final version of this algorithm, I'll trace the version of every solution. For any suggest of improvments please
open an issue or a pull request.

@author Matteo Manchi (@matteomanchi)
@version 1.0
'''

def is_prime(n):
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

# Smart and fast with generators
def getPrimeNumber():
    yield 2;

    i = 3

    while True:
        if is_prime(i):
            yield i
        i += 2


target = 600851475143

primeFactors = []

primeNumbers = getPrimeNumber();
lastPrimeNumber = next(primeNumbers);

while target > 1:
    if target % lastPrimeNumber == 0:
        target /= lastPrimeNumber;
        primeFactors.append(lastPrimeNumber);
    else:
        lastPrimeNumber = next(primeNumbers);
