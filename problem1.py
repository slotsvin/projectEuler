def sum35(n):
	sum = 0

	for i in range(1, int(n/3)+1):
		if i*5 < n:
			sum += i*5
		if not ((i*3) % 5) == 0:
			sum += i*3
	return sum

print sum35(1000)