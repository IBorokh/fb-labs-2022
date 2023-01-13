from random import randint
from numpy import gcd


def miller_rabin_test(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0:
        return False

    d = num - 1
    s = 0
    while d % 2 == 0:
        d = d // 2
        s += 1

    x = randint(2, num - 2)

    if gcd(x, num) > 1:
        return False
    elif (x**d % num == 1) or (x**d % num == -1):
        return True

    for i in range(1, s - 1):
        x = (x ** 2) % num
        if x == -1:
            return True
        if x == 1:
            return False
    return False


def random_search(n_max, n_min=0):
    x = randint(n_min, n_max)

    m = x
    if x % 2 == 0:
        m = x + 1

    k = m
    found = False
    for i in range(m, int((n_max - m) / 2)):
        k = m + (2 * i)
        if miller_rabin_test(k):
            found = True
            break
    if not found:
        return random_search(n_max, n_min)
    return k



