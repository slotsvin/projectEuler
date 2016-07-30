def sumSquaresDifference(n):

    sumSquares = 0
    squareSum = (((n + 1) / 2) * n) ** 2

    for i in range(1, n + 1):
        sumSquares += i ** 2

    return squareSum - sumSquares


print sumSquaresDifference(100)