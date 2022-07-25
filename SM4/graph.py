from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from pycallgraph2 import Config
from pycallgraph2 import GlobbingFilter
import sys

def main():
    def inverse(u, v):  # 辗转相除求逆
        u2, v2 = int(u), int(v)
        u1, v1 = 1, 0
        while v2 > 0:
            q = divmod(u2, v2)[0]  # divmod(x, y, /) Return the tuple (x//y, x%y)
            u1, v1 = v1, u1 - v1 * q
            u2, v2 = v2, u2 - v2 * q
        while u1 < 0:
            u1 = u1 + v
        return u1

    def crtdecode(c, d, p, q):  # 中国剩余定理加速解密
        m1 = pow(c % p, d % (p - 1), p)
        m2 = pow(c % q, d % (q - 1), q)
        a = inverse(q, p)
        b = inverse(p, q)
        m = (m1 * a * q + m2 * b * p) % (p * q)
        return m

    def RSA(p, q, e, m, op):
        n = p * q
        if op == 1:
            res = pow(m, e, n)
        else:
            phi = (p - 1) * (q - 1)
            d = inverse(e, phi)
            # res = pow(m, d, n)
            res = crtdecode(m, d, p, q)
        return res

    p = int(input())
    q = int(input())
    e = int(input())
    m = int(input())
    op = int(input())
    print(RSA(p, q, e, m, op))

if __name__ == "__main__":
    config = Config()
    # 关系图中包括(include)哪些函数名。
    # 如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，表示以gobang.开头的所有函数。（利用正则表达式）。
    config.trace_filter = GlobbingFilter(include=[
        'inverse',
        'crtdecode',
        'RSA',
        # 'SubWord',
        # 'SM4',
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
    graphviz.output_file = 'RSA.png'
    with PyCallGraph(output=graphviz, config=config):
        main()

