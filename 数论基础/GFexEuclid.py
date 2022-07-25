def addorminus(a1,a2):
    add = a1 ^ a2
    res = add
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
    res = result
    return res

def divide(a1,a2):
    len1 = len(bin(a1)) - 2
    len2 = len(bin(a2)) - 2
    len0 = len1 - len2 + 1
    if len0 < 1:   # 被除数位数小于除数
        return 0
    if len0 == 1:  # 被除数位数等于除数
        return 1
    if len0 > 1:   # 被除数位数大于除数
        if a2 == 1:
            return a1
        else:
            div = 0
            while(len1 >= len2):
                a1 ^= (a2 << (len1 - len2))
                div ^= (1 << (len1 - len2))
                len1 = len(bin(a1)) - 2
            res = div
            return res
    return -1

def remainder(a1,a2,poly):
    div = divide(a1,a2)
    if div == 1:
        r = addorminus(a1,a2)
    else:
        temp = multiply(a2,div,poly)
        r = addorminus(a1,temp)
    return r

def GFexEuclid(a, b):
    if b == 0:
        return(a, 1, 0)
    else:
        g,xt,yt = GFexEuclid(b, remainder(a,b,poly))
        x = yt
        temp1 = divide(a, b)
        temp2 = multiply(yt,temp1,poly)
        y = addorminus(xt, temp2)
        return(g,x,y)

a, b = input().split()
a = int(a,16)
b = int(b,16)
poly = int('0x11b',16)
ans = GFexEuclid(a,b)
print("%02x" % ans[1],"%02x" % ans[2],"%02x" % ans[0])
