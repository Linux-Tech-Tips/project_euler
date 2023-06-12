# Project euler problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

# generating triples using Euclid's formula
def genTriple(m, n):
    return [(m*m - n*n), (2 * m * n), (m*m + n*n)]

# finding triplets (ranges that are small but still work)
for m in range(100):
    for n in range(10):
        if sum((genTriple(m, n))) == 1000:
            print(genTriple(m, n))
