Sbox = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B,
    0xFE, 0xD7, 0xAB, 0x76, 0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0,
    0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0, 0xB7, 0xFD, 0x93, 0x26,
    0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2,
    0xEB, 0x27, 0xB2, 0x75, 0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0,
    0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84, 0x53, 0xD1, 0x00, 0xED,
    0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F,
    0x50, 0x3C, 0x9F, 0xA8, 0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5,
    0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2, 0xCD, 0x0C, 0x13, 0xEC,
    0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14,
    0xDE, 0x5E, 0x0B, 0xDB, 0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C,
    0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79, 0xE7, 0xC8, 0x37, 0x6D,
    0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F,
    0x4B, 0xBD, 0x8B, 0x8A, 0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E,
    0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E, 0xE1, 0xF8, 0x98, 0x11,
    0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F,
    0xB0, 0x54, 0xBB, 0x16
]
Sbox_inv = [
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E,
    0x81, 0xF3, 0xD7, 0xFB, 0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87,
    0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB, 0x54, 0x7B, 0x94, 0x32,
    0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49,
    0x6D, 0x8B, 0xD1, 0x25, 0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16,
    0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92, 0x6C, 0x70, 0x48, 0x50,
    0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05,
    0xB8, 0xB3, 0x45, 0x06, 0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02,
    0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B, 0x3A, 0x91, 0x11, 0x41,
    0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8,
    0x1C, 0x75, 0xDF, 0x6E, 0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89,
    0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B, 0xFC, 0x56, 0x3E, 0x4B,
    0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59,
    0x27, 0x80, 0xEC, 0x5F, 0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D,
    0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF, 0xA0, 0xE0, 0x3B, 0x4D,
    0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63,
    0x55, 0x21, 0x0C, 0x7D
]

Key = ""
def subByte(st, sbx):
    sb = []
    for i in st:
        sb.append(sbx[i])
    return sb


def hexList(st):
    hx = []
    for i in st:
        hx.append(ord(i))
    return hx


def rotWord(st, n):
    return st[n:] + st[0:n]


def XOR(a, b):
    hhx = []
    for i in range(0, len(a)):
        hx = a[i] ^ b[i]
        hhx.append(hx)

    return hhx


