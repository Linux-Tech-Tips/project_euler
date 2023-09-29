# Project Euler Problem 26
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# Returns the next digit of a div unit fraction and the remainder
def getNextUnitDigit(div : int, lastRem : int) -> (int, int):
    # If -1 passed as the last remainder, perform the first division step (1/div)
    if lastRem < 0:
        c = 1
    else:
        c = int(str(lastRem) + "0")
    nextDigit = c // div
    rem = c % div
    return (nextDigit, rem)

# Returns the length of a recurring pattern, based on remainders
def recLen(num : int):
    rem = getNextUnitDigit(num, -1)[1]
    rems = []
    idx = 0
    while True:
        rem = getNextUnitDigit(num, rem)[1]
        if rem in rems:
            break
        rems.append(rem)
        idx += 1
    return idx - rems.index(rem)

largest = 0
lastSize = 0
for i in range(1, 1000):
    s = recLen(i)
    if s > lastSize:
        largest = i
        lastSize = s

print("Number:", largest, "Length:", lastSize)