def BBS(l, p, q, s):
    n = p * q
    x0 = pow(s, 2, n)
    res = []
    xi = x0
    for i in range(l):
        xi = pow(xi, 2, n)
        bi = xi % 2
        res.append(str(bi))
    out = '0b'
    for j in range(l):
        out += res[l-1-j]  # x1在最低位
    out = int(out, 2)
    return out

l = int(input())
p = int(input())
q = int(input())
s = int(input())
print(BBS(l, p, q, s))

