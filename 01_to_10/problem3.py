# Project euler problem 3
# Prime factorization
import math

def genNextPrime(primes):
    n = primes[-1]+1
    while not all([(n % i != 0) for i in range(2, math.ceil(math.sqrt(primes[-1]))+1)]):
        n += 1
    primes.append(n)
    return primes

p = [2, 3, 5, 7, 11, 13]
number = 600851475143
factors = []

while True:
    for i in p:
        if number % i == 0:
            factors.append(i)
            number /= i
            continue
    if number == 1:
        break
    else:
        p = genNextPrime(p)

print(factors, "\n", max(factors))
