from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from pycallgraph2 import Config
from pycallgraph2 import GlobbingFilter


Key_Substitution_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
                      10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
                      63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
                      14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]  # 已经去掉校验位了

def main():
    def parity(key_56, m):
        res = []
        for i in range(8):
            t = 0
            for j in range(7):
                if key_56[i * 7 + j] == '1':
                    t += 1
            if m == 1:  # odd check
                if t % 2 == 1:
                    res.append('0')
                else:
                    res.append('1')
            else:  # even check
                if t % 2 == 1:
                    res.append('1')
                else:
                    res.append('0')
        return res

    def hexy(s):
        res = ''.join(list(map(str, s)))  # list转str
        res = int(hex(int(res, 2)), 16)  # 以十六进制输出
        res = '{:016x}'.format(res)  # 补齐16位
        res = '0x' + res
        return res

    def retrans1(key_56, m):
        res = []
        for i in range(64):
            res.append('*')
        for j in range(56):
            res[Key_Substitution_1[j] - 1] = key_56[j]
        parity_bits = parity(key_56, m)
        for k in range(8):
            res[(k + 1) * 8 - 1] = parity_bits[k]
        return hexy(res)

    def hex2bin(s):  # 用于将28位密钥变成二进制字符串
        s_bin = int(bin(int(s, 16)).replace('0b', ''), 2)
        s_bin = '{:028b}'.format(s_bin)
        return s_bin

    def weak_keys():
        C = '0x0000000'  # 56位的弱密钥左移无效，只能是全0与全1的组合
        D = '0xFFFFFFF'
        C = hex2bin(C)
        D = hex2bin(D)
        keys_56 = [C + C, C + D, D + C, D + D]
        weak = []
        for i in range(4):
            rekey_odd = retrans1(keys_56[i], 1)
            weak.append(rekey_odd)
        for j in range(4):
            rekey_even = retrans1(keys_56[j], 0)
            weak.append(rekey_even)
        return weak

    def halfweak_keys():
        A = '0x5555555'  # 56位半弱密钥只能是这四段28位密钥组合，共12种
        B = '0xAAAAAAA'  # 其中互逆密钥满足A对应B，C对应D
        C = '0x0000000'
        D = '0xFFFFFFF'
        A = hex2bin(A)
        B = hex2bin(B)
        C = hex2bin(C)
        D = hex2bin(D)
        keys_56 = [A + A, B + B, A + B, B + A, A + C, B + C, A + D, B + D, C + A, C + B, D + A, D + B]
        halfweak = []
        for i in range(12):
            rekey_odd = retrans1(keys_56[i], 1)
            halfweak.append(rekey_odd)
        for j in range(12):
            rekey_even = retrans1(keys_56[j], 0)
            halfweak.append(rekey_even)
        return halfweak

    weak = weak_keys()
    halfweak = halfweak_keys()
    for i in range(8):
        print(weak[i])
    for j in range(12):
        print(halfweak[2 * j], halfweak[2 * j + 1])


if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
        'main'
        'parity',
        'hexy',
        'retrans1',
        'hex2bin',
        'weak_keys',
        'halfweak_keys',
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
    graphviz.output_file = 'weak_keys.py.png'
    with PyCallGraph(output=graphviz, config=config):
        main()

