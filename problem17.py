# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

nums = {"0": 0, "00": 0, "1": 3, "2": 3, "3": 5, "4": 4, "5": 4, "6": 3, "7": 5, "8": 5, "9": 4, "10": 3, \
        "11": 6, "12": 6, "13": 8, "14": 8, "15": 7, "16": 7, "17": 9, "18": 8, "19": 8, "20": 6, \
        "30": 6, "40": 5, "50": 5, "60": 5, "70": 7, "80": 6, "90": 6, "100": 7, "1000": 8}

def getLen(num):
    sNum = str(num)
    if num <= 20:
        return nums[sNum]
    elif num < 100:
        return nums[sNum[0] + "0"] + nums[sNum[1]]
    elif num < 1000:
        return nums[sNum[0]] + nums["100"] + (3 if sNum[1:3] != "00" else 0) + ((nums[sNum[1] + "0"] + nums[sNum[2]]) if int(sNum[1:3]) > 20 else (nums[sNum[1:3]] if int(sNum[1:3]) > 9 else nums[sNum[2]]))
    else:
        return nums[sNum[0]] + nums["1000"]

sum = 0
for i in range(1, 1001):
    sum += getLen(i)
print(sum)

# Works well enough