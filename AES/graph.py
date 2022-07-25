from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from pycallgraph2 import Config
from pycallgraph2 import GlobbingFilter

SBox = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

inSBox = [[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
          [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
          [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
          [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
          [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
          [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
          [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
          [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
          [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
          [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
          [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
          [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
          [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
          [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
          [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
          [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]

Rcon = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000,
        0x20000000, 0x40000000, 0x80000000, 0x1b000000, 0x36000000]

RowMix = [[0x02, 0x03, 0x01, 0x01],
          [0x01, 0x02, 0x03, 0x01],
          [0x01, 0x01, 0x02, 0x03],
          [0x03, 0x01, 0x01, 0x02]]

reRowMix = [[0x0e, 0x0b, 0x0d, 0x09],
            [0x09, 0x0e, 0x0b, 0x0d],
            [0x0d, 0x09, 0x0e, 0x0b],
            [0x0b, 0x0d, 0x09, 0x0e]]

def main():
    def addorminus(a1, a2):
        add = a1 ^ a2
        # res = "%02x" % add
        return add

    def gmul(a, poly):
        a <<= 1
        if a & 0x100 == 0x100:
            a ^= poly
        return a & 0xff

    def multiply(a1, a2, poly):
        result = 0
        while a2 > 0:
            if a2 & 1:  # 如果a2最低位为1
                result ^= a1
            a1 = gmul(a1, poly)
            a2 >>= 1
        res = result
        return res

    def G28_matrix_multiply(a, b, poly):
        res = []
        for i in range(4):
            res.append([])
        for x in range(4):
            for y in range(4):
                res[x].append(0)

        for x in range(4):
            for y in range(4):
                temp = 0
                j = 0
                for i in range(4):
                    temp = addorminus(multiply(a[x][i], b[j][y], poly), temp)
                    if j < len(b):
                        j += 1
                    else:
                        break
                res[x][y] = temp
        return res

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

    def hex2bytes(s, Nk):
        if Nk == 4:
            s = '{:032x}'.format(int(s, 16))
        if Nk == 6:
            s = '{:048x}'.format(int(s, 16))
        if Nk == 8:
            s = '{:064x}'.format(int(s, 16))
        s = bytes().fromhex(s)  # fromhex里的参数必须是去掉0x的偶数位十六进制字符串
        return s

    def hex2state(s, Nk):  # 用于将十六进制字符串变成状态矩阵的形式
        w = []
        s = hex2bytes(s, Nk)
        for i in range(Nk):
            w.append([])
        for i in range(Nk):
            for j in range(4):
                w[i].append(s[4 * i + j])
        return w

    def state2hex(state):
        res = '0x'
        for i in range(4):
            for j in range(4):
                res += '{:02x}'.format(int(hex(state[i][j]), 16))
        return res

    def strlist2hex(l):  # 输入['d6', 'e0', '0d', '8b']，输出3605007755
        res = '0x'
        for i in l:
            res += i
        res = int(res, 16)
        return res

    def intlist2hex(l):  # 输入[247, 218, 208, 56]，输出4158312504
        temp = []
        for i in l:
            temp.append('{:02x}'.format(int(hex(i), 16)))
        res = strlist2hex(temp)
        return res

    def int2list(a):  # 输入4158312504，输出[247, 218, 208, 56]
        res = []
        temp = '{:08x}'.format(int(hex(a), 16))
        for i in range(4):
            res.append(int(temp[2 * i:2 * i + 2], 16))
        return res

    def SubWord(l):  # 接受一个4bytes字列表，对每个字节做S盒变换。输入示例：[247, 218, 208, 56]
        res = []
        for i in range(4):
            temp = '{:08b}'.format(int(bin(l[i]), 2))
            L = int(temp[0:4], 2)
            R = int(temp[4:], 2)
            res.append('{:02x}'.format(int(hex(SBox[L][R]), 16)))
        return res

    def inSubWord(l):  # 接受一个4bytes字列表，对每个字节做S盒变换。输入示例：[247, 218, 208, 56]
        res = []
        for i in range(4):
            temp = '{:08b}'.format(int(bin(l[i]), 2))
            L = int(temp[0:4], 2)
            R = int(temp[4:], 2)
            res.append('{:02x}'.format(int(hex(inSBox[L][R]), 16)))
        return res

    def RotWord(l):  # 循环移位，接受[a0,a1,a2,a3],返回[a1,a2,a3,a0]
        res = []
        res.append(l[1])
        res.append(l[2])
        res.append(l[3])
        res.append(l[0])
        return res

    def Print(s):  # 将[247, 218, 208, 56]打印成十六进制字符串
        res = '0x'
        for i in range(4):
            res += '{:02x}'.format(int(hex(s[i]), 16))
        print(res, end=' ')
        # return res

    def Printplus(state):  # 将状态矩阵按列变十六进制打印
        for i in range(4):
            Print(state[i])
        print('...............')

    def KeyExpansion(key, Nb, Nr, Nk):  # Nb分组大小 Nr轮数 Nk密钥长度
        w = hex2state(key,
                      Nk)  # 此时结果示例：w = [[247, 218, 208, 56], [251, 61, 192, 171], [88, 187, 153, 135], [206, 74, 160, 243]]
        i = Nk
        while i < Nb * (Nr + 1):
            temp = w[i - 1]
            if i % Nk == 0:
                temp = strlist2hex(SubWord(RotWord(temp))) ^ Rcon[(i // Nk) - 1]  # 此处为按位异或?
                temp = int2list(temp)
            if Nk > 6 and i % Nk == 4:
                temp = SubWord(temp)
                temp = int2list(strlist2hex(temp))
            wi = intlist2hex(w[i - Nk]) ^ intlist2hex(temp)
            w.append(int2list(wi))
            i += 1
        return w  # 目前输出十进制数组版密钥

    def ByteSub(state):
        res = []
        for i in range(4):
            res.append(SubWord(state[i]))
        # print('ByteSub:', res)
        return res  # 输出字符型二维数组

    def inByteSub(state):
        res = []
        for i in range(4):
            res.append(inSubWord(state[i]))
        # print('ByteSub:', res)
        return res  # 输出字符型二维数组

    def ShiftRow(state):  # 为了方便后面的列混淆，在行变换时将以列为一维数组改成以行为一维数组
        temp = []
        for i in range(4):
            for j in range(4):
                temp.append(state[i][j])
        res = []
        for i in range(4):
            res.append([])
        for i in range(4):
            for j in range(4):
                res[i].append(temp[(5 * i + 4 * j) % 16])
        # print('ShiftRow:', res)
        return res  # 输出字符型二维数组

    def inShiftRow(state):  # 为了方便后面的列混淆，在行变换时将以列为一维数组改成以行为一维数组
        temp = []
        for i in range(4):
            for j in range(4):
                temp.append(state[i][j])
        res = []
        for i in range(4):
            res.append([])
        for i in range(4):
            for j in range(4):
                res[i].append(temp[(13 * i + 4 * j) % 16])
        # print('ShiftRow:', end=' ')
        # Printplus(res)
        return res  # 输出字符型二维数组

    def MixColumns(state):
        poly = int('0x11b', 16)
        res = G28_matrix_multiply(RowMix, state, poly)
        res = trans(res)  # 需要转置一下
        # print('MixColumns:', end=' ')
        # Printplus(res)
        return res

    def inMixColumns(state):
        poly = int('0x11b', 16)
        res = G28_matrix_multiply(reRowMix, state, poly)
        res = trans(res)  # 需要转置一下
        # print('MixColumns:', end=' ')
        # Printplus(res)
        return res

    def AddRoundKey(state, keys, x):  # 输入状态矩阵，所有轮密钥，轮数
        res = []
        for i in range(4):
            res.append([])
        for i in range(4):
            for j in range(4):
                res[i].append(state[i][j] ^ keys[4 * x + i][j])
        return res  # 十进制数组

    def Round(state, x):
        state = ByteSub(state)
        state = ShiftRow(state)
        temp = []
        for i in range(4):
            temp.append(int2list(strlist2hex(state[i])))
        state = MixColumns(temp)
        state = AddRoundKey(state, keys, x)
        return state

    def inRound(state, x, Nr):
        state = inShiftRow(state)
        state = inByteSub(state)
        state = trans(state)
        temp = []
        for i in range(4):
            temp.append(int2list(strlist2hex(state[i])))
        state = AddRoundKey(temp, keys, Nr - x)
        state = trans(state)
        state = inMixColumns(state)
        return state

    def AES_encode(m, keys, Nr):
        state = AddRoundKey(m, keys, 0)
        # Printplus(state)
        for x in range(1, Nr):
            state = Round(state, x)
        # round 10
        state = ByteSub(state)
        state = ShiftRow(state)
        state = trans(state)
        temp = []
        for i in range(4):
            temp.append(int2list(strlist2hex(state[i])))
        state = AddRoundKey(temp, keys, Nr)
        return state

    def AES_decode(c, keys, Nr):
        state = AddRoundKey(c, keys, Nr)
        # Printplus(state)
        for x in range(1, Nr):
            state = inRound(state, x, Nr)
        # round 10
        state = inShiftRow(state)
        state = inByteSub(state)
        state = trans(state)
        temp = []
        for i in range(4):
            temp.append(int2list(strlist2hex(state[i])))
        state = AddRoundKey(temp, keys, 0)
        return state

    def multi_AES(T, s, keys, Nr, mode):
        if mode == '1':
            temp = AES_encode(s, keys, Nr)
            for i in range(T - 1):
                temp = AES_encode(temp, keys, Nr)
        else:
            temp = AES_decode(s, keys, Nr)
            for i in range(T - 1):
                temp = AES_decode(temp, keys, Nr)
        res = state2hex(temp)
        return res

    l = int(input())
    T = int(input())
    s = input().strip().replace('\n', '').replace('\r', '')
    k = input().strip().replace('\n', '').replace('\r', '')
    m = input()
    s = hex2state(s, 4)
    if l == 192:
        Nr = 12
        Nk = 6
    if l == 256:
        Nr = 14
        Nk = 8
    keys = KeyExpansion(k, 4, Nr, Nk)
    res = multi_AES(T, s, keys, Nr, m)
    print(res)

if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
        'main'
        'addorminus',
        'gmul',
        'multiply',
        'G28_matrix_multiply',
        'trans',
        'hex2bytes',
        'hex2state',
        'state2hex',
        'strlist2hex',
        'intlist2hex',
        'int2list',
        'SubWord',
        'inSubWord',
        'RotWord',
        'KeyExpansion',
        'ByteSub',
        'ShiftRow',
        'MixColumns',
        'AddRoundKey',
        'Round',
        'AES_encode',
        'multi_AES',
    ])
    # 该段作用是关系图中不包括(exclude)哪些函数。(正则表达式规则)
    # config.trace_filter = GlobbingFilter(exclude=[
    #     'pycallgraph.*',
    #     '*.secret_function',
    #     'FileFinder.*',
    #     'ModuleLockManager.*',
    #     'SourceFilLoader.*'
    # ])
    graphviz = GraphvizOutput()
    graphviz.output_file = 'AES192256.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()

