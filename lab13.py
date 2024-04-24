

import random


def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

def PQ(P, Q, p):
    xQ = Q[0]
    yQ = Q[1]
    xP = P[0]
    yP = P[1]

    dtu= (yQ - yP) % p
    dtd = (xQ - xP) % p
    gcd = GCD(dtu, dtd)
    if(gcd == dtd):
        dt = dtu // dtd
    else:
        dtu = dtu // gcd
        dtd = dtd // gcd 
        dt = (pow(dtd, -1, p)*dtu) % p
    return dt 
def PP(P, a, p):
    xP = P[0]
    yP = P[1]
    dtu = (3*(xP**2)+a)%p
    dtd = (2*yP)%p
    gcd = GCD(dtu, dtd)
    if (gcd == dtd):
        dt = dtu // dtd
    else:
        dtu = dtu // gcd
        dtd = dtd // gcd
        dt = (pow(dtd, -1, p)*dtu) % p
    return dt 

def ECCPQ(P, Q, a, p):
    if(P[0] == Q[0] and P[1] == Q[1]):
        L = PP(P, a, p)
    else:
        L = PQ(P, Q, p)
    xQ = Q[0]
    yQ = Q[1]
    xP = P[0]
    yP = P[1]
    xR = (L** 2 - xP - xQ) % p
    yR = (L*(xP - xR) - yP) % p
    return (xR, yR)

def Mult(na, G, a, p):
    P = G
    for i in range(1, na):
        P = ECCPQ(P, G, a, p)
    return P
def Neg(P):
    return (P[0], -P[1])

#Encrypt. decrypt, text file
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
# alpha += ",./;'[]-=<>?:\"{}|\\_+!@#$%^&*()`~\n"
p = 257
a = 0
b = -4
G = (2, 2)
nb = 101
pm = (68, 84)
k = 41
PB = Mult(nb, G, a, p)
# C1 = kG = Mult(k, G, a, p)
# print(C1)
# kpB = Mult(k, PB, a, p)
# print(kpB)
# C2 = ECCPQ(pm, kpB, a, p)
# nbC1 = Mult(nb, C1, a, p)
# nbC1 = Neg(nbC1)
# print(nbC1)

# PM = ECCPQ(C2, nbC1, a, p)
# print(pm, PB, kpB, kG, C2, PM)

ecca = []
for i in range(len(alpha)):
    res = Mult(i+2, G, a, p)
    ecca.append(res)
print(ecca, end="\n\n")



##########

kk = [4, 13, 22, 23, 32, 41, 46, 50, 53, 55, 59, 64, 73, 82, 91, 101, 110, 115, 119, 124, 128]
def Encrypt(text, G, a, p):
    ecca = []
    for i in range(len(alpha)):
        res = Mult(i+2, G, a, p)
        ecca.append(res) 
    result = []
    for ch in text:
        ind = alpha.index(ch)
        Pm = ecca[ind]
        k = random.choice(kk)
        nb = 101 
        Pb = Mult(nb, G, a, p)
        c1 = Mult(k, G, a, p)
        c2 = ECCPQ(Pm, Mult(k, Pb, a, p), a, p)
        result.append(c1[0])
        result.append(c1[1])
        result.append(c2[0])
        result.append(c2[1])
    return result

def Decrypt(text, G, a, p):
    ecca = []
    for i in range(len(alpha)):
        res = Mult(i+2, G, a, p)
        ecca.append(res) 
    txt = ""
    for i in range(0, len(text), 4):
        c1 = (text[i], text[i+1])
        c2 = (text[i+2], text[i+3])
        Mp = ECCPQ(c2, Neg(Mult(nb, c1, a, p)), a, p)
        txt += alpha[ecca.index(Mp)]
    return txt

file = open("crypto/lab13Input.txt", "r")
G = eval(file.readline())
a = int(file.readline())
p = int(file.readline())

file = open("crypto/lab13.txt", "r")
text = file.read()
file.close()

res = Encrypt(text, G, a, p)
print(res)
file = open("crypto/lab13_enc.txt", "w")
file.write(str(res))
file.close()


file = open("crypto/lab13_enc.txt", "r")
res = eval(file.read())
file.close()
res = Decrypt(res, G, a, p)
print(res)
file = open("crypto/lab13_dec.txt", "w")
file.write(res)
file.close()
    