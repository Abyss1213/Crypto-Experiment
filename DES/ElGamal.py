from hashlib import sha256
from gmpy2 import invert


def Sign(M, XA, K, a, q):
    m = int(sha256(bytearray(M.encode('utf-8'))).hexdigest(), 16)
    S1 = pow(a, K, q)
    k = invert(K, q-1)
    S2 = (k * (m - XA * S1)) % (q-1)
    return S1, S2


def Vrfy(S1, S2, q, a, YA, M):
    m = int(sha256(bytearray(M.encode('utf-8'))).hexdigest(), 16)
    V1 = pow(a, m, q)
    V2 = pow(YA, S1, q) * pow(S1, S2, q) % q
    if V1 == V2:
        return 'True'
    else:
        return 'False'


q = int(input())
a = int(input())
M = input()
Mode = input()
if Mode == 'Sign':
    XA = int(input())
    K = int(input())
    S1, S2 = Sign(M, XA, K, a, q)
    print(S1, S2)
else:
    YA = int(input())
    S1, S2 = input().split()
    S1 = int(S1)
    S2 = int(S2)
    res = Vrfy(S1, S2, q, a, YA, M)
    print(res)
