# Project Euler Problem 27
# Find the product of the coefficients, a and b, 
# for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
# starting with n = 0.

# Equation: n^2 + an + b
# Where |a| < 1000, |b| <= 1000

import math

# Is Prime function taken from problem 10
def isPrime(n):
    prime = True
    # Check for negative input
    if n <= 1:
        return False
    # Finding prime
    for i in range(2, math.ceil(math.sqrt(n))+1):
        tmp = (prime and not ((n % i) == 0))
        prime = tmp
        if prime == False:
            return False
    return prime

# Function function
def getFn(a, b, n):
    return ((n*n) + (a*n) + b)

# Going through all possible coefficients, trying combinations and testing for primes
largest = 0
la = 0
lb = 0
for a in range (-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while True:
            if not isPrime(getFn(a, b, n)):
                break
            n += 1
        if n > largest:
            largest = n
            la = a
            lb = b

print("Longest sequence:", largest, "Product:", la * lb)