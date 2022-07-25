def fastpow(b, e, p):
    res = 1
    while e > 0:
        if e & 1 == 1:
            res = (res*b) % p
        e = int(bin(e >> 1), 2)
        b = (b*b) % p
    return res

b,e,p = input().split()
b = int(b)
e = int(e)
p = int(p)
print(fastpow(b, e, p))