from hashlib import sha1
import sys
Hlen = 20

def OS2IP(X):  # hexstr to int
    x = []
    for i in range(0, len(X), 2):
        x.append(int(X[i:i+2], 16))

    res = 0
    xLen = len(x)
    for i in range(xLen):
        res += x[i] * pow(256, xLen - (i + 1))

    return res


def I2OSP(x, xLen):  # int to hexstr
    if x >= pow(256, xLen):
        print('Ree')
        sys.exit()
    digits = []

    while x:
        digits.append(int(x % 256))
        x //= 256
    # print(len(digits), digits)
    for i in range(xLen - len(digits)):
        digits.append(0)
    x_int = digits[::-1]

    res = ''
    for i in range(len(x_int)):
        res += '{:02x}'.format(x_int[i], 16)
    return res


def RSAEP(n, e, m):
    if m < 0 or m > n - 1:
        print('Err')
        sys.exit()
    c = pow(m, e, n)
    return c


def RSADP(n, e, c):
    if c < 0 or c > n - 1:
        print('Ree')
        sys.exit()
    m = pow(c, e, n)
    return m


def MGF(x, maskLen):  # x是去掉0x的十六进制串
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


def OAEP_Encoding(k, M, L, seed, n, e):
    Mlen = len(M[2:]) // 2
    Llen = len(L[2:]) // 2
    if Llen > pow(2, 61) - 1 or Mlen > k - 2 * Hlen - 2:
        print('Err')
        sys.exit()

    # lHash = sha1(L[2:].encode('utf-8')).hexdigest()  # 将输入当做字符串处理
    lHash = sha1(bytes.fromhex(L[2:])).hexdigest()  # 将输入当做十六进制处理

    PS = ''
    PSlen = k - Mlen - 2 * Hlen - 2
    for i in range(2 * PSlen):  # 十六进制字符串
        PS += '0'

    DB = lHash + PS + '01' + M[2:]
    # print(DB)

    dbMask = MGF(seed, k - Hlen - 1)
    maskedDB = hex(int(DB, 16) ^ int(dbMask, 16))[2:].zfill(len(DB))
    # print(maskedDB)

    seedMask = MGF(maskedDB, Hlen)
    maskedSeed = hex(int(seed, 16) ^ int(seedMask, 16))[2:].zfill(len(seed))
    # print(maskedSeed)

    EM = '00' + maskedSeed + maskedDB
    # print(EM)

    m = OS2IP(EM)
    c = RSAEP(n, e, m)
    C = I2OSP(c, k)

    return C


def OAEP_Decodeing(k, C, L, n, e):
    Clen = len(C[2:]) // 2
    Llen = len(L[2:]) // 2
    if Llen > pow(2, 61) - 1 or Clen != k or k < 2 * Hlen + 2:
        print('Ree')
        sys.exit()

    c = OS2IP(C[2:])
    # if c >= n:
    #     print('Ree')
    #     sys.exit()

    m = RSADP(n, e, c)

    EM = I2OSP(m, k)

    Y = int(EM[0:2], 16)
    if Y != 0:
        print('Ree')
        sys.exit()

    lHash = sha1(bytes.fromhex(L[2:])).hexdigest()

    maskedSeed = EM[2:2+Hlen*2]
    maskedDB = EM[-2 * (k - Hlen - 1):]

    seedMask = MGF(maskedDB, Hlen)
    seed = hex(int(maskedSeed, 16) ^ int(seedMask, 16))[2:].zfill(len(maskedSeed))

    dbMask = MGF(seed, k - Hlen - 1)
    DB = hex(int(maskedDB, 16) ^ int(dbMask, 16))[2:].zfill(len(maskedDB))
    # print(len(DB), DB)

    lHash2 = DB[0:Hlen*2]

    if lHash != lHash2:
        print('Ree')
        sys.exit()

    t = 0
    for i in range(2 * Hlen, len(DB), 2):
        if DB[i:i + 2] == '00':
            continue
        else:
            t = i + 2
            flag = DB[i:i + 2]
            # print(flag)
            if flag != '01':
                print('Ree')
                sys.exit()
            break

    if DB[t] == '0':
        t += 1
    M = DB[t:]
    return M


def main():
    op = int(input().strip().replace('\n', '').replace('\r', ''))
    k = int(input().strip().replace('\n', '').replace('\r', ''))
    e = int(input().strip().replace('\n', '').replace('\r', ''), 16)
    n = int(input().strip().replace('\n', '').replace('\r', ''), 16)
    s = input().strip().replace('\n', '').replace('\r', '')
    L = input().strip().replace('\n', '').replace('\r', '')

    if op == 1:
        seed = input().strip().replace('\n', '').replace('\r', '')[2:]
        res = OAEP_Encoding(k, s, L, seed, n, e)
        b = 2 * k - len(res)
        for i in range(b):
            res = '0' + res
        print('0x' + res)
    else:
        res = OAEP_Decodeing(k, s, L, n, e)
        print('0x' + res)


if __name__ == '__main__':
    main()