def wlist(sthx):
    w = []
    RC = [0, 1, 2, 4, 8, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
    for i in range(0, 4):
        w.append(sthx[i * 4:i * 4 + 4])

    for i in range(4, 44):
        Rcon = [RC[i // 4], 0, 0, 0]
        temp = w[i - 1]
        if i % 4 == 0:
            temp = XOR(subByte(rotWord(temp, 1), Sbox), Rcon)
        w.append(XOR(w[i - 4], temp))

    return w


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


def mix_columns(st):
    ss = []
    st2 = []
    for i in range(0, 4):
        ss.append(st[i * 4:i * 4 + 4])
    for i in range(0, 4):
        gg = 0
        gg ^= gmul(0x02, ss[i][0])
        gg ^= gmul(0x03, ss[i][1])
        gg ^= ss[i][2]
        gg ^= ss[i][3]
        st2.append(gg)

        gg = 0
        gg ^= ss[i][0]
        gg ^= gmul(0x02, ss[i][1])
        gg ^= gmul(0x03, ss[i][2])
        gg ^= ss[i][3]
        st2.append(gg)

        gg = 0
        gg ^= ss[i][0]
        gg ^= ss[i][1]
        gg ^= gmul(0x02, ss[i][2])
        gg ^= gmul(0x03, ss[i][3])
        st2.append(gg)

        gg = 0
        gg ^= gmul(0x03, ss[i][0])
        gg ^= ss[i][1]
        gg ^= ss[i][2]
        gg ^= gmul(0x02, ss[i][3])
        st2.append(gg)
    return st2


def inv_mix_columns(st):
    ss = []
    st2 = []
    for i in range(0, 4):
        ss.append(st[i * 4:i * 4 + 4])
    for i in range(0, 4):
        gg = 0
        gg ^= gmul(0x0E, ss[i][0])
        gg ^= gmul(0x0B, ss[i][1])
        gg ^= gmul(0x0D, ss[i][2])
        gg ^= gmul(0x09, ss[i][3])
        st2.append(gg)

        gg = 0
        gg ^= gmul(0x09, ss[i][0])
        gg ^= gmul(0x0E, ss[i][1])
        gg ^= gmul(0x0B, ss[i][2])
        gg ^= gmul(0x0D, ss[i][3])
        st2.append(gg)

        gg = 0
        gg ^= gmul(0x0D, ss[i][0])
        gg ^= gmul(0x09, ss[i][1])
        gg ^= gmul(0x0E, ss[i][2])
        gg ^= gmul(0x0B, ss[i][3])
        st2.append(gg)

        gg = 0
        gg ^= gmul(0x0B, ss[i][0])
        gg ^= gmul(0x0D, ss[i][1])
        gg ^= gmul(0x09, ss[i][2])
        gg ^= gmul(0x0E, ss[i][3])
        st2.append(gg)

    return st2


def shiftRow(st):
    m = []
    m.append([st[0], st[4], st[8], st[12]])
    m.append([st[1], st[5], st[9], st[13]])
    m.append([st[2], st[6], st[10], st[14]])
    m.append([st[3], st[7], st[11], st[15]])

    m[1] = rotWord(m[1], 1)
    m[2] = rotWord(m[2], 2)
    m[3] = rotWord(m[3], 3)
    st1 = []
    for j in range(0, 4):
        for i in range(0, 4):
            st1.append(m[i][j])
    return st1


def inv_shiftRow(st):
    m = []

    m.append([st[0], st[4], st[8], st[12]])
    m.append([st[1], st[5], st[9], st[13]])
    m.append([st[2], st[6], st[10], st[14]])
    m.append([st[3], st[7], st[11], st[15]])

    m[1] = rotWord(m[1], 3)
    m[2] = rotWord(m[2], 2)
    m[3] = rotWord(m[3], 1)
    st1 = []
    for j in range(0, 4):
        for i in range(0, 4):
            st1.append(m[i][j])
    return st1


def addRoundKey(a, ww):
    w1 = []
    for i in ww:
        for j in i:
            w1.append(j)
    return XOR(a, w1)


def AES(Key, PlainText):
    PlainText = TextToHex(PlainText)
    keyList = st_2_16(Key)
    pList = st_2_16(PlainText)
    w = wlist(keyList)
    st0 = addRoundKey(pList, w[0:4])
    for i in range(1, 11):
        st0 = subByte(st0, Sbox)
        st0 = shiftRow(st0)
        if i != 10:
            st0 = mix_columns(st0)
        st0 = addRoundKey(st0, w[4 * i:4 * i + 4])
    return st0
def AES16(Key, hex):
    keyList = st_2_16A(Key)
    pList = st_2_16A(hex)
    w = wlist(keyList)
    st0 = addRoundKey(pList, w[0:4])
    for i in range(1, 11):
        st0 = subByte(st0, Sbox)
        st0 = shiftRow(st0)
        if i != 10:
            st0 = mix_columns(st0)
        st0 = addRoundKey(st0, w[4 * i:4 * i + 4])
    st0= ToHex(st0)
    return st0


def AES_de(Key, PlainText):
    keyList = st_2_16(Key)
    pList = PlainText
    w = wlist(keyList)
    st0 = addRoundKey(pList, w[40:44])
    for i in range(9, -1, -1):
        st0 = inv_shiftRow(st0)
        st0 = subByte(st0, Sbox_inv)
        st0 = addRoundKey(st0, w[4 * i:4 * i + 4])
        if (i != 0):
            st0 = inv_mix_columns(st0)
    return st0


def st_2_16(st):
    while(len(st) % 32 != 0):
        st += "00"
    p = []
    for i in range(0, len(Key), 2):
        
        a = st[i:i + 2]
        if(len(a) != 0):
            p.append(int(st[i:i + 2], 16))
    return p
def st_2_16A(st):
    while(len(st) % 32 != 0):
        st += "00"
    p = []
    for i in range(0, len(st), 2):
        
        a = st[i:i + 2]
        if(len(a) != 0):
            p.append(int(st[i:i + 2], 16))
    return p


def ToHex(array):
    h = ""
    for i in array:
        a = hex(i)
        if (len(a) == 3):
            h += "0"
        h += a[2:]
    return h
def PrintKey(key):
    list = st_2_16(key)
    list = wlist(list)
    for i in list:
        num = str(list.index(i))
        if(len(num) == 1):
            num = "0" + num
        print(num, end=". ")
        for j in i:
            a = hex(j)[2:]
            if(len(a) == 1):
                a = "0" + a
            print(a, end=" ")
        print("")

def TextToHex(text):
    h = ""
    for i in text:
        num = str(hex(ord(i))[2:])
        if(len(num) == 1):
            num = "0" + num
        h += num
    return h
def HexToText(h):
    text = ""
    for i in range(0, len(h), 2):
        num = h[i]+h[i+1]
        if(num != "00"):
            text += chr(int(num , 16))
    return text



def Encrypt(key, text):
    global Key
    Key = key
    crypt = ""
    for i in range(0, len(text) // 16 + 1):
        block = text[i * 16:i * 16 + 16]
        if(len(block) == 0):
            break
        result = (AES(key, block))
        crypt+=ToHex(result)
    return crypt


def Decrypt(key, text):
    global Key
    Key = key
    t = ""
    for i in range(0, len(text) // 32 + 1):
        block = text[i * 32:i * 32 + 32]
        if(len(block) == 0):
            break
        result = AES_de(key, st_2_16(block))
        res = HexToText(ToHex(result))
        t += res
    return t

if(__name__ == "__main__"):

    readFile = open("./crypto/lab9En.txt", "r")
    Key = readFile.readline()[:-1].split("=")[1]
    PlainText = "".join(readFile.readlines())
    readFile.close()

    res = Encrypt(Key, PlainText)
    decFile = open("./crypto/lab9De.txt", "w")
    decFile.writelines(Key + "\n")
    decFile.writelines((res))
    decFile.close()
    decFile = open("./crypto/lab9De.txt", "r")
    Key = decFile.readline()[:-1]
    text = decFile.readline()
    decFile.close()

    result = Decrypt(Key, text)
    resultFile = open("./crypto/lab9Res.txt", "w")
    resultFile.writelines(((result)))