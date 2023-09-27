# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# sum of all the proper divisors of a number
def d(n):
    s = 1
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            s += i
    return s

# get the next abundant number following n
def getNextAb(n):
    n += 1
    while True:
        if(d(n) > n):
            return n
        else:
            n += 1

abn = [12]

final = 0

# Program works, but ran for a total of 30 minutes, 54.452 seconds, on an i7 laptop - definitely room for improvements

for i in range(1, 28123):
    # Getting the next abundant number (getting all until 28123 takes approx. 10 s)
    lastAb = abn[-1]
    while lastAb < i:
        abn.append(getNextAb(lastAb))
        lastAb = abn[-1]
    
    # checking if i is the sum of abundant numbers
    isSum = False
    print("currently at:", i)
    for j in range(len(abn)):
        if isSum:
            break
        for k in range(j, len(abn)):
            if abn[j] + abn[k] == i:
                isSum = True
                break
    
    if not isSum:
        final += i

print(final)