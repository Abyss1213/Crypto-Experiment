from random import randint


def gcd(x, y):  # 求最大公因子
    x = abs(x)
    y = abs(y)
    while x > 0:
        x, y = y % x, x  # 辗转相除
    return y


def isPrime(n):  # Miller-Rabin Test
    if n == 2:
        return True
    m = n - 1
    k = 0
    while gcd(m, 2) != 1:  # 当m还是偶数时
        m //= 2  # 数很大的时候一定要用整除啊！
        k += 1
    q = int((n - 1) // 2 ** k)  # 求k,q使 n-1 = 2^k*q with q odd

    for i in range(10):  # 试10次，n是合数还没遇到witness的概率已经极小了
        a = randint(2, n - 1)
        if gcd(a, n) != 1:  # 此时a是n的witness
            return False

        a = pow(a, q, n)
        t = 0
        if a % n == 1:
            continue
        for j in range(k):
            if a % n != n - 1:
                a = pow(a, 2, n)
                t += 1
            else:
                break  # 一旦有a^(2^i*q)=-1(mod n)，a不是witness。退出这个小循环，再换个a大循环
        if t == k:  # 所有a^(2^i*q)!=-1(mod n), n是合数
            return False
    return True


n = int(input())
if isPrime(n):
    print('yes')
else:
    print('no')
