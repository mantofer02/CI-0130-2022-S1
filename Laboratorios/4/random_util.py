P = 5


def good_abm(n):
    m = n + 1
    while (not is_prime(m)):
        m += 1

    b = m + 1
    while (not is_prime(b)):
        b += 1

    p = P
    a = (p*m) + 1
    return (a, b, m)


def is_prime(n):
    n_is_prime = True
    if n > 1:
        for i in range(2, n//2 + 1):
            if (n % i) == 0:
                n_is_prime = False
                break
    return n_is_prime
