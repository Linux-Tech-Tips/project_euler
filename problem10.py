# Project euler problem 10
# Find the sum of all the primes below two million.
import math

def checkPrime(n):
    prime = True
    for i in range(2, math.ceil(math.sqrt(n))+1):
        tmp = (prime and not ((n % i) == 0))
        prime = tmp
    return prime

def nextPrime(n):
    if n == 1:
        return 2
    ul = 2*n # upper limit of the range to search for the prime
    # according to Bertrand-Chebyshev theorem, for any n > 1 exists at least one prime p, for which n < p < 2n
    for i in range(n+1, ul):
        if checkPrime(i):
            return i

# Finds the sum of all primes below a certain number
def sumPrimes(limit):
    total = 0
    prime = 2
    while True:
        if prime >= limit:
            return total
        else:
            total += prime
            tmp = nextPrime(prime)
            prime = tmp

print(sumPrimes(2000000))

# Although it takes around 1-2 minutes, this solves it (?)
# I don't like primes enough to look for a better solution right now
