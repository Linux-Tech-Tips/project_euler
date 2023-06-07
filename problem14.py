# The following iterative sequence is defined for the set of positive integers:
#  n -> n/2 (n is even)
#  n -> 3n+1 (n is odd)
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

chained = set()

def nextCN(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

def chain(n):
    len = 1
    while n != 1:
        tmp = nextCN(n)
        n = tmp
        chained.add(tmp)
        len += 1
    return len

lN = 1
cI = 0
for i in range(999999, 0, -1):
    if i in chained:
        continue
    c = chain(i)
    if c > lN:
        lN = c
        cI = i

print(cI)

# Takes around 15-20 seconds, probably could be more optimised, but moving on for now