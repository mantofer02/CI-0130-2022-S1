import math as ma
P = 11


def good_abm(n):
    k = int(ma.log2(n))
    m = pow(2, k)
    while (m < n):
        k += 1
        m = pow(2, k)

    c = n + 1
    a = 4*c + 1

    b = a + 1

    if (b % 2 == 0):
        b += 1

    return (a, b, m)


def is_prime(n):
    n_is_prime = True
    if n > 1:
        for i in range(2, n//2 + 1):
            if (n % i) == 0:
                n_is_prime = False
                break
    return n_is_prime
