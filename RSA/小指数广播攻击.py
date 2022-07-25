from gmpy2 import *

def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        a0 = a
        b0 = b
        a = abs(a)  # 用绝对值辗转相除
        b = abs(b)
        g, xt, yt = exgcd(b, a % b)
        x = yt
        y = xt - a // b * yt
        if a0 < 0:  # 经试验，a0<0,b0<0 和 a0<0,b0>0结果绝对值一样
            x = -x
            y = -y
        while x < 0:
            x += b // g  # 使x是最小正整数
            y = (g - a * x) // b
        if a0 * b0 > 0:
            return g, x, y
        else:
            return g, x, -y


def crt(N, c):
    l = len(N)
    m = 1
    for i in N:
        m *= i

    M = []
    for i in range(l):
        M.append(m // N[i])

    I = []
    for i in range(l):
        I.append(exgcd(M[i], N[i])[1])

    res = 0
    for i in range(l):
        res += I[i] * M[i] * c[i]
    res = res % m

    return res, m


if __name__ == '__main__':
    n = int(input())
    e = int(input())
    c = []
    N = []
    for i in range(n):
        c.append(int(input()))
        N.append(int(input()))

    res, mod = crt(N, c)  # crt中国剩余定理。 M做模数数组，C做系数数组，res是解，mod是解的模数，也就是所有n的乘积
    value, bool = iroot(res % mod, e)  # m^e = res%mod
    print(value)

