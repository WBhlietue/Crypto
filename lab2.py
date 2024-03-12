import math

def GCD(a, b):
    if a % b == 0 or b % a == 0:
        return b
    return GCD(b, a % b)


def EGCD(a, b):
    if a == 0:
        return (b, 0, 1)
    (g, x1, y1) = EGCD(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (g, x, y)

def GetEulerTotient(n):
    num = 1
    for i in range(1, n):
        if GCD(i, n) == 1:
            num += 1
    return num

def GetEulerWithP(n):
    def GetSingle(p):
        return math.pow(p[0], p[1] - 1) * (p[0] - 1)
    res = 1
    for i in n:
        res *= GetSingle(i)
    return int(res)

def CheckIsP(n):
    return GetEulerTotient(n) == n - 1


def ToPrime(n):
    result = []
    i = 2
    while i <= n:
        num = 0
        count = 0
        while n % i == 0:
            num = i
            count += 1
            n /= i
        if num > 0:
            result.append((num, count))
        i += 1

    return result


# for i in range(2, 100):
#     print(i, ":", GetEulerTotient(i))
#     res = ToPrime(i)
#     print(i, ":", GetEulerWithP(res), "\n")

# print(ToPrime(999999999))
# print(GetEulerWithP(ToPrime(264600)))

# print(GCD(12, 18))
# print(EGCD(7, 15))
# print(EGCD(7, 26))
