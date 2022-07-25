import numpy as np

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


# 复制矩阵
def copy(n, a):
    b = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][j]
    return b


# 求模意义下矩阵逆
def matrix_inverse(n, a, mod):
    res = np.zeros((n, n), dtype=int)
    M = np.zeros((n, n), dtype=int)  # M为伴随矩阵
    for i in range(n):
        for j in range(n):
            b = copy(n, a)
            for x in range(n):
                b[i][x] = 0
            for y in range(n):
                b[y][j] = 0
            b[i][j] = 1
            A = round(np.linalg.det(b))  # 余子式
            if exgcd(i+j, 2)[0] == 1:
                A = -A
            M[i][j] = A * pow(-1, i+j)  # 代数余子式
    M = M.T
    det_a = round(np.linalg.det(a))  # 求行列式的逆，注意行列式向下取整
    det_inverse = exgcd(det_a, mod)[1]
    for i in range(n):
        for j in range(n):
            res[i][j] = (det_inverse * M[i][j]) % mod
    return res


def Hill(n, key, s, m):
    res = {}
    temp_s = np.zeros(n, dtype=int)
    t = 0
    if m == '1':  # encode  message * key
        key = key
    else:  # decode
        key = matrix_inverse(n, key, 26)

    while t < len(s):
        for i in range(n):
            temp_s[i] = ord(s[t+i]) - 97  # 把明文s按n分组
        temp_res = temp_s.dot(key)  # 分组加密
        for j in range(n):
            res[t+j] = chr(temp_res[j] % 26 + 97)  # 结果填充
        t += n
    return res


n = int(input().strip().replace('\n', '').replace('\r', ''))
key = np.zeros((n, n), dtype=int)
for i in range(n):
    key[i] = input().split()
s = input().strip().replace('\n', '').replace('\r', '')
m = input().strip().replace('\n', '').replace('\r', '')
res = Hill(n, key, s, m)
for i in res:
    print(res[i], end="")