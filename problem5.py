# Project euler problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Given info: 2520 smallest divisible by all from 1 to 10

res = 0
i = 2520

while res == 0:
    if all([i % n == 0 for n in range(1, 21)]):
        res = i
    else:
        # For a number to be divisible by all from 1 to 20, it has to be divisible by all from 1 to 10, so it has to be divisible by this, the smallest number that is
        i += 2520

print(res)
