# Project Euler Problem 30
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# The complexity of the program is nearing linear, which allows us to set a very high limit
# Given a sufficiently high limit, one can assume that no more numbers fit the desired property
# Therefore, a simple algorithm which tests all options until a certain number solves the problem

# <3 bruteforce

def powerDigits(num):
    return sum([int(x)**5 for x in str(num)])

nums = []
counter = 2
unfound = 0
limit = 1000000 # With a limit of 1,000,000 the program runs approx. 2-3 seconds, which is good enough for this use case
while unfound < limit:
    if(counter == powerDigits(counter)):
        nums.append(counter)
        unfound = 0
    else:
        unfound += 1
    counter += 1

print(sum(nums), nums)