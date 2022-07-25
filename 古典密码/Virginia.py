def line(sym):  # 生成Virginia表的一行
    res = {}
    add = ord(sym)-97
    for i in range(26):
        res[i] = chr((i+add) % 26 + 97)
    return res


def Virginia(k, s, m):
    res = {}
    if m == '1':  # encode
        for i in range(len(s)):
            table = line(k[i % len(k)])
            t = ord(s[i]) - 97  # 明文字母对应下标
            res[i] = table[t]
    else:
        for i in range(len(s)):
            table = line(k[i % len(k)])
            for j in range(26):
                if table[j] == s[i]:
                    res[i] = chr(j + 97)
    return res


k = input().strip().replace('\n', '').replace('\r', '')
s = input().strip().replace('\n', '').replace('\r', '')
m = input().strip().replace('\n', '').replace('\r', '')
res = Virginia(k, s, m)
for i in res:
    print(res[i], end="")

