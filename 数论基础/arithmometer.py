def addorminus(a1,a2):
    add = a1 ^ a2
    res = "%02x" % add
    return res

def gmul(a,poly):
    a <<= 1
    if a & 0x100 == 0x100:
        a ^= poly
    return a & 0xff
def multiply(a1,a2,poly):
    result = 0
    while(a2 > 0):
        if a2 & 1:  # 如果a2最低位为1
            result ^= a1
        a1 = gmul(a1,poly)
        a2 >>= 1
    res = "%02x" % result
    return res

def divide(a1,a2):
    len1 = len(bin(a1)) - 2
    len2 = len(bin(a2)) - 2
    len0 = len1 - len2 + 1
    if len0 < 1:   # 被除数位数小于除数
        return "%02x" % 0
    if len0 == 1:  # 被除数位数等于除数
        return "%02x" % 1
    if len0 > 1:   # 被除数位数大于除数
        div = 0
        while(len1 >= len2):
            a1 ^= (a2 << (len1 - len2))
            div ^= (1 << (len1 - len2))
            len1 = len(bin(a1)) - 2
        res = "%02x" % div
        return res
    return -1

def remainder(a1,a2):
    div = divide(a1,a2)
    if div == 1:
        r = addorminus(a1,a2)
    else:
        temp = multiply(a2,int(div,16),poly)
        r = addorminus(a1,int(temp,16))
    return r

a1, sym, a2 = input().split()
a1 = int(a1,16)
a2 = int(a2,16)
poly = int('0x11b',16)  # 不可约多项式为x^8+x^4+x^3+x+1

if sym == '+':
    print(addorminus(a1,a2))
if sym == '-':
    print(addorminus(a1,a2))
if sym == '*':
    print(multiply(a1,a2,poly))
if sym == '/':
    print(divide(a1,a2),remainder(a1,a2))
