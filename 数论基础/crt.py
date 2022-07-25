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


def crt(a1, a2, a3, b1, b2, b3):
    m = a1 * a2 * a3
    M1 = m // a1
    M2 = m // a2
    M3 = m // a3
    I1 = exgcd(M1, a1)[1]
    I2 = exgcd(M2, a2)[1]
    I3 = exgcd(M3, a3)[1]
    res = (I1 * M1 * b1 + I2 * M2 * b2 + I3 * M3 * b3) % m
    while res > 0:
        res -= m
    if res < 0:
        res += m
    if res == 0:
        res = m
    return res


a1, a2, a3 = input().split()
b1, b2, b3 = input().split()
print(crt(int(a1), int(a2), int(a3), int(b1), int(b2), int(b3)))
