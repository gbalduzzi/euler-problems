'''
Problem 1 from Project Euler

If we list all the natural numbers below 10 that are multiples of 3 and 5, we get 3, 5, 6 and 9. The sum of these multipes is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

This file is made with VIM using Python 3 on Mac osX.

@author Andrea Benfatti (@Benfa94)
'''

size = 999
# numberOfMultiple*(lastMultiple + firstMultiple)/2

nMultiplesOf3 = size//3
nMultiplesOf5 = size//5
nMultiplesOf15 = size//15

maxMultipleOf3 = nMultiplesOf3 * 3
maxMultipleOf5 = nMultiplesOf5 * 5
maxMultipleOf15 = nMultiplesOf15 * 15

sumMultiples3 = nMultiplesOf3*(maxMultipleOf3+3)/2
sumMultiples5 = nMultiplesOf5*(maxMultipleOf5+5)/2
sumMultiples15 = nMultiplesOf15*(maxMultipleOf15+15)/2
total = sumMultiples3 + sumMultiples5 - sumMultiples15


