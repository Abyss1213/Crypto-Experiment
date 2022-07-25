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


# 创建n*n全0方阵
def matrix_zeros(n):
    a = []
    for i in range(n):
        a.append([])
    for x in range(n):
        for y in range(n):
            a[x].append(0)
    return a


# 矩阵转置
def trans(arr):
    arr2 = []
    # 数组的第二维维度
    for i in range(len(arr[0])):
        temp = []
        # 数组的第一维维度
        for j in range(len(arr)):
            temp.append(arr[j][i])
        arr2.append(temp)
    return arr2


# 复制方阵
def copy(n, a):
    b = matrix_zeros(n)
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][j]
    return b


# 矩阵乘法
def matrix_multiply(a, b):
    res = []
    for i in range(len(a)):
        res.append([])
    for x in range(len(a)):
        for y in range(len(b[0])):
            res[x].append(0)

    for x in range(len(a)):
        for y in range(len(b[0])):
            temp = 0
            j = 0
            for i in range(len(a[0])):
                temp += a[x][i] * b[j][y]
                if j < len(b):
                    j += 1
                else:
                    break
            res[x][y] = temp
    return res


def det(m):
    if len(m) <= 0:
        return None
    if len(m) == 1:
        return m[0][0]
    else:
        s = 0
        for i in range(len(m)):
            n = [[row[a] for a in range(len(m)) if a != i] for row in m[1:]]
            if i % 2 == 0:
                s += m[0][i] * det(n)
            else:
                s -= m[0][i] * det(n)
        return s


# 求模意义下矩阵逆
def matrix_inverse(n, a, mod):
    res = matrix_zeros(n)
    M = matrix_zeros(n)  # M为伴随矩阵
    for i in range(n):
        for j in range(n):
            b = copy(n, a)
            for x in range(n):
                b[i][x] = 0
            for y in range(n):
                b[y][j] = 0
            b[i][j] = 1
            A = det(b)  # 余子式
            if exgcd(i + j, 2)[0] == 1:
                A = -A
            M[i][j] = A * pow(-1, i + j)  # 代数余子式
    M = trans(M)
    det_a = det(a)  # 求行列式的逆
    det_inverse = exgcd(det_a, mod)[1]
    for i in range(n):
        for j in range(n):
            res[i][j] = (det_inverse * M[i][j]) % mod
    return res


def fill(n, s, c):  # 将s按顺序填充进n*n方阵,直到使行列式与26互素
    res_m = matrix_zeros(n)
    res_c = matrix_zeros(n)
    k = 0
    t = 0
    while exgcd(26, det(res_m))[0] != 1:
        for i in range(n):
            for j in range(n):
                res_m[i][j] = ord(s[k])-97
                k += 1
        t += 1
        k = t*n

    k -= n  # 对应填充c
    for i in range(n):
        for j in range(n):
            res_c[i][j] = ord(c[k])-97
            k += 1

    return res_m, res_c


def deHill(n, m, c):  # （密钥阶数，明文，密文）
    temp_m = fill(n, m, c)[0]
    temp_m = matrix_inverse(n, temp_m, 26)
    temp_c = fill(n, m, c)[1]
    key = matrix_multiply(temp_m, temp_c)
    for i in range(n):
        for j in range(n):
            key[i][j] = key[i][j] % 26
    return key


n = int(input())

m = input().strip().replace('\n', '').replace('\r', '')
c = input().strip().replace('\n', '').replace('\r', '')

res = deHill(n, m, c)
for i in range(n):
    for j in range(n):
        if j == n-1:
            print(res[i][j])
        else:
            print(res[i][j], end=' ')
