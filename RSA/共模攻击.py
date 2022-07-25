from gmpy2 import invert
# 很生气，因为没去掉换行符一直RE
e1 = int(input().strip().replace('\n', '').replace('\r', ''))
e2 = int(input().strip().replace('\n', '').replace('\r', ''))
c1 = int(input().strip().replace('\n', '').replace('\r', ''))
c2 = int(input().strip().replace('\n', '').replace('\r', ''))
N = int(input().strip().replace('\n', '').replace('\r', ''))
d1 = invert(e1, e2)
d2 = (1 - e1 * d1) // e2
res = (pow(c1, d1, N) * pow(c2, d2, N)) % N
print(res)
