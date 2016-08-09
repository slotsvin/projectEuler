from math import factorial

count = 0
s = str(factorial(100))
for i in range(s.__len__()):
    count += int(s[i])


print count