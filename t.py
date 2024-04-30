n = 192649
s= 101355 
Xi = s*s % n 
a = ""
for i  in range(1, 14): 
    Xi = (Xi)*(Xi) % n 
    Bi = Xi % 2
    print(Bi)
    a += str(Bi)
print(Xi)
print(a)
print(int(a, 2) * Xi)