def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        a0 = a
        b0 = b
        a = abs(a)
        b = abs(b)
        g, xt, yt = exgcd(b, a % b)
        x = yt
        y = xt - int(a / b) * yt
        while x < 0:
            x += int(abs(b) / g)
            if a0 * b0 > 0:
                y = int((g - a * x) / b)
            else:
                y = int((g + a * x) / b)
        return g, x, y


a, b = input().split()
a = int(a)
b = int(b)
ans = exgcd(a, b)
print(ans[1], ans[2], ans[0])
