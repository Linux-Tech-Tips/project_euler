# What is the sum of the digits of the number 2^1000?

# To my surprise, Python just does this, really simply and really quickly

num = str(pow(2, 1000))
result = 0
for i in num:
    result += int(i)
print(result)