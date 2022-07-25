import random
from math import *

# 用辗转相除将分数x/y转为连分数形式
def rational_to_contfrac(x, y):
    a = x // y
    pquotients = [a]
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        pquotients.append(a)
    return pquotients


# 生成渐进分数的分母分子
def contfrac_to_rational(frac):
    if len(frac) == 0:
        return 0, 1
    num = frac[-1]
    denom = 1
    for i in range(-2, -len(frac) - 1, -1):
        num, denom = frac[i] * num + denom, num
    return num, denom

# 求每个渐进分数
def convergents_from_contfrac(frac):
    convs = []
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs


def is_perfect_square(n):
    h = n & 0xF  # last hexadecimal "digit"

    if h > 9:
        return -1  # return immediately in 6 cases out of 16.

    # Take advantage of Boolean short-circuit evaluation
    if (h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8):
        # take square root if you must
        t = isqrt(n)
        if t * t == n:
            return t
        else:
            return -1

    return -1


def fastpow(b, e, p):
    res = 1
    while e > 0:
        if e & 1 == 1:
            res = (res*b) % p
        e = int(bin(e >> 1), 2)
        b = (b*b) % p
    return res


def wiener_hack(e, n):
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
    for (k, d) in convergents:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            discr = s * s - 4 * n
            if (discr >= 0):
                t = is_perfect_square(discr)
                if t != -1 and (s + t) % 2 == 0:
                    return d
    return False


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def getpq(n, e, d):
    p = 1
    q = 1
    while p == 1 and q == 1:
        k = d * e - 1
        g = random.randint(0, n)
        while p == 1 and q == 1 and k % 2 == 0:
            k //= 2
            y = fastpow(g, k, n)
            if y != 1 and gcd(y - 1, n) > 1:
                p = gcd(y - 1, n)
                q = n // p
    return p, q


e = int(input().strip().replace('\n', '').replace('\r', ''))
n = int(input().strip().replace('\n', '').replace('\r', ''))
d = wiener_hack(e, n)
p, q = getpq(n, e, d)
if p < q:
    print(p)
    print(q)
else:
    print(q)
    print(p)
print(d)



