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
    res = []  # 其实有问题，应该输出一个矩阵的，但是Hill加解密正好就一行。这个问题攻击代码里改
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
            res.append(temp)
    return res

# 失败的行列式算法，太复杂了
# def submatrix(A, i, j):
#     # 矩阵A第i行第j列元素的余矩阵
#     p = len(A)  # 矩阵的行数
#     q = len(A[0])  # 矩阵的列数
#     C = [[A[x][y] for y in range(q) if y != j] for x in range(p) if x != i]  # 列表推导式
#     return C
#
#
# # 求行列式
# def det(A):
#     # 按第一行展开递归求矩阵的行列式
#     p = len(A)  # 矩阵的行数
#     q = len(A[0])  # 矩阵的列数
#     if p == 1 and q == 1:
#         return A[0][0]
#     else:
#         value = 0
#         for j in range(q):
#             value += ((-1) ** (j + 2)) * A[0][j] * det(submatrix(A, 0, j))
#         return value


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
    det_a = det(a)  # 求行列式的逆，注意行列式向下取整
    det_inverse = exgcd(det_a, mod)[1]
    for i in range(n):
        for j in range(n):
            res[i][j] = (det_inverse * M[i][j]) % mod
    return res


def Hill(n, key, s, m):
    res = {}
    temp_s = [[]]
    t = 0
    if m == '1':  # encode  message * key
        key = key
    else:  # decode
        key = matrix_inverse(n, key, 26)

    while t < len(s):
        for i in range(n):
            temp_s[0].append(ord(s[t + i]) - 97)  # 把明文s按n分组
        temp_res = matrix_multiply(temp_s, key)  # 分组加密
        temp_s = [[]]
        for j in range(n):
            res[t + j] = chr(temp_res[j] % 26 + 97)  # 结果填充
        t += n
    return res


n = int(input())

key = matrix_zeros(n)
for i in range(n):
    key[i] = input().split()
for i in range(n):
    for j in range(n):
        key[i][j] = int(key[i][j])

s = input().strip().replace('\n', '').replace('\r', '')
m = input().strip().replace('\n', '').replace('\r', '')
res = Hill(n, key, s, m)
for i in res:
    print(res[i], end="")
