def Euler(n):
    lis = [False for i in range(n+1)]
    primeNumber = []
    for i in range(2, n+1):
        if not lis[i]:
            primeNumber.append(i)
        for prime in primeNumber:
            if i*prime > n:
                break
            lis[i*prime] = True
            if i % prime == 0:
                break
    return primeNumber


n = int(input())
res = Euler(n)
count = 0
if n == 2 or n == 3:
    print(n)
else:
    for i in range(n):
        print(res[i], end=' ')
        count += 1
        if count == len(res):
            break