from lab6 import *
import datetime as dt


def EDE(text, key1, key2):
    key1 = GenerateKey(key1)
    key2 = GenerateKey(key2)
    return EncryptChar(DecryptChar(EncryptChar(text, key1), key2), key1)


def FZFilt(n, b):
    s = bin(n)[2:]
    s = s[::-1]
    s = s + "0" * (b - len(s))
    s = s[::-1]
    return s


def XOR(a, b):
    a = int(a, 2)
    b = int(b, 2)
    c = a ^ b
    return FZFilt(c, 8)


def DT():
    d1 = dt.datetime.now()
    t = str(d1)
    t = t[-6:]
    t = int(t, 10) % 256
    t = FZFilt(t, 8)
    # print(d1, t)
    return t

def X9(key1, key2, iv):
    d = DT()
    ede1 = EDE(d, key1, key2)
    xor1 = XOR(ede1, iv)
    randm  = EDE(xor1, key1, key2)
    xor2 = XOR(ede1, randm)
    iv = EDE(xor2, key1, key2)
    return randm, iv

key1 = "1010000010"
key2 = "1000110010"
iv = FZFilt(3, 8)

r64 = ''
for i in range(8):
    randm, iv =  X9(key1, key2, iv)
    print(randm, int(randm, 2))
    r64 += randm
h = hex(int(r64, 2))[2:]
print(h)