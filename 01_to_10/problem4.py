# Project euler problem 4
# Largest palindrome number made from the multiplication of 2 3-digit numbers

def isp(num):
    n2 = str(num)
    return all([n2[i] == n2[-1-i] for i in range(round(len(n2)/2))])

def find():
    res = 0
    # Range to 900 because still works lol
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            c = i * j
            if isp(c) and c > res:
                res = c
    return res

print(find())
