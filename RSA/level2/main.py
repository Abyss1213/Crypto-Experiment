import ContinuedFractions, Arithmetic
import random

def wiener_hack(e, n):
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    for (k, d) in convergents:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            discr = s * s - 4 * n
            if (discr >= 0):
                t = Arithmetic.is_perfect_square(discr)
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
            y = pow(g, k, n)
            if y != 1 and gcd(y - 1, n) > 1:
                p = gcd(y - 1, n)
                q = n // p
    return p, q


def main():
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


if __name__ == "__main__":
    main()


