import math
import random
import sympy
def IsPrime(n, k=500):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


Ls = []
for i in range(512, 1025):
    if(i % 64 == 0):
        Ls.append(i)
print(Ls)   
L = 512
p = 0
a = 0
ps = []
nMin = int(math.pow(2, L-1))+1
nMax = int(math.pow(2, L))
for i in range(nMin, nMax):
    a += 1
    if(IsPrime(i)):
        p = int(i)
        break

p1 = p - 1
file = open("./crypto/lab15Params.txt", "w")
# divs = factors(p1)
divs = sympy.factorint(p1)
# print(divs)
q = list(divs.keys())[-1]
print(q)
h = random.randrange(0, p)
g = pow(h, (p-1)//q, int(p))
file.write("p=" + str(p) + "\n")
file.write("g=" + str(g) + "\n")
file.write("q=" + str(q) + "\n")


# pow random 2iig solino