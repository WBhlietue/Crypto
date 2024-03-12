# cbc
# ofb
# counter
import lab6 as SDES
import feistel


def CBCEn(text, key):
    text = text.upper()
    binArray = feistel.binArray(text)
    vec = "00000000"
    l = SDES.XORstr(vec, binArray[0])
    cbc = []
    cbc.append(SDES.EncryptChar(l, key))
    for i in range(len(binArray) - 1):
        l = SDES.XORstr(binArray[i], binArray[i + 1])
        cbc.append(SDES.EncryptChar(l, key))
    return (cbc)


def CBCDe(arr, key):
    vec = "00000000"
    cbc = []
    last = arr[-1]
    l = SDES.XORstr(SDES.DecryptChar(arr[0], key), vec)
    cbc.append(l)
    for i in range(1, len(arr)):
        lo = SDES.DecryptChar(arr[i], key)
        l = SDES.XORstr(l, lo)
        cbc.append(l)
    text = ""
    for i in cbc:
        o = int(i, 2)
        text += chr(o)
    return (text)


def OFBEn(text, key):
    text = text.upper()
    binArray = feistel.binArray(text)
    non = "00000000"
    ofb = []
    for i in binArray:
        c = SDES.EncryptChar(non, key)
        l = SDES.XORstr(i, c)
        non = c
        ofb.append(SDES.EncryptChar(l, key))
    return (ofb)
def OFBDe(arr, key):
    non = "00000000"
    ofb = []
    for i in arr:
        c = SDES.EncryptChar(non, key)
        l = SDES.XORstr(SDES.DecryptChar(i, key), c)
        non = c
        ofb.append(l)
    text = ""
    for i in ofb:
        o = int(i, 2)
        text += chr(o)
    return (text)


def CounterEn(text, key):
    text = text.upper()
    binArray = feistel.binArray(text)
    c = []
    n = 0
    for i in binArray:
        nt = feistel.decimalToBinary(n, 8)
        o = SDES.EncryptChar(nt, key)
        l = SDES.XORstr(i, o)
        c.append(l)
        n += 1
    return c
def CounterDe(arr, key):
    c = []
    n = 0
    for i in arr:
        nt = feistel.decimalToBinary(n, 8)
        o = SDES.EncryptChar(nt, key)
        l = SDES.XORstr(i, o)
        c.append(l)
        n += 1
    text = ""
    for i in c:
        o = int(i, 2)
        text += chr(o)
    return (text)


text = "Unlimited Blade Works"
key = SDES.GenerateKey("0001000100")

cbc = (CBCEn(text, key))
print(CBCDe(cbc, key))

ofb = OFBEn(text, key)
print(OFBDe(ofb, key))

counter = CounterEn(text, key)
print(CounterDe(counter, key))