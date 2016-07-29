from math import sqrt;
from itertools import count, islice

def isPrime(n):
    return (n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1))))

def largestPrimeFactor(n):
	root = int(sqrt(n)) + 1
	largest = -1
	for i in range(root, 1, -1):
		if n % i == 0:
			if isPrime(i):
				return i

print largestPrimeFactor(600851475143)