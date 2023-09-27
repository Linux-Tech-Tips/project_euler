# Project Euler Problem 55
# How many Lychrel numbers are there below ten-thousand?

import math as m

def isP(num):
    s = str(num)
    if len(s) > 1:
        return all([s[i] == s[-1-i] for i in range(round(len(s)/2))])
    else:
        return False

def revSum(num):
    rev = int(str(num)[::-1])
    return (num + rev)

counter = 0

test = []

for i in range(1, 10001):
    # first sum
    tmpS = revSum(i)
    if isP(tmpS):
        counter += 1
    
    # the rest of the sums
    else:
        t = 0
        did = False
        while t < 50:
            newTmpS = revSum(tmpS)
            tmpS = newTmpS
            if isP(tmpS):
                counter += 1
                did = True
                break
            else:
                t += 1
        if not did:
            test.append(i)

print()
print(10000-counter)