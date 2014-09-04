#!/usr/bin/env python
import time,math
'''
    By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
    
    By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
    
    Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''

# IT WORKS - 10 (s).

def find_prime_family():
    
    # Thoughts:
    # Convert prime to string
    # Remove last digit (can't replace it with 0,2,4,6, or 8 cause it won't be prime)
    # Convert to list, sort, and remove repeats
    # Loop through each of the "numbers" this list contains and replace them in the prime
    # and test if the new number is a prime number (do this for 0-9).  Don't replace last digit.
    
    # This might not work tho'.  What about 35335, where the only digits you wanna replace are the "33" in the middle
    # definitely doesn't work for all possible solutions - but see how it works.  "Not necessarily adjacent digits"
    # Actually it might work...  we'll see.
    
    # Generate a list of primes to a million (may need to test higher - but answer is probably < 10million)
    primes = find_primes(1e6,[])
    
    # Smallest 7 prime family starts at 56003, so rule out all primes below that.
    # Use dictionary for lookups - has_key much faster than "in list"
    prime_dict = {}
    primes_short = []
    for prime in primes[:]:
        if prime > 56000:
            prime_dict[prime] = 1
            primes_short.append(prime)
    
    # Loop through and search for Eight Prime Families.
    test_nums = [str(i) for i in range(0,10) ]
    match_dict = {}
    match_found = False
    for prime in primes_short[:]:
        match_dict[prime] = []
        prime_str = str(prime)
        prime_stub = prime_str[:-1]
        last_digit = prime_str[-1]
        
        prime_stub_list = list(prime_stub)
        prime_stub_list.sort()
        unique_list = list(set(prime_stub_list))
        
        for num in unique_list[:]:
            for i in test_nums:
                temp_stub = prime_stub
                temp_stub = temp_stub.replace(num,str(i))
                temp_num = int(temp_stub + last_digit)
                if prime_dict.has_key(temp_num):
                    match_dict[prime].append(temp_num)
            if len(match_dict[prime][:]) == 8:
                match_found = True
                break
            else:
                match_dict[prime] = []
        if match_found == True:
            print prime
            print match_dict[prime]
            match_found = False

#############################################################
# Functions from Problem #35 - Circular Primes.
#############################################################

# Function inputs a number and list of prime divisors
# It will add to the input list of prime divisors all prime numbers
# computed up to the input number (input = 9,[2,3] - returns list: [2,3,5,7])
def find_primes(max_num,prime_divisors):
    if len(prime_divisors) < 2:
        prime_divisors = [2,3]
    num = prime_divisors[-1] + 2
    while num < max_num:
        if is_prime(num,prime_divisors):
            prime_divisors.append(num)
        num += 2
    return prime_divisors

# Determine if the passed num is a prime number (True or False)
def is_prime(num,prime_divisors):
    max_divisor = int(math.sqrt(num)) + 1
    
    # If the input prime number (num) is divisible by any of the primes
    # then it itself is not prime.
    # When divisor exceeds max divisor, break out of loop, and return True
    if num == 1:
        return False
    elif num in [2,3,5,7]:
        return True
    for divisor in prime_divisors:
        if num % divisor == 0:
            return False
        if divisor > max_divisor:
            break
    return True


# Determine Start Time
start_time = time.time()

# Execute main program.
find_prime_family()

# Determine Exec Time
exec_time = time.time() - start_time
print 'Total Execution Time: ' + exec_time.__str__() + '(s)'