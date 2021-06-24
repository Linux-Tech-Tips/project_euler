# Project euler problem 7
# What is the 10 001st prime number?

import math

def genNextPrime(primes):
    if(len(primes) < 1):
        primes.append(2)
    else:
        n = primes[-1]+1
        while not all([(n % i != 0) for i in range(2, math.ceil(math.sqrt(primes[-1]))+1)]):
            n += 1
        primes.append(n)

primes = []

for i in range(10001):
    genNextPrime(primes)

print(len(primes))
print(primes[-1])
