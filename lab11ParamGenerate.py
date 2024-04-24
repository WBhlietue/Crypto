import random
primes = open("./crypto/Prime.txt", "r")
primeNumbers = primes.read().split(",")[:100]
primes.close()

p = random.choice(primeNumbers)
q = random.choice(primeNumbers)
e = random.choice(primeNumbers)

file = open("./crypto/lab11Params.txt", "w")
file.write(str(p) + "\n")
file.write(str(q) + "\n")
file.write(str(e) + "\n")



# 73
# 151
# 11