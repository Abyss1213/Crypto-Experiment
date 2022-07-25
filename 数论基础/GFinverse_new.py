def gmul(a, poly):
    a <<= 1
    if a & 0x100 == 0x100:
        a ^= poly
    return a & 0xff


def multiply(a1, a2, poly):
    result = 0
    while a2 > 0:
        if a2 & 1:  # 如果a2最低位为1
            result ^= a1
        a1 = gmul(a1, poly)
        a2 >>= 1
    res = result
    return res


def inverse(a):
    if a == 0x00:
        return 0x00
    else:
        i = 0x01
        while i <= 0xff and i != 0x00:
            if multiply(a, i, poly) == 0x01:
                return i
            else:
                i += 1

#
# def bukeyue(a):
#     i = 0
#     j = 0
#     for i in range(0xff):
#         for j in range(0xff):
#             if multiply(i, j, poly) == a:
#                 return 0
#             else:
#                 j += 0x01
#         i += 0x01


a = input()
a = int(a, 16)
poly = int('0x11b', 16)
ans = inverse(a)
print("%02x" % ans)
