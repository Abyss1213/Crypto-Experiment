w, n, m, r = 32, 624, 397, 31
a = 0x9908B0DF
f = 1812433253
u, d = 11, 0xFFFFFFFF
s, b = 7, 0x9D2C5680
t, c = 15, 0xEFC60000
l = 18


def seed_mt(seed: int):
    MT = [seed]
    for i in range(1, n):
        temp = f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i
        MT.append(temp & d)
    return MT


lower_mask = (1 << r) - 1
upper_mask = ~ lower_mask
def twist(MT):
    for i in range(n):
        x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
        xA = x >> 1
        if x % 2 != 0:
            xA = xA ^ a
        MT[i] = MT[(i+m) % n] ^ xA


def extract_number(MT, index):
    if index == 0:
        twist(MT)
    x = MT[index]
    y = x ^ ((x >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    z = y ^ (y >> l)
    return z

seed = int(input())
MT = seed_mt(seed)
index = 0
for j in range(20):
    print(extract_number(MT, index))
    index = (index + 1) % n