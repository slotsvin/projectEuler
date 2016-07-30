def specialPythTriplet(n):
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                if ((i + j + k) == n) and (((i ** 2) + (j ** 2) == (k ** 2)) or ((i ** 2) + (k ** 2) == (j ** 2))
                                           or ((j ** 2) + (k ** 2) == (i ** 2))):
                    return i*j*k


print specialPythTriplet(1000)
