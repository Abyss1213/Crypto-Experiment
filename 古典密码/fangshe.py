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


def fangshe(k, b, x, m):
    output = {}  # 在此不能定义为空列表[]，不然会报错
    k_inverse = exgcd(k, 26)[1]
    if m == '1':  # encode
        for i in range(len(x)):
            output[i] = chr(((ord(x[i]) - 97) * k + b) % 26 + 97)
    else:  # decode
        for j in range(len(x)):
            output[j] = chr(((ord(x[j]) - 97) - b) * k_inverse % 26 + 97)
    return output


k, b = input().split()
k = int(k)
b = int(b)
x = input().strip().replace('\n', '').replace('\r', '')
m = input().strip().replace('\n', '').replace('\r', '')
if exgcd(k, 26)[0] != 1:
    print("invalid key")
else:
    res = fangshe(k, b, x, m)
    for i in res:
        print(res[i], end="")