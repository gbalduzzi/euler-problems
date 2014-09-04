'''

Problem 4 from Project Euler

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is '9009' = '91' times '99'.

Find the largest palindrome made from the product of two 3-digit numbers.

PLEASE NOTE
In order to work you should have at least Python 2.3+ install, 2.7+ is reccomended.

REGARDING THE PERFORMANCE
This is not the final version of the algorithm, everyone can improve it.

@author
@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.1

'''

# Support function to check if a number is palindromic
def isPalindromic(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i]!=n[len(n)-i-1]:
            return False
    return True


maxPalidomic = 0

for i in range(1000,100,-1):
    for j in range(1000, 100,-1):
        if isPalindromic(i*j):
            if i*j>maxPalidomic:
                maxPalidomic = i*j
