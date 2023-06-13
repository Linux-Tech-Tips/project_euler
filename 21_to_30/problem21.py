# Evaluate the sum of all the amicable numbers under 10000.

# sum of all the proper divisors of a number
def d(n):
    s = 1
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            s += i
    return s

amic = []
for a in range(10000):
    b = d(a)
    if (d(b) == a) and (a != b):
        if a not in amic and b not in amic:
            amic.append(a)
            amic.append(b)

print(sum(amic))

# Not instant, but decently fast, which is enough for now