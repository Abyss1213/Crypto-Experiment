def inverse(u, v):  # 辗转相除求逆
    u2, v2 = int(u), int(v)
    u1, v1 = 1, 0
    while v2 > 0:
        q = divmod(u2, v2)[0]  # divmod(x, y, /) Return the tuple (x//y, x%y)
        u1, v1 = v1, u1 - v1 * q
        u2, v2 = v2, u2 - v2 * q
    while u1 < 0:
        u1 = u1 + v
    return u1

def crtdecode(c, d, p, q):  # 中国剩余定理加速解密
    m1 = pow(c % p, d % (p - 1), p)
    m2 = pow(c % q, d % (q - 1), q)
    a = inverse(q, p)
    b = inverse(p, q)
    m = (m1 * a * q + m2 * b * p) % (p * q)
    return m


def RSA(p, q, e, m, op):
    n = p * q
    if op == 1:
        res = pow(m, e, n)
    else:
        phi = (p-1) * (q-1)
        d = inverse(e, phi)
        # res = pow(m, d, n)
        res = crtdecode(m, d, p, q)
    return res


p = int(input())
q = int(input())
e = int(input())
m = int(input())
op = int(input())
print(RSA(p, q, e, m, op))