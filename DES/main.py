import math
def comb(n, m):
    # 直接使用math里的阶乘函数计算组合数
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))
# N = 0
# for i in range(11, 20):
#     p = pow(0.6, i)*pow(0.4, 25-i)
#     c = comb(25, i)
#     res = p*c
#     res += res
#     N += c
#     print(p, c, res, N)

h = -0.6*math.log2(0.6)-0.4*math.log2(0.4)
e = 0.01
res = 0
for i in range(10):
    e += 0.001*i
    L = pow(2, -25 * (h + e))
    R = pow(2, -25 * (h - e))
    print('......',e,L,R)
    for j in range(26):
        p = pow(0.6, j)*pow(0.4, 25-j)
        if p >= L and p <= R:
            c = comb(25, j)
            temp = p*c
            res += temp
            print('!!!!!',j,p,c,res)

