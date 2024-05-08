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

class Feistel:
    def decimalToBinary(n,b):
        bnr=bin(n).replace("0b", "")
        bnr=bnr.rjust(b, '0') 
        return bnr

    def binArray(text):
        binArr=[]
        for i in text:
            p=Feistel.decimalToBinary(ord(i),8)
            binArr.append(p)
        
        return binArr

    def feistel(plaintText):
        s16=""
        f_ed=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
        for bitn in Feistel.binArray(plaintText):
            pt=int(bitn,2)
            pt1 = pt%16
            pt2 = pt//16
            en1 = f_ed[pt1]
            en2 = f_ed[pt2]
            s161 = hex(en1)[2:]
            s162 = hex(en2)[2:]
            s16 += s161+ s162
        return s16

    def feisteld(plaintText):
        s16=""
        f_ed=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
        for i in range(0,len(plaintText),2):
            pt1=int(plaintText[i],16)
            pt2=int(plaintText[i+1],16)
            de1=f_ed.index(pt1)
            de2=f_ed.index(pt2)
            tmdgt=de2*16+de1
            s16+=chr(tmdgt)
        return s16
class SDES:
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
            res += (SDES.XOR(str1[i], str2[i]))
        return res

    def ChangeIndex(list, index):
        str = ""
        for i in index:
            str += list[i]
        return str

    def GenerateKey(key):
        pKey = SDES.ChangeIndex(key, p10)
        pKeyR = pKey[0:5]
        pKeyL = pKey[5:10]
        pKeyR = SDES.ListShift(pKeyR)
        pKeyL = SDES.ListShift(pKeyL)
        pKey = pKeyR + pKeyL
        pKey1 = SDES.ChangeIndex(pKey, p8)
        pKeyR = SDES.ListShift(pKeyR)
        pKeyL = SDES.ListShift(pKeyL)
        pKeyR = SDES.ListShift(pKeyR)
        pKeyL = SDES.ListShift(pKeyL)
        pKey = pKeyR + pKeyL
        pKey2 = SDES.ChangeIndex(pKey, p8)
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
        return s[SDES.BinToDec(c)][SDES.BinToDec(l)]

    def Rou(pChar, key):
        pCharR = pChar[0:4]
        pCharL = pChar[4:8]
        pCharLE = SDES.ChangeIndex(pCharL, ep)
        pCharLEX = SDES.XORstr(key, pCharLE)
        pCharLEXR = pCharLEX[0:4]
        pCharLEXL = pCharLEX[4:8]
        pCharLEXRL = pCharLEXR[0] + pCharLEXR[3]
        pCharLEXRC = pCharLEXR[1] + pCharLEXR[2]
        pCharLEXLL = pCharLEXL[0] + pCharLEXL[3]
        pCharLEXLC = pCharLEXL[1] + pCharLEXL[2]
        pCharLEXRM = SDES.GetFromBox(pCharLEXRL, pCharLEXRC, s0)
        pCharLEXLM = SDES.GetFromBox(pCharLEXLL, pCharLEXLC, s1)
        pCharLEXM = pCharLEXRM + pCharLEXLM
        pCharLEXMP = SDES.ChangeIndex(pCharLEXM, p4)
        pCharXOR = SDES.XORstr(pCharR, pCharLEXMP)
        return pCharL, pCharXOR

    def EncryptChar(char, key):
        pChar = SDES.ChangeIndex(char, ip8)
        pChar = SDES.Rou(pChar, key[0])
        pChar = pChar[0] + pChar[1]
        pChar = SDES.Rou(pChar, key[1])
        pChar = pChar[1] + pChar[0]
        pCharMMP = SDES.ChangeIndex(pChar, p1)
        return pCharMMP
    def DecryptChar(char, key):
        key = [key[1], key[0]]
        return SDES.EncryptChar(char, key)

    def Encrypt(text, key):
        list = []
        for i in range(0, len(text), 2):
            char = Feistel.decimalToBinary(int(text[i]+text[i+1], 16), 8)
            list.append(SDES.EncryptChar(char, key))
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
            char = Feistel.decimalToBinary(int(text[i]+text[i+1], 16), 8)
            list.append(SDES.DecryptChar(char, key))
        hexList = []
        for i in list:
            dec = int(i, 2)
            hexValue = hex(dec)[2:]
            if(len(hexValue) == 1):
                hexValue = "0"+hexValue
            hexList.append(hexValue)
        res = "".join(hexList)
        return res

class CBC:
    def __init__(self):
        self.initVector = "00000000"
        self.key = ""
        pass
    def Encrypt(self, plainText):
        binArray = plainText
        vec = self.initVector
        l = SDES.XORstr(vec, binArray[0])
        cbc = []
        cbc.append(SDES.EncryptChar(l, self.key))
        for i in range(len(binArray) - 1):
            l = SDES.XORstr(cbc[i], binArray[i + 1])
            cbc.append(SDES.EncryptChar(l, self.key))
        return cbc
    def Decrypt(self, cipherText):
        vec = self.initVector
        cbc = []
        l = SDES.XORstr(SDES.DecryptChar(cipherText[0], self.key), vec)
        cbc.append(l)
        for i in range(1, len(cipherText)):
            lo = SDES.DecryptChar(cipherText[i], self.key)
            l = SDES.XORstr(lo, cipherText[i - 1])
            cbc.append(l)
        return cbc
    def SetKey(self, key):
        self.key = SDES.GenerateKey(key)
    def SetInitVector(self, initVector):
        self.initVector = initVector



cbc = CBC()
cbc.SetKey("0111111101")
cbc.SetInitVector("10101010")

plainText = ["00000001", "00100011"]

cipherText = cbc.Encrypt(plainText)
print(cipherText)

plainText = cbc.Decrypt(cipherText)
print(plainText)
