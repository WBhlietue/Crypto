
import random
import feistel

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

def ListShift(list):
    a = list[0]
    a = list[1:len(list)]
    a += list[0]
    return a

def XOR(a, b):
    if (a == b):
        return "0"
    return "1"

def XORstr(str1, str2):
    res = ""
    for i in range(len(str1)):
        res += (XOR(str1[i], str2[i]))
    return res

def ChangeIndex(list, index):
    str = ""
    for i in index:
        str += list[i]
    return str

def GenerateKey(key):
    pKey = ChangeIndex(key, p10)
    pKeyR = pKey[0:5]
    pKeyL = pKey[5:10]
    pKeyR = ListShift(pKeyR)
    pKeyL = ListShift(pKeyL)
    pKey = pKeyR + pKeyL
    pKey1 = ChangeIndex(pKey, p8)
    pKeyR = ListShift(pKeyR)
    pKeyL = ListShift(pKeyL)
    pKeyR = ListShift(pKeyR)
    pKeyL = ListShift(pKeyL)
    pKey = pKeyR + pKeyL
    pKey2 = ChangeIndex(pKey, p8)
    return (pKey1, pKey2)

def BinToDec(b):
    if (b == "00"):
        return 0
    if (b == "01"):
        return 1
    if (b == "10"):
        return 2
    return 3

def GetFromBox(c, l, s):
    return s[BinToDec(c)][BinToDec(l)]

def Rou(pChar, key):
    pCharR = pChar[0:4]
    pCharL = pChar[4:8]
    pCharLE = ChangeIndex(pCharL, ep)
    pCharLEX = XORstr(key, pCharLE)
    pCharLEXR = pCharLEX[0:4]
    pCharLEXL = pCharLEX[4:8]
    pCharLEXRL = pCharLEXR[0] + pCharLEXR[3]
    pCharLEXRC = pCharLEXR[1] + pCharLEXR[2]
    pCharLEXLL = pCharLEXL[0] + pCharLEXL[3]
    pCharLEXLC = pCharLEXL[1] + pCharLEXL[2]
    pCharLEXRM = GetFromBox(pCharLEXRL, pCharLEXRC, s0)
    pCharLEXLM = GetFromBox(pCharLEXLL, pCharLEXLC, s1)
    pCharLEXM = pCharLEXRM + pCharLEXLM
    pCharLEXMP = ChangeIndex(pCharLEXM, p4)
    pCharXOR = XORstr(pCharR, pCharLEXMP)
    return pCharL, pCharXOR

def EncryptChar(char, key):
    pChar = ChangeIndex(char, ip8)
    pChar = Rou(pChar, key[0])
    pChar = pChar[0] + pChar[1]
    pChar = Rou(pChar, key[1])
    pChar = pChar[1] + pChar[0]
    pCharMMP = ChangeIndex(pChar, p1)
    return pCharMMP
def DecryptChar(char, key):
    key = [key[1], key[0]]
    return EncryptChar(char, key)

def Encrypt(text, key):
    list = []
    for i in range(0, len(text), 2):
        char = feistel.decimalToBinary(int(text[i]+text[i+1], 16), 8)
        list.append(EncryptChar(char, key))
    hexList = []
    for i in list:
        dec = int(i, 2)
        hexValue = hex(dec)[2:]
        if(len(hexValue) == 1):
            hexValue = "0"+hexValue
        hexList.append(hexValue)
    res = "".join(hexList)
    return res

def Decrypt(text, key):
    list = []
    print(len(text))
    for i in range(0, len(text), 2):
        char = feistel.decimalToBinary(int(text[i]+text[i+1], 16), 8)
        list.append(DecryptChar(char, key))
    hexList = []
    for i in list:
        dec = int(i, 2)
        hexValue = hex(dec)[2:]
        if(len(hexValue) == 1):
            hexValue = "0"+hexValue
        hexList.append(hexValue)
    res = "".join(hexList)
    return res

if(__name__=="__main__"):

    key = "1010000010"
    # key = "".join(random.choice(["0", "1"]) for _ in range(10))
    print(key)
    key = GenerateKey(key)
    text = open("from.txt", "r")
    textValue = "".join(text)
    textValue = textValue.upper()
    binArray = feistel.binArray(textValue)
    feis = feistel.feistel(textValue)


    en = Encrypt(feis, key)

    file = open("to.txt", "w")
    # file.write(feistel.feisteld(en))
    file.write(en)

    de = Decrypt(en, key)
    res = feistel.feisteld(de)
    print(en)
    print(res)

