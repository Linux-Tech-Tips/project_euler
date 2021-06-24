# Project euler problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_squares = sum([i*i for i in range(1, 101)])
square_sums = pow(sum([i for i in range(1, 101)]), 2)
print(square_sums - sum_squares)
