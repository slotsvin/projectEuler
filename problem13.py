with open('problem13numbers.txt') as nums:
    lines = nums.readlines()

total = 0
for num in lines:
    total += int(num[:12])

print int(str(total)[:10])
