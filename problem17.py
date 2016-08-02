from num2words import num2words

total = 0
for i in range(1, 1001):
    for j in num2words(i).replace('-', ' ').split():
        total += j.__len__()

print(total)