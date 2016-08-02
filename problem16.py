num = 2 ** 1000
s = str(num)
total = 0
for i in range(s.__len__()):
    total += int(s[i])

print total
