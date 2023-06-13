# Using the given 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# (The alphabetical value of a name is the sum of the alphabetical positions of the letters)
# What is the total of all the name scores in the file?

def getNames(fileName):
    names = []
    with open(fileName, "r") as f:
        names = f.read().strip().replace("\"", "").split(",")
    return names

def nameVal(name):
    val = 0
    for ch in name:
        val += ord(ch)-64
    return val

names = getNames("problem22.txt")
names.sort()

s = 0
for i in range(len(names)):
    s += (nameVal(names[i]) * (i+1))
print(s)

# Works nice and fast, thanks default Python sort!