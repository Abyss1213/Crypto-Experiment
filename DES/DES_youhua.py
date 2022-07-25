IP_Substitution = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
                   62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
                   57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
                   61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

IP_Inverse_Substitution = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
                           38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
                           36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
                           34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

Key_Substitution_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
                      10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
                      63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
                      14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]  # 已经去掉校验位了

Key_Substitution_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
                      23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
                      41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
                      44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

Key_Extension = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
                 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

Key_Left_Shift_Scheduling = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PBox = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

SBox1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
         0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
         4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
         15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]

SBox2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
         3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
         0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
         13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]

SBox3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
         13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
         13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
         1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]

SBox4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
         13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
         10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
         3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]

SBox5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
         14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
         4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
         11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]

SBox6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
         10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
         9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
         4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]

SBox7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
         13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
         1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
         6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]

SBox8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
         1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
         7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
         2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]


def ip(bin_str):
    res = []
    for i in IP_Substitution:
        res.append(int(bin_str[i-1]))
    return res


def re_ip(bin_str):
    res = []
    for i in IP_Inverse_Substitution:
        res.append(int(bin_str[i-1]))
    return res


def left_move(key, i):
    res = key[i:] + key[0:i]
    return res


def PC1(key):
    # 压缩置换1
    trans = []
    for i in Key_Substitution_1:
        trans.append(key[i-1])
    return trans


def get_keys(bin_key):
    # 密钥分组
    left_key0 = bin_key[0:28]
    right_key0 = bin_key[28:]

    # 循环左移
    keys = []
    left_next = left_key0
    right_next = right_key0
    for i in range(16):
        left_next = left_move(left_next, Key_Left_Shift_Scheduling[i])
        right_next = left_move(right_next, Key_Left_Shift_Scheduling[i])
        keys.append(left_next + right_next)

    # 压缩置换2
    res = []
    key_i = []
    for i in range(16):
        for j in Key_Substitution_2:
            key_i.append(keys[i][j-1])
        res.append(key_i)
        key_i = []

    return res


def oneturn(Li_32, Ri_32, x, keys):
    # 扩展置换E
    Ri_48 = []
    for i in Key_Extension:
        Ri_48.append(Ri_32[i-1])
    # print('E-Ri_48:', hexy(Ri_48))
    # 异或
    temp = []
    for i in range(48):
        temp.append(Ri_48[i] ^ int(keys[x][i], 2))   # 此时temp是整型数组
    # print('xor-temp:', hexy(temp))
    # SBox
    SBox = [SBox1, SBox2, SBox3, SBox4, SBox5, SBox6, SBox7, SBox8]
    out = []
    for i in range(8):
        line = temp[6*i]*2 + temp[6*i+5]*1
        row = temp[6*i+1]*8 + temp[6*i+2]*4 + temp[6*i+3]*2 + temp[6*i+4]*1
        out_i = bin(SBox[i][16*line+row])
        out_i = int(out_i, 2)
        out_i_str = '{:04b}'.format(out_i)
        out.append(out_i_str)
    out_32 = ''
    for i in range(8):
        out_32 = out_32 + out[i]
    # print('SBox-out_32:', hexy(out_32))
    # P置换
    P_res = []
    for i in PBox:
        P_res.append(int(out_32[i-1]))
    # print('PBox-P_res:', hexy(P_res))
    # 异或交换
    R_next = []
    for i in range(32):
        R_next.append(Li_32[i] ^ P_res[i])
    L_next = Ri_32

    return L_next, R_next  # 皆为整型数组


def hexy(s):
    res = ''.join(list(map(str, s)))  # list转str
    res = int(hex(int(res, 2)), 16)  # 以十六进制输出
    res = '{:016x}'.format(res)  # 补齐16位
    res = '0x' + res
    return res


def DES(s_bin, key_bin, m):
        s_ip = ip(s_bin)
        # print('s_ip:', hexy(s_ip))

        key_bin = PC1(key_bin)  # PC1只要最开始用一次
        keys = get_keys(key_bin)

        L = s_ip[0:32]
        R = s_ip[32:]

        for x in range(16):
            # print('turn:', x)
            if m == '1':  # encode
                temp = oneturn(L, R, x, keys)
            else:
                temp = oneturn(L, R, 15 - x, keys)
            L = temp[0]
            R = temp[1]  # 此处不用temp代替就会运行两遍oneturn函数


        # IP逆运算
        res16 = R + L
        res = []
        for i in IP_Inverse_Substitution:
            res.append(res16[i-1])

        return hexy(res)


def DESs(T, s_bin, key_bin, m):
    temp = DES(s_bin, key_bin, m)
    temp_bin = int(bin(int(temp, 16)).replace('0b', ''), 2)
    temp_bin = '{:064b}'.format(temp_bin)  # 需要补齐64位
    for i in range(T-1):
        temp = DES(temp_bin, key_bin, m)
        temp_bin =int(bin(int(temp, 16)).replace('0b', ''), 2)
        temp_bin = '{:064b}'.format(temp_bin)
    return temp

T = input().strip().replace('\n', '').replace('\r', '')
T = int(T)
s = input().strip().replace('\n', '').replace('\r', '')
key = input().strip().replace('\n', '').replace('\r', '')
s_bin = int(bin(int(s, 16)).replace('0b', ''), 2)
key_bin = int(bin(int(key, 16)).replace('0b', ''), 2)
s_bin = '{:064b}'.format(s_bin)
key_bin = '{:064b}'.format(key_bin)

res = DESs(T, s_bin, key_bin, '1')
print(res)
