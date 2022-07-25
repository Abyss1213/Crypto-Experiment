# from gmpy2 import invert
# from hashlib import sha256
# from math import ceil, log2
# h = 1
# klen = 128
# Par = 256 // 4
#
# def ECC_add(x1, y1, x2, y2, a, p):
#     if x1 == y1 == 0:
#         return x2, y2
#     if x2 == y2 == 0:
#         return x1, y1
#     if x1 == x2 and y1 == p - y2:
#         return 0, 0
#     elif x1 == x2 and y1 == y2:
#         fenzi = 3 * x1 * x1 + a
#         fenmu = 2 * y1
#         k = fenzi * invert(fenmu, p) % p
#         x3 = (k * k - x1 - x1) % p
#         y3 = (k * (x1 - x3) - y1) % p
#         return x3, y3
#     else:
#         k = ((y2 - y1) * invert((x2 - x1), p)) % p
#         x3 = (k * k - x1 - x2) % p
#         y3 = (k * (x1 - x3) - y1) % p
#         return x3, y3
#
#
# def ECC_minus(x1, y1, x2, y2, a, p):
#     y2 = p - y2
#     res = ECC_add(x1, y1, x2, y2, a, p)
#     return res[0], res[1]
#
#
# def ECC_multiply(x1, y1, a, p, k):  # 只用x1,y1
#     xr, yr = 0, 0
#     while k > 0:
#         if k & 1 == 1:
#             xr, yr = ECC_add(xr, yr, x1, y1, a, p)
#         k >>= 1
#         x1, y1 = ECC_add(x1, y1, x1, y1, a, p)
#     return xr, yr
#
#
# def ECC_division(x2, y2, a, p, k):  # 只用x2,y2
#     k = invert(k, p)
#     res = ECC_multiply(x2, y2, a, p, k)
#     return res[0], res[1]
#
#
# def KDF(Z:str, klen):
#     '''
#     :param Z: 十六进制字符串
#     :param klen: 输出密钥的比特长度
#     :return: K: 长度为klen//4的十六进制串
#     '''
#     v = 256
#     ct = '00000001'
#     K = ''
#     l = ceil(klen/v)
#     Ha = []
#     for i in range(l):
#         Hai = sha256(bytes.fromhex(Z + ct)).hexdigest()
#         Ha.append(Hai)
#         ct = '{:08x}'.format(int(ct, 16) + 1)
#     if klen % v == 0:
#         Hal = Ha[l - 1]
#     else:
#         Hal = Ha[l - 1][:(klen - v*(klen//v))//4]
#     for i in range(len(Ha)-1):
#         K += Ha[i]
#     K += Hal
#     return K
#
#
# # def A1(Gx, Gy, a, p, rA):
# #     RAx, RAy = ECC_multiply(Gx, Gy, a, p, rA)
# #     return RAx, RAy
#
#
# def B1(w, n, Gx, Gy, a, b, p, rB, dB, RAx, RAy, PAx, PAy, ZA, ZB):
#     RBx, RBy = ECC_multiply(Gx, Gy, a, p, rB)
#     X2 = 2**w + (x2 & (2**w - 1))
#     tB = (dB + X2 * rB) % n
#     if RAy != pow(RAx, 3)+a*RAx+b:
#         print("FAILED")
#     else:
#         X1 = 2 ** w + (RAx & (2 ** w - 1))
#         x_temp1, y_temp1 = ECC_multiply(RAx, RAy, a, p, X1)
#         x_temp2, y_temp2 = ECC_add(PAx, PAy, x_temp1, y_temp1, a, p)
#         xV, yV = ECC_multiply(x_temp2, y_temp2, a, p, h*tB)
#         xV = hex(xV)[2:].zfill(Par)
#         yV = hex(yV)[2:].zfill(Par)
#         # if xV == yV == 0:  # V是无穷远点？
#         #     print("FAILED")
#         # else:
#         #     KB = KDF(xV + yV + ZA + ZB, klen)
#         KB = KDF(xV + yV + ZA + ZB, klen)
#         temp1 = xV + ZA + ZB + RAx + RAy + RBx + RBy
#         temp2 = sha256(bytes.fromhex(temp1)).hexdigest()
#         SB = sha256(bytes.fromhex('0x02' + yV + temp2)).hexdigest()
#         return KB, SB
#
#
# # def A2(w, n, RAx, dA, RBx, RBy, rA, PBx, PBy, a, p, ZA, ZB, SB):
# def A2(w, n, RAx, dA, RBx, RBy, rA, PBx, PBy, a, p, ZA, ZB):
#     X1 = 2 ** w + (RAx & (2 ** w - 1))
#     tA = (dA + X1 * rA) % n
#     if RBy != pow(RBx, 3) + a * RBx + b:
#         print("FAILED")
#     else:
#         X2 = 2 ** w + (RBx & (2 ** w - 1))
#         x_temp1, y_temp1 = ECC_multiply(RBx, RBy, a, p, X2)
#         x_temp2, y_temp2 = ECC_add(PBx, PBy, x_temp1, y_temp1, a, p)
#         xU, yU = ECC_multiply(x_temp2, y_temp2, a, p, h * tA)
#         xU = hex(xU)[2:].zfill(Par)
#         yU = hex(yU)[2:].zfill(Par)
#         # if xU == yU == 0:  # U是无穷远点？
#         #     print("FAILED")
#         # else:
#         #     KA = KDF(xU + yU + ZA + ZB, klen)
#         KA = KDF(xU + yU + ZA + ZB, klen)
#         temp1 = xU + ZA + ZB + RAx + RAy + RBx + RBy
#         temp2 = sha256(bytes.fromhex(temp1)).hexdigest()
#         S1 = sha256(bytes.fromhex('0x02' + yU + temp2)).hexdigest()
#         # if S1 != SB:
#         #     print("FAILED")
#         SA = sha256(bytes.fromhex('0x03' + yU + temp2)).hexdigest()
#         return KA, S1, SA
#
#
# # def B2(xV, yV, ZA, ZB, RAx, RAy, RBx, RBy, SA):
# def B2(xV, yV, ZA, ZB, RAx, RAy, RBx, RBy):
#     temp1 = xV + ZA + ZB + RAx + RAy + RBx + RBy
#     temp2 = sha256(bytes.fromhex(temp1)).hexdigest()
#     S2 = sha256(bytes.fromhex('0x03' + yV + temp2)).hexdigest()
#     # if S2 != SA:
#     #     print("FAILED")
#     return S2
#
#
# def dec2hex(a:int):
#     a_hex = hex(a)[2:]
#     m = len(a_hex) % 4
#     if m != 0:
#         for i in range(4-m):
#             a_hex = '0' + a_hex
#     return a_hex
#
#
# Name = input().strip().replace('\n', '').replace('\r', '')
# p = int(input().strip().replace('\n', '').replace('\r', ''))
# a = int(input().strip().replace('\n', '').replace('\r', ''))
# b = int(input().strip().replace('\n', '').replace('\r', ''))
# Gx, Gy = input().split()
# n = int(input().strip().replace('\n', '').replace('\r', ''))
# IDA = input().strip().replace('\n', '').replace('\r', '')
# IDB = input().strip().replace('\n', '').replace('\r', '')
# d = int(input().strip().replace('\n', '').replace('\r', ''))
# PAx, PAy = input().split()
# PBx, PBy = input().split()
# r = int(input())
# Rx, Ry = input().split()
# Gx = int(Gx)
# Gy = int(Gy)
# PAx = int(PAx)
# PAy = int(PAy)
# PBx = int(PBx)
# PBy = int(PBy)
# Rx = int(Rx)
# Ry = int(Ry)
#
# w = ceil(ceil(log2(n))/2)-1
# entlenA = len(IDA) * 4
# entlenB = len(IDB) * 4
# ENTLA = '{:04x}'.format(entlenA)
# ENTLB = '{:04x}'.format(entlenB)
# tmpA = ENTLA + IDA + hex(a)[2:] + hex(b)[2:] + hex(Gx)[2:] + hex(Gy)[2:] + hex(PAx)[2:] + hex(PAy)[2:]
# tmpB = ENTLA + IDB + hex(a)[2:] + hex(b)[2:] + hex(Gx)[2:] + hex(Gy)[2:] + hex(PBx)[2:] + hex(PBy)[2:]
# ZA = sha256(bytes.fromhex(tmpA)).hexdigest()
# ZB = sha256(bytes.fromhex(tmpB)).hexdigest()
#
#
# if Name == 'A':
#     # RAx, RAy = A1(Gx, Gy, a, p, rA)
#     RAx, RAy = ECC_multiply(Gx, Gy, a, p, rA)
#     KA, S1, SA = A2(w, n, RAx, d, Rx, Ry, r, PBx, PBy, a, p, ZA, ZB)
#     print(KA)
#     print(S1, SA)
# else:
#     RBx, RBy = ECC_multiply(Gx, Gy, a, p, rB)
#     KB, SB = B1(w, n, Gx, Gy, a, b, p, r, d, Rx, Ry, PAx, PAy, ZA, ZB)
#     S2 = B2(xV, yV, ZA, ZB, Rx, Ry, RBx, RBy)
#     print(KB)
#     print(SB, S2)
#
# def dec2hex(a:int):
#     a_hex = hex(a)[2:]
#     m = len(a_hex) % 4
#     if m != 0:
#         for i in range(4-m):
#             a_hex = '0' + a_hex
#     return a_hex
#
# print(dec2hex(12345678934560))
p=60275702009245096385686171515219896416297121499402250955537857683885541941187
a=54492052985589574080443685629857027481671841726313362585597978545915325572248
b=45183185393608134601425506985501881231876135519103376096391853873370470098074
x = 49170271750780605002340338109423982046800493186843347705654277232249705737200
y = 6077618384723092770196272055827406523573877188367034612615140375118334770970
if y**2 % p == (pow(x,3)+a*x+b)%p:
    print('right')