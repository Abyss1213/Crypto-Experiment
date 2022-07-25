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

a = [[2,3],[4,5]]
print(det(a))