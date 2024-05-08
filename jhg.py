a = 13
m = 60

i = 1
num = a
while num != 1:
    bN = num
    num = (i * a) % m
    print(f"{a} * {i} % {m} = {num}")
    i+=1 

print(pow(a, -1, m))