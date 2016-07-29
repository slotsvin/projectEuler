def fibSumEvens(n):
	sum = 0
	num1, num2 = 1, 2
	while num1 < n:
		if num2 % 2 == 0:
			sum += num2
		num1, num2 = num2, num1 + num2
	return sum


print fibSumEvens(4000000)
