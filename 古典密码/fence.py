def fence(k, s, m):
    res = {}
    t = 0
    if m == '1':  # encode
        for i in range(k):
            for j in range(len(s)):
                if j % k == i:
                    res[t] = s[j]
                    t += 1
                else:
                    continue
    else:  # decode
        mod = len(s) % k
        l = (len(s) - mod) // k  # 分行长度
        for i in range(l):  # i是去掉余数后s能排出的列数
            for j in range(k):
                if j <= mod:
                    res[t+j] = s[i+j*l+j]
                else:
                    res[t+j] = s[i+j*l+mod]  # 一些下标运算，手动标一个例子就能明白
            t += k  # 以k为一组填充res
        for n in range(mod):
            res[t+n] = s[l*(n+1)+n]  # 把最后的i+1列填进res
    return res


k = input().strip().replace('\n', '').replace('\r', '')
s = input().strip().replace('\n', '').replace('\r', '')
m = input().strip().replace('\n', '').replace('\r', '')
res = fence(int(k), s, m)
for i in res:
    print(res[i], end="")
