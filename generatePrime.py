import math
file = open("./crypto/Prime.txt", "w")
def CheckPrime(num):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if(num % i == 0 and i != num):
            return False 
    return True
file.write("2")
for i in range(3, 1000000, 2):
    if (CheckPrime(i)):
        file.write("," + str(i))
file.close