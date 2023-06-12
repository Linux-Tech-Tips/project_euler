# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import *

count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        day = date(year, month, 1)
        if day.weekday() == 6:
            count += 1
print(count)

# Project Euler developers, thought you were clever?
# ...time to meet Python and its default libraries