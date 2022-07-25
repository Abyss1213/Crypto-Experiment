def Vernam(k, s):
    res = {}
    for i in range(len(s)):
        res[i] = chr(ord(s[i]) ^ ord(k[i % len(k)]))
    return res


k = input().strip().replace('\n', '').replace('\r', '')
s = input().strip().replace('\n', '').replace('\r', '')
m = input().strip().replace('\n', '').replace('\r', '')  # 其实m没用，加解密都一样模2加
res = Vernam(k, s)
for i in res:
    print(res[i], end="")