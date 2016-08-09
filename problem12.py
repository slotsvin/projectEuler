from math import sqrt


def triangleNumDivisors(n):
    num = 1
    i = 2
    while(1):
        if divisors(num) >= n:
            return num
        num += i
        i += 1


def divisors(m):
    count = 0
    for i in range(1, int(sqrt(m)) + 1):
        if m % i == 0:
            if not (m / i == i):
                count += 2
            else:
                count += 1
    return count


print triangleNumDivisors(500)
