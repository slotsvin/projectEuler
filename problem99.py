import math

with open("problem99base_exp.txt") as nums:
    listOfNums = nums.readlines()

largest = 0
pair = ''
for i in range(listOfNums.__len__()):
    listOfNums[i] = listOfNums[i].replace('\n', '').replace(',', ' ')
for j in range(listOfNums.__len__()):
    a = listOfNums[j].split()
    if int(a[1]) * math.log(int(a[0]), 10) > largest:
        largest = math.log(int(a[0]), 10) * int(a[1])
        pair = j

print pair