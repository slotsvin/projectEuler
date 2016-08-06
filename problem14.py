def nextCollatzNumber(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1


def CollatzChain(n):
    start = n
    count = 1
    if n == 1:
        return count
    while nextCollatzNumber(start) != 1:
        count += 1
        start = nextCollatzNumber(start)
    return count + 1


def lookForLongestCollatz(n):
    longestChain = 0
    num = 0
    for i in range(1, n):
        chain = CollatzChain(i)
        if chain > longestChain:
            longestChain = chain
            num = i
    return num


print lookForLongestCollatz(1000000)
