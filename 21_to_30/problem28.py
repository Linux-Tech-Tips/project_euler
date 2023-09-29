# Project Euler Problem 28
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31

# given layer number l
# and a previous number n'
# the following number is n' + 2*l


# Based on the previous hypothesis, solving the problem is very straightforward

sum = 1
lastN = 1

for layer in range(1, 501):
    for i in range(4):
        lastN = lastN + 2*layer
        sum += lastN

print(sum)