# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

import math

# Combinatorics says:
#   basically, 20x R, 20x D
#   so, unique permutations of length 40 string -> 40!
#   order of each R or each D doesn't matter -> unique ordered strings of R - 20!, of D - 20!
#   -> total amount of paths is 40!/(20!*20!)

print("Answer:", math.factorial(40) / (math.factorial(20)*math.factorial(20)))