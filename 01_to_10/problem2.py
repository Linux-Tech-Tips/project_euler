# Project euler: problem 1
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

l1 = 1
l2 = 2
total = 0
limit = 4000000
#limit = 10

while l1 < limit:
    total += l1 if (l1 % 2 == 0) else 0
    c = l1 + l2
    l1 = l2
    l2 = c

print(total)
