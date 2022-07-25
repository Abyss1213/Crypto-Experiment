def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        a0 = a
        b0 = b
        a = abs(a)  # 用绝对值辗转相除
        b = abs(b)
        g, xt, yt = exgcd(b, a % b)
        x = yt
        y = xt - a // b * yt
        if a0 < 0:  # 经试验，a0<0,b0<0 和 a0<0,b0>0结果绝对值一样
            x = -x
            y = -y
        while x < 0:
            x += b // g  # 使x是最小正整数
            y = (g - a * x) // b
        if a0 * b0 > 0:
            return g, x, y
        else:
            return g, x, -y


a, b = input().split()
a = int(a)
b = int(b)
ans = exgcd(a, b)
print(ans[1], ans[2], ans[0])
