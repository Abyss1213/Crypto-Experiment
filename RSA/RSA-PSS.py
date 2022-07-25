from hashlib import sha1
import sys
from math import ceil

def MGF(x, maskLen):  # x是去掉0x的十六进制串
    Hlen = 20
    T = bytearray(b'')
    k = maskLen // Hlen
    if len(x) & 1 == 1:
        x = '0' + x
    X = bytearray.fromhex(x)
    if maskLen % Hlen == 0:
        k -= 1
    for i in range(k + 1):
        tmp = X + bytearray.fromhex('%08x' % i)
        T = T + bytearray.fromhex(sha1(tmp).hexdigest())
    mask = T[:maskLen]
    return mask.hex()


def RSA_PSS_Sign(M, n, emBits, salt, d):
    mHash = sha1(bytearray(M.encode('utf-8'))).hexdigest()
    padding1 = '00'* 8
    M1 = padding1 + mHash + salt
    H = sha1(bytes.fromhex(M1)).hexdigest()
    sLen = 20
    hLen = 20
    emLen = ceil(emBits / 8)
    padding2 = '00'*(emLen-sLen-hLen)+'01'
    DB = padding2 + salt
    dbMask = MGF(H, emLen - hLen - 1)
    maskedDB = hex(int(DB, 16) ^ int(dbMask, 16))[2:].zfill(len(DB))
    maskedDB = '0'*(8*emLen-emBits) + maskedDB[8*emLen-emBits:]
    EM = maskedDB + H +'bc'
    s = pow(int(EM, 16), d, n)
    k = 1024//8
    S = hex(s)[2:].zfill(2*k)
    return S


def RSA_PSS_Vrfy(M, n, emBits, S, e):
    hLen = 20
    sLen = 20
    s = int(S, 16)
    m = pow(s, e, n)
    emLen = ceil(emBits/8)
    EM = hex(m)[2:].zfill(emLen)
    mHash = sha1(bytearray(M.encode('utf-8'))).hexdigest()
    maskedDB = EM[:2*(emLen-hLen-1)]
    H = EM[2*(emLen-hLen-1):-2]
    dbMask = MGF(H, emLen-hLen-1)
    DB = hex(int(maskedDB, 16) ^ int(dbMask, 16))[2:].zfill(len(maskedDB))
    DB = '0' * (8 * emLen - emBits) + DB[8 * emLen - emBits:]
    salt = DB[-sLen*2:]
    padding1 = '00' * 8
    M1 = padding1 + mHash + salt
    H1 = sha1(bytes.fromhex(M1)).hexdigest()
    if H1 == H:
        return 'True'
    else:
        return 'False'


def main():
    M = input()
    n = int(input())
    emBits = int(input())
    Mode = input()
    if Mode == 'Sign':
        d = int(input())
        salt = input()
        print(RSA_PSS_Sign(M, n, emBits, salt, d))
    else:
        e = int(input())
        S = input()
        print(RSA_PSS_Vrfy(M, n, emBits, S, e))


if __name__ == '__main__':
    main()