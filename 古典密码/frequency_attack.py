def find_max(lis):
    max = lis[0]
    index = 0
    for i in range(1, len(lis)):
        if max <= lis[i]:
            max = lis[i]
            index = i
    return max, index


def frequency(s):
    f = []  # f用于统计字母频率
    for j in range(26):
        f.append(0)
    for i in s:
        f[ord(i)-97] += 1
    x = find_max(f)[1]
    k = (x-4) % 26
    return k


s = input().strip().replace('\n', '').replace('\r', '')
print(frequency(s))
