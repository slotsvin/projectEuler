from math import sqrt


def divisors(m):
    count = 0
    for i in range(1, int(sqrt(m)) + 1):
        if m % i == 0:
            if not (m / i == i):
                count += 2
            else:
                count += 1
    return count


def consecSameDivs(m, n):
    consecSameDivisors = 0
    prev = divisors(m)  # number of divisors for 2, to start
    for i in range(m + 1, n):
        numDivs = divisors(i)
        if numDivs == prev:
            consecSameDivisors += 1
        prev = numDivs
        print(i)
    return consecSameDivisors

print consecSameDivs(2, (10**7))