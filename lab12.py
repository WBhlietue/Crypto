# Diffie Hellman 6 or 5,  20 oron, prime
# elgamal
# txt file
# sanamsargu aes


#sympy

import lab3
import lab10
import lab11

class Person:
    def __init__(self, name, p, a):
        self.name = name
        self.x = 0
        self.y = 0
        self.p = p
        self.a = a
        self.k = 0
    def GeneratePublicKey(self):
        x = int(lab10.RandomNumberCTR(), 16) % self.p
        y = pow(self.a, x, self.p)
        self.x = x
        self.y = y
        return y

    def GenerateSecretKey(self, y ):
        self.k = pow(y, self.x, self.p)
        return self.k



primeNum = 257
root = lab3.PrimitiveRoot(primeNum)
a = root[int(lab10.RandomNumberCTR(), 16) % len(root)]
bob = Person("Bob", primeNum, a)
alice = Person("Alice", primeNum, a)

bobK = bob.GeneratePublicKey()
aliceK = alice.GeneratePublicKey()

def CheckK():
    

    print(f"Bob's public key: {bobK}")
    print(f"Alice's public key: {aliceK}")

    bobS = alice.GenerateSecretKey(bobK)
    aliceS = bob.GenerateSecretKey(aliceK)
    print(f"Alice's secret key: {bobS}")
    print(f"Bob's secret key: {aliceS}")


def ElgamalEncrypt(text, y, p, a):
    s = ""
    for i in text:
        p = 31
        a =3
        y = 25
        m = 14
        k = 7
        K = pow(y, k, p)
        c1 = pow(a, k, p)
        c2 = (m*K)%p
        print(i, (c2))
        s += str(c1) + "," + str(c2) + ","
    return s[:-1]
def ElgamalDecrypt(text, p, x):
    CT = text.split(",")
    txt = ""
    for i in range(0, len(CT), 2):
        c1 = int(CT[i], 10)
        c2 = int(CT[i+1], 10)
        K = pow(c1, x, p)
        k = lab11.ModInverse(K, p)
        m = (c2 * k)%p
        txt += chr(m)
    return txt


CheckK()
file = open("./crypto/lab12Text.txt", "r")
prime = int(file.readline())
root=lab3.PrimitiveRoot(prime)
a = root[int(lab10.RandomNumberCTR(), 16) % len(root)]
x = int(lab10.RandomNumberCTR(), 16) % prime
y = pow(a, x, prime)
plainText = file.read()

file.close()
encrypt = ElgamalEncrypt(plainText, y, prime, a)
file = open("./crypto/lab12Encrypt.txt", "w")
file.write(str(prime) +","+str(x)+ "\n")
file.write(encrypt)
file.close()




file = open("./crypto/lab12Encrypt.txt", "r")
prime = file.readline()
x = int(prime.split(",")[1])
prime = int(prime.split(",")[0])
encrypt = file.readline()
file.close()
decrypt = ElgamalDecrypt(encrypt, prime, x)
file = open("./crypto/lab12Decrypt.txt", "w")
file.write(decrypt)
file.close()