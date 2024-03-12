import random

def ChangeIndex(value, permute):
    list = [0] * len(value)
    for i in range(len(permute)):
        list[permute[i]] = value[i]
    return list

def GetPermute(length):
    permute = []
    for i in range(length):
        permute.insert(random.randint(0, len(permute)), i)
    return permute
def GenerateKey():
    key = []
    permute = GetPermute(10)
    permute2 = GetPermute(10)
    for _ in range(10):
        key.append(random.randint(0, 1))
    changedKey = ChangeIndex(key, permute)
    print(changedKey)
    r = changedKey[0:5]
    l = changedKey[5:10]
    r.append(r.pop(0))
    l.append(l.pop(0))
    newKey = r + l
    changedNewKey = ChangeIndex(newKey, permute2)[0:8]
    print(changedNewKey)
    r.append(r.pop(0))
    l.append(l.pop(0))
    r.append(r.pop(0))
    l.append(l.pop(0))

    newKey = r + l
    changedNewKey2 = ChangeIndex(newKey, permute2)[0:8]
    print(changedNewKey2)
    return (changedNewKey, changedNewKey2)
def EncrypeChar():
    pass


key = GenerateKey()