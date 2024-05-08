import lab8
import random
import lab14
import hashlib

file = open("./crypto/lab15Params.txt", "r")
p = int(file.readline().split("=")[1])
q = int(file.readline().split("=")[1])
g = int(file.readline().split("=")[1])
x = random.randrange(0, q)
y = pow(g, x, p)
k = random.randrange(0, q)

# signing
r = pow(g, k, p) % q 
M = b"1234567890"
hh = int(hashlib.sha1(M).hexdigest(), 16)
print(hh)
# hh = lab14.H(M)
k1 = pow(k, -1, q)
s = (k1 * (hh + x * r)) % q

print( s)

# verify
w = pow(s, -1, q)
u1 = (hh * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

print(v)
print(v == s)