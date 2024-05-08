p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
p8 = [5, 2, 6, 3, 7, 4, 9, 8]
ip8 = [1, 5, 2, 0, 3, 7, 4, 6]
ep = [3, 0, 1, 2, 1, 2, 3, 0]
p4 = [1, 3, 2, 0]
p1 = [3, 0, 2, 4, 6, 1, 7, 5]
s0 = [['01', '00', '11', '10'], ['11', '10', '01', '00'],
      ['00', '10', '01', '11'], ['11', '01', '11', '10']]
s1 = [['00', '01', '10', '11'], ['10', '00', '01', '11'],
      ['11', '00', '01', '00'], ['10', '01', '00', '11']]

import lab6 as SDES

initVector = "10101010"

def encrypt(plainText):
    binArray = plainText
    vec = initVector
    l = SDES.XORstr(vec, binArray[0])
    cbc = []
    cbc.append(SDES.EncryptChar(l, key))
    for i in range(len(binArray) - 1):
        l = SDES.XORstr(cbc[i], binArray[i + 1])
        cbc.append(SDES.EncryptChar(l, key))
    return cbc
def decrypt( cipherText):
    vec = initVector
    cbc = []
    l = SDES.XORstr(SDES.DecryptChar(cipherText[0], key), vec)
    cbc.append(l)
    for i in range(1, len(cipherText)):
        lo = SDES.DecryptChar(cipherText[i], key)
        l = SDES.XORstr(lo, cipherText[i - 1])
        cbc.append(l)
    return cbc

key = SDES.GenerateKey("0111111101")
plainText = ["00000001", "00100011"]
cipherText = encrypt(plainText)
print("cipher", cipherText)
plainText = decrypt(cipherText)
print("plain", plainText)
