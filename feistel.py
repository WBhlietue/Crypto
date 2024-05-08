def decimalToBinary(n,b):
    bnr=bin(n).replace("0b", "")
    bnr=bnr.rjust(b, '0') 
    return bnr

def binArray(text):
    binArr=[]
    for i in text:
        p=decimalToBinary(ord(i),8)
        binArr.append(p)
    
    return binArr

def feistel(plaintText):
    s16=""
    f_ed=[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
    for bitn in binArray(plaintText):
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



# plaintText = "unlimited blade works"
# plaintText = plaintText.upper()
# en=feistel(plaintText)
# print(en)
# de=feisteld(en)
# print(de)


