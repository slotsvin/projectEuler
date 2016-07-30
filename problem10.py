from math import sqrt


def is_prime(a):
    return a > 1 and all(a % i for i in range(2, int(sqrt(a)) + 1))

def sumOfPrimes(n):
    total = 0
    for i in range(2, n):
        if is_prime(i):
            total += i
    return total


print sumOfPrimes(2000000)
