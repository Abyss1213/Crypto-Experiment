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

def Matrix(n, k, s, m):
    res = []
    t = 0
    p = len(s) // n
    if m == '1':  # encode
        temp1 = []
        for i in range(p):
            temp1.append([])
        for i in range(p):  # 明文分组
            for j in range(n):
                temp1[i].append(s[t+j])
            t += n

        for x in range(n):
            for y in range(n):
                if ord(k[y])-48 == x+1:
                    for z in range(p):
                        res.append(temp1[z][y])
                    break
                else:
                    continue

    else:  # decode
        temp2 = []  # temp2存密文分组
        for i in range(n):
            temp2.append([])
        temp3 = []  # temp3调换temp2顺序
        for i in range(n):  # 密文分组
            for j in range(p):
                temp2[i].append(s[t+j])
            t += p

        for x in range(n):
            temp3.append(temp2[ord(k[x])-48-1])
        temp3 = trans(temp3)
        for i in range(p):
            for j in range(n):
                res.append(temp3[i][j])

    return res


n = int(input())
k = input().strip().replace('\n', '').replace('\r', '')
s = input().strip().replace('\n', '').replace('\r', '')
m = input().strip().replace('\n', '').replace('\r', '')

res = Matrix(n, k, s, m)
for i in res:
    print(i, end="")