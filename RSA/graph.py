from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from pycallgraph2 import Config
from pycallgraph2 import GlobbingFilter
from gmpy2 import *
import random
from hashlib import sha256
import sys
from math import *
def main():
    h = 1
    klen = 128
    Par = 256 // 4

    def ECC_add(x1, y1, x2, y2, a, p):
        if x1 == y1 == 0:
            return x2, y2
        if x2 == y2 == 0:
            return x1, y1
        if x1 == x2 and y1 == p - y2:
            return 0, 0
        elif x1 == x2 and y1 == y2:
            fenzi = 3 * x1 * x1 + a
            fenmu = 2 * y1
            k = fenzi * invert(fenmu, p) % p
            x3 = (k * k - x1 - x1) % p
            y3 = (k * (x1 - x3) - y1) % p
            return x3, y3
        else:
            k = ((y2 - y1) * invert((x2 - x1), p)) % p
            x3 = (k * k - x1 - x2) % p
            y3 = (k * (x1 - x3) - y1) % p
            return x3, y3

    def ECC_minus(x1, y1, x2, y2, a, p):
        y2 = p - y2
        res = ECC_add(x1, y1, x2, y2, a, p)
        return res[0], res[1]

    def ECC_multiply(x1, y1, a, p, k):  # 只用x1,y1
        xr, yr = 0, 0
        while k > 0:
            if k & 1 == 1:
                xr, yr = ECC_add(xr, yr, x1, y1, a, p)
            k >>= 1
            x1, y1 = ECC_add(x1, y1, x1, y1, a, p)
        return xr, yr

    def ECC_division(x2, y2, a, p, k):  # 只用x2,y2
        k = invert(k, p)
        res = ECC_multiply(x2, y2, a, p, k)
        return res[0], res[1]

    def KDF(Z: str, klen):
        '''
        :param Z: 十六进制字符串
        :param klen: 输出密钥的比特长度
        :return: K: 长度为klen//4的十六进制串
        '''
        v = 256
        ct = '00000001'
        K = ''
        l = ceil(klen / v)
        Ha = []
        for i in range(l):
            Hai = sha256(bytes.fromhex(Z + ct)).hexdigest()
            Ha.append(Hai)
            ct = '{:08x}'.format(int(ct, 16) + 1)
        if klen % v == 0:
            Hal = Ha[l - 1]
        else:
            Hal = Ha[l - 1][:(klen - v * (klen // v)) // 4]
        for i in range(len(Ha) - 1):
            K += Ha[i]
        K += Hal
        return K

    def dec2hex(a: int):
        a_hex = hex(a)[2:]
        m = len(a_hex) % 4
        if m != 0:
            for i in range(4 - m):
                a_hex = '0' + a_hex
        return a_hex

    def A_get_RA(Gx, Gy, a, p, rA):
        RAx, RAy = ECC_multiply(Gx, Gy, a, p, rA)
        return RAx, RAy

    def B_get_RB_SB_KB(w, n, Gx, Gy, a, b, p, rB, dB, RAx, RAy, PAx, PAy, ZA, ZB):
        RBx, RBy = ECC_multiply(Gx, Gy, a, p, rB)
        X2 = (2 ** w + (RBx & (2 ** w - 1))) % p
        tB = (dB + X2 * rB) % n
        X1 = (2 ** w + (RAx & (2 ** w - 1))) % p
        x_temp1, y_temp1 = ECC_multiply(RAx, RAy, a, p, X1)
        x_temp2, y_temp2 = ECC_add(PAx, PAy, x_temp1, y_temp1, a, p)
        xV, yV = ECC_multiply(x_temp2, y_temp2, a, p, h * tB)
        xV = hex(xV)[2:].zfill(Par)
        yV = hex(yV)[2:].zfill(Par)
        KB = KDF(xV + yV + ZA + ZB, klen)
        RAx = dec2hex(RAx)
        RAy = dec2hex(RAy)
        RBx = dec2hex(RBx)
        RBy = dec2hex(RBy)
        temp1 = xV + ZA + ZB + RAx + RAy + RBx + RBy
        temp2 = sha256(bytes.fromhex(temp1)).hexdigest()
        SB = sha256(bytes.fromhex('02' + yV + temp2)).hexdigest()
        return KB, SB, xV, yV

    def A_get_KA_SA(w, n, RAx, RAy, dA, RBx, RBy, rA, PBx, PBy, a, p, ZA, ZB):
        X1 = (2 ** w + (RAx & (2 ** w - 1))) % p
        tA = (dA + X1 * rA) % n
        X2 = (2 ** w + (RBx & (2 ** w - 1))) % p
        x_temp1, y_temp1 = ECC_multiply(RBx, RBy, a, p, X2)
        x_temp2, y_temp2 = ECC_add(PBx, PBy, x_temp1, y_temp1, a, p)
        xU, yU = ECC_multiply(x_temp2, y_temp2, a, p, h * tA)
        xU = hex(xU)[2:].zfill(Par)
        yU = hex(yU)[2:].zfill(Par)
        KA = KDF(xU + yU + ZA + ZB, klen)
        RAx = dec2hex(RAx)
        RAy = dec2hex(RAy)
        RBx = dec2hex(RBx)
        RBy = dec2hex(RBy)
        temp1 = xU + ZA + ZB + RAx + RAy + RBx + RBy
        temp2 = sha256(bytes.fromhex(temp1)).hexdigest()
        S1 = sha256(bytes.fromhex('02' + yU + temp2)).hexdigest()
        SA = sha256(bytes.fromhex('03' + yU + temp2)).hexdigest()
        return KA, S1, SA

    def B_get_S2(xV, yV, ZA, ZB, RAx, RAy, RBx, RBy):
        RAx = dec2hex(RAx)
        RAy = dec2hex(RAy)
        RBx = dec2hex(RBx)
        RBy = dec2hex(RBy)
        temp1 = xV + ZA + ZB + RAx + RAy + RBx + RBy
        temp2 = sha256(bytes.fromhex(temp1)).hexdigest()
        S2 = sha256(bytes.fromhex('03' + yV + temp2)).hexdigest()
        return S2

    Name = input().strip().replace('\n', '').replace('\r', '')
    p = int(input().strip().replace('\n', '').replace('\r', ''))
    a = int(input().strip().replace('\n', '').replace('\r', ''))
    b = int(input().strip().replace('\n', '').replace('\r', ''))
    Gx, Gy = input().split()
    n = int(input().strip().replace('\n', '').replace('\r', ''))
    IDA = input().strip().replace('\n', '').replace('\r', '')
    IDB = input().strip().replace('\n', '').replace('\r', '')
    d = int(input().strip().replace('\n', '').replace('\r', ''))
    PAx, PAy = input().split()
    PBx, PBy = input().split()
    r = int(input())
    Rx, Ry = input().split()
    Gx = int(Gx)
    Gy = int(Gy)
    PAx = int(PAx)
    PAy = int(PAy)
    PBx = int(PBx)
    PBy = int(PBy)
    Rx = int(Rx)
    Ry = int(Ry)

    w = ceil(ceil(log2(n)) / 2) - 1
    entlenA = len(IDA) * 4
    entlenB = len(IDB) * 4
    ENTLA = '{:04x}'.format(entlenA)
    ENTLB = '{:04x}'.format(entlenB)
    tmpA = ENTLA + IDA + dec2hex(a) + dec2hex(b) + dec2hex(Gx) + dec2hex(Gy) + dec2hex(PAx) + dec2hex(PAy)
    tmpB = ENTLB + IDB + dec2hex(a) + dec2hex(b) + dec2hex(Gx) + dec2hex(Gy) + dec2hex(PBx) + dec2hex(PBy)
    ZA = sha256(bytes.fromhex(tmpA)).hexdigest()
    ZB = sha256(bytes.fromhex(tmpB)).hexdigest()

    if Name == 'A':
        RAx, RAy = A_get_RA(Gx, Gy, a, p, r)
        KA, S1, SA = A_get_KA_SA(w, n, RAx, RAy, d, Rx, Ry, r, PBx, PBy, a, p, ZA, ZB)
        print(int(KA, 16))
        print(int(S1, 16), int(SA, 16))
    else:
        RBx, RBy = ECC_multiply(Gx, Gy, a, p, r)
        KB, SB, xV, yV = B_get_RB_SB_KB(w, n, Gx, Gy, a, b, p, r, d, Rx, Ry, PAx, PAy, ZA, ZB)
        S2 = B_get_S2(xV, yV, ZA, ZB, Rx, Ry, RBx, RBy)
        print(int(KB, 16))
        print(int(SB, 16), int(S2, 16))


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
        'ECC_add',
        'ECC_minus',
        'ECC_multiply',
        'KDF',
        'dec2hex',
        'A_get_RA',
        'B_get_RB_SB_KB'
        'A_get_KA_SA',
        'B_get_S2'
    ])
    # 该段作用是关系图中不包括(exclude)哪些函数。(正则表达式规则)
    # config.trace_filter = GlobbingFilter(exclude=[
    #     'pycallgraph.*',
    #     '*.secret_function',
    #     'FileFinder.*',
    #     'ModuleLockManager.*',
    #     'SourceFilLoader.*'
    # ])
    graphviz = GraphvizOutput()
    graphviz.output_file = 'SM2_CHANGE.png'
    with PyCallGraph(output=graphviz, config=config):
        main()

