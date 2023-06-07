# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

lines = []
with open("problem13.txt", "r") as f:
    lines = f.read().strip().split("\n")

sum = 0
for l in lines:
    sum += int(l)

print(str(sum)[0:10])

# A bit wasteful, but since modern computers are so powerful, here I didn't deem it worth it to make a faster algorithm