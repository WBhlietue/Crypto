
import datetime as dt
import math
import lab9 as T


def DT():
    dt_now = str(dt.datetime.now())[-16:]
    dt_now = T.TextToHex(dt_now)
    return dt_now



def gmul(a, b):
    p = 0
    for c in range(8):
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11b
        b >>= 1
    return p

def ToBin(num):
    b = bin(num)[2:]
    while(len(b) < 8):
        b = "0" + b
    b = b[0:4] + " " +b[4:8]
    return b

def mix_columns(st):
    ss = []
    st2 = []
    for i in range(0, 4):
        ss.append(st[i * 4:i * 4 + 4])
    for i in range(0, 4):
        gg = 0
        gg ^= gmul(0x02, ss[i][0])
        print(f"{'02'} * {hex(ss[i][0])[2:]} = {ToBin(gg)}")
        gg ^= gmul(0x03, ss[i][1])
        print(f"{'03'} * {hex(ss[i][1])[2:]} = {ToBin(gmul(0x03, ss[i][1]))}")
        gg ^= ss[i][2]
        print(f"{hex(ss[i][2])[2:]}      = {ToBin(ss[i][2])}")
        gg ^= ss[i][3]
        print(f"{hex(ss[i][3])[2:]}      = {ToBin(ss[i][3])}")
        print(f"          {ToBin(gg)}  {hex(gg)[2:]}")
        st2.append(gg)

        gg = 0
        gg ^= ss[i][0]
        print(f"{hex(ss[i][0])[2:]}      = {ToBin(ss[i][0])}")
        gg ^= gmul(0x02, ss[i][1])
        print(f"{'02'} * {hex(ss[i][1])[2:]} = {ToBin(gg)}")
        gg ^= gmul(0x03, ss[i][2])
        print(f"{'03'} * {hex(ss[i][2])[2:]} = {ToBin(gg)}")
        gg ^= ss[i][3]
        print(f"{hex(ss[i][3])[2:]}      = {ToBin(ss[i][3])}")
        print(f"          {ToBin(gg)}  {hex(gg)[2:]}")
        st2.append(gg)

        gg = 0
        gg ^= ss[i][0]
        print(f"{hex(ss[i][0])[2:]}      = {ToBin(ss[i][0])}")
        gg ^= ss[i][1]
        print(f"{hex(ss[i][1])[2:]}      = {ToBin(ss[i][1])}")
        gg ^= gmul(0x02, ss[i][2])
        print(f"{'02'} * {hex(ss[i][2])[2:]} = {ToBin(gg)}")
        gg ^= gmul(0x03, ss[i][3])
        print(f"{'03'} * {hex(ss[i][3])[2:]} = {ToBin(gg)}")
        print(f"          {ToBin(gg)}  {hex(gg)[2:]}")

        st2.append(gg)

        gg = 0
        gg ^= gmul(0x03, ss[i][0])
        print(f"{'03'} * {hex(ss[i][0])[2:]} = {ToBin(gg)}")
        gg ^= ss[i][1]
        print(f"{hex(ss[i][1])[2:]}      = {ToBin(ss[i][1])}")
        gg ^= ss[i][2]
        print(f"{hex(ss[i][2])[2:]}      = {ToBin(ss[i][2])}")
        gg ^= gmul(0x02, ss[i][3])
        print(f"{'02'} * {hex(ss[i][3])[2:]} = {ToBin(gg)}")
        print(f"          {ToBin(gg)}  {hex(gg)[2:]}")
        st2.append(gg)
        print("\n\n")
    return st2

key = "cfb0ef3108d49cc4562d5810b0a9af60"
v = DT()
# v = "4c89af496176b728ed1e2ea8ba27f5a4"
pwr = int(math.pow(2, 128))

def RandomNumberOFB():
    global v
    value = T.AES16(key, v)
    v = value
    return value


def RandomNumberCTR():
    global v
    value = T.AES16(key, v)
    l = len(v)
    num = (int(v, 16) + 1) % pwr
    num = hex(num)[2:]
    while (len(num) < l):
        num = "0" + num
    v = num
    return value
# for i in range(10):
#     print(RandomNumberOFB())

# v = "4c89af496176b728ed1e2ea8ba27f5a4"

# print("--------------------------------")

# for i in range(8):
#     print(RandomNumberCTR())


# txtFile = open("./crypto/lab10mix.txt")
# txt = txtFile.readline()
# txtFile.close()

# s16 = T.st_2_16A(T.TextToHex(txt))
# # print(s16)
s16 = T.st_2_16A("876e46a6f24ce78c4d904ad897ecc395")
mix = mix_columns(s16)
# print(mix)
# print(mix)
# mix = T.mix_columns(s16)
# print(mix)
