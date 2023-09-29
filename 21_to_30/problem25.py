# Project Euler Problem 25
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

n1 = 1
n2 = 1
idx = 2
while True:
    # Incrementing index
    idx += 1
    tmp = n1 + n2
    # Printing which and exiting after reaching 1000 digits
    if len(str(tmp)) >= 1000:
        print(idx, tmp)
        exit()
    n1 = n2
    n2 = tmp
