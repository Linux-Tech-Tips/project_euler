# Project Euler Problem 24
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# The program solves the task in around 10 seconds

import itertools

res = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

r2 = []
for i in res:
    tmp = ""
    for j in i:
        tmp += str(j)
    r2.append(tmp)

r2 = sorted(r2)

print(r2[999999])