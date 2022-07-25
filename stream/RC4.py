import sys

# 对原始数据的随机化排序——打乱S表。K为密钥序列
def KSA(K: list):
    l = len(K)
    S = []
    for i in range(256):
        S.append(i)
    j = 0
    for i in range(256):
        j = (j + S[i] + K[i % l]) % 256
        S[i], S[j] = S[j], S[i]
    return S


# 随机选取数据作为密钥字节——输出密钥流
def PRGA(S: list):
    sys.stdin.read(2)
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
        ch = sys.stdin.read(2).replace('\n', '').replace('\r', '')
        if ch == '':
            break
        else:
            out = '{:02x}'.format(k ^ int(ch, 16))
            print(out, end='')


K = []
k = input().strip().replace('\n', '').replace('\r', '')
for i in range(2, len(k), 2):
    K.append(int(k[i:i+2], 16))
S = KSA(K)
print('\n0x', end='')
PRGA(S)



