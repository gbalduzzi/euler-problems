'''
Problem 43 from Project Euler

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

REGARDING THE PERFORMANCE
This is not the final version of the Algorithm, anyone can improve it
If you have a better solution please submit a pull request, or an issue, on Github

@author Claudio Ludovico Panetta (@Ludo237)

@version 1.0.0
'''
# Start
print "Algorithm starts, please wait..."
# For this algorithm I choose
# to use recursive approach
def core(number, lenght, used):
    # Useful array for the very first primes
    first_primes = [1,1,1,2,3,5,7,11,13,17]
    total = 0
    if lenght == 10:
        return number
    for i in range(10):
        if not used[i]:
            if((10 * number + i) % 1000) % first_primes[lenght] == 0:
                used[i] = 1
                total += core(10 * number + i, lenght + 1, used)
                used[i] = 0
    return total
# Run the core
core(0,0,[0,0,0,0,0,0,0,0,0,0])
print "Algorithm end"
