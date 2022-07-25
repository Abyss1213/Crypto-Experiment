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


def inverse(a):
    if a == 0x00:
        return 0x00
    else:
        i = 0x01
        while i <= 0xff and i != 0x00:
            if multiply(a, i, poly) == 0x01:
                return i
            else:
                i += 1


def matrix_multiply(a, b):
    res = []
    for i in range(len(a)):
        res.append([])
    for x in range(len(a)):
        for y in range(len(b[0])):
            res[x].append(0)

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
            res[x][y] = temp
    return res


def matrix_plus(a, b):  # 模2加
    res = []
    for i in range(len(a)):
        res.append([])
    for x in range(len(a)):
        for y in range(len(a[0])):
            res[x].append(0)
    for x in range(len(a)):
        for y in range(len(a[0])):
            res[x][y] =(a[x][y] + b[x][y]) % 2
    return res


def SBox_change(s):  # 对一个字节（8位）的仿射变换
    A = [[1, 0, 0, 0, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 1]]
    s_bin = '{:08b}'.format(int(bin(int(s, 16)), 2))
    B = []
    for i in range(8):
        B.append([])
    for i in range(8):
        B[i].append(int(s_bin[7-i]))
    C = [[1], [1], [0], [0], [0], [1], [1], [0]]
    temp = matrix_multiply(A, B)
    res = matrix_plus(temp, C)
    temp = ''
    for i in range(8):
        temp += str(res[7-i][0])
    res = '0x' + '{:02x}'.format(int(hex(int(temp, 2)), 16))
    return res


def SBox_rechange(s):  # 对一个字节（8位）的仿射变换
    A = [[0, 0, 1, 0, 0, 1, 0, 1],
         [1, 0, 0, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0, 0, 1],
         [1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 0, 1, 0]]
    s_bin = '{:08b}'.format(int(bin(int(s, 16)), 2))
    B = []
    for i in range(8):
        B.append([])
    for i in range(8):
        B[i].append(int(s_bin[7-i]))
    C = [[1], [0], [1], [0], [0], [0], [0], [0]]
    temp = matrix_multiply(A, B)
    res = matrix_plus(temp, C)
    temp = ''
    for i in range(8):
        temp += str(res[7-i][0])
    res = '0x' + '{:02x}'.format(int(hex(int(temp, 2)), 16))
    return res


def Print(str):
    for i in range(16):
        for j in range(16):
            if j == 15:
                print(str[16 * i + j])
            else:
                print(str[16 * i + j], end=' ')


def SBox_origin():
    SBox_origin = []
    for i in range(0x100):
        SBox_origin.append('0x' + '{:02x}'.format(int(hex(i), 16)))
    return SBox_origin


def SBox_inverse():
    SBox_inverse = []
    temp = SBox_origin()
    for i in temp:
        SBox_inverse.append('0x' + '{:02x}'.format(inverse(int(i, 16))))
    return SBox_inverse


def SBox_byte():
    SBox_byte = []
    temp = SBox_inverse()
    for i in temp:
        SBox_byte.append(SBox_change(i))

    return SBox_byte

def inSbox():
    inSBox = []
    temp0 = []
    temp1 = SBox_origin()
    for i in temp1:
        temp0.append(SBox_rechange(i))
    for i in temp0:
        inSBox.append('0x' + '{:02x}'.format(inverse(int(i, 16))))
    return inSBox


poly = int('0x11b', 16)
a = SBox_origin()
b = SBox_inverse()
c = SBox_byte()
d = inSbox()
print('inverse_sbox:')
Print(d)
# Print(b)
# Print(c)
# Print(d)