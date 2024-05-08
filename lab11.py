import numpy as np

a = 7
b = 560 
n = 561 # 1
a = 10260
b = 5891
n = 11023 # 3314



def ModInverse(a, m):
    return pow(a, -1, m)

def D1(a, b, n):
    c = 0
    f = 1
    for bi in bin(b)[2:]:
        c = c * 2 
        f = (f * f) % n 
        if bi == "1":
            c = c + 1 
            f = (f * a) % n
    return f

letters = "abcdefghijklmnopqrstuvwxyz"
letters += letters.upper()
letters += "0123456789 @[]?()#,:;.-'\"_=\n"

def RSA(P, p, q, e, en):
    CC = []
    p = 7
    q = 11
    n = p * q 
    e = 13
    et = (p-1) * (q-1)
    d = pow(e, -1, et)
    for pp in P:
        if en != "en":
            e = d 
        CC.append(D1(pp, e, n))
    return CC

print(RSA([20], 1, 1, 1, "de"))

def RSAEnDe(txt, p, q, e, en):
    list = []
    for i in txt:
        list.append(letters.index(i))
    arr =np.reshape(list, [-1, 2])
    P = []
    for i in arr:
        st2 = i[0] * 100 + i[1]
        P.append(st2)

    result = RSA(P, p, q,e,  en)
    return result

def Encrypt(txt, p, q, e):
    return RSAEnDe(txt,p, q, e, "en")
def Decrypt(l, p, q, e):
    result = RSA(l, p, q,e, "de")
    list = []
    for i in result:
        x1 = i // 100
        x2 = i % 100
        list.append(x1)
        list.append(x2)
    str = ""
    for i in list:
        str += letters[i]
    return str
    

# file = open("./crypto/lab11Params.txt")
# p = int(file.readline())
# q = int(file.readline())
# e = int(file.readline())
# file.close()

# file = open("./crypto/lab11Input.txt", "r")
# txt = file.read()
# if(len(txt) % 2 != 0):
#     txt = txt + " "
# file.close()
# file = open("./crypto/lab11En.txt", "w")
# en = Encrypt(txt, p, q, e)
# file.write(str(en))
# file.close()
# file = open("./crypto/lab11De.txt", "w")
# de = Decrypt(en, p, q, e)
# file.write(str(de))
# file.close()


# print(D1(a, b, n))


# print(RSA(P=[8], p=7, q=11, e=17, en="en"))