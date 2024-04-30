import lab11
import lab9

INT_BITS = 128

def LeftRotate(n, d):
    return ((n << d) | (n >> (INT_BITS - d))) & 0xffffffffffffffffffffffffffffffff
def RightRotate(n, d):
    return ((n >> d) | (n << (INT_BITS - d))) & 0xffffffffffffffffffffffffffffffff


def H(st, s=""):
    while(len(st) < 16):
        st += " "
    st += s
    h = 0
    h1 = 0
    st1 = ""
    hh = []
    for i in st:
        nt = ord(i)
        st1 += hex(nt)[2:]
    for i in range(0, len(st1), 16):
        hh.append(int(st1[i:i+16], 16))
    for i in hh:
        h = RightRotate(h, 1) ^ i
        h1 = h1 ^ i
    return  h

def H2(m):
    file = open("./crypto/lab11Params.txt")
    p = int(file.readline())
    q = int(file.readline())
    e = int(file.readline())
    file.close()
    h = hex(H(m))[2:]
    en = lab11.Encrypt(h, p, q, e)
    h = m + lab9.ToHex(en)
    h1 = hex(H(h))[2:]
    d = lab11.Decrypt(en, p, q, e)
    return h1, d

def H1(m, s):
    file = open("./crypto/lab9En.txt", "r")
    aesKey = file.readline()[:-1].split("=")[1]
    file.close()
    h = hex(H(m, s))[2:]
    h = m + h 
    e = lab9.Encrypt(aesKey, h)
    d = lab9.Decrypt(aesKey, e)
    h = hex(H(d, s))[2:]
    return d, h
    

s = "test test tesing"
M = "hello"

h1 = H1(M, s)
h2 = H2(M)

print("h1 AES decrypt:", h1[0])
print("h1 hash       :", h1[1])
print("h2 RSA decrypt:", h2[0])
print("h2 hash       :", h2[1])

