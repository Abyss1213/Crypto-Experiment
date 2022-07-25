def single_table(l1, l2, x, m):
    res = {}
    if m == '1':  # encode
        for i in range(len(x)):
            for j in range(26):
                if l1[j] == x[i]:
                    res[i] = l2[j]
                else:
                    continue
    else:  # decode
        for i in range(len(x)):
            for j in range(26):
                if l2[j] == x[i]:
                    res[i] = l1[j]
                else:
                    continue
    return res


l1 = input()
l2 = input()
x = input()
m = input()
res = single_table(l1, l2, x, m)
for i in res:
    print(res[i], end="")