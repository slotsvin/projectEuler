import sys
from math import sqrt

def is_prime(a):
    return a > 1 and all(a % i for i in range(2, int(sqrt(a)) + 1))


def nthPrime(n):
    count = 1
    for i in range(3, sys.maxsize, 2):
        if is_prime(i):
            count += 1
        if count == n:
            return i


print nthPrime(10001)
