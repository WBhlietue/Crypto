letters = [chr(i) for i in range(65, 91)]
table = []

for i in range(26):
    l = letters
    a = i
    while (a > 0):
        f = l[0]
        l = l[1:26]
        l.append(f)
        a -= 1
    table.append(l)


def Encrypt(text, key):
    if (len(text) != len(key)):
        return None
    targetText = ""
    for i in range(len(text)):
        target = (letters.index(text[i]), letters.index(key[i]))
        # print(target, table[11])
        targetText += table[target[1]][target[0]]
    return (targetText)


def Decrypt(text, key):
    if (len(text) != len(key)):
        return None
    targetText = ""
    for i in range(len(key)):
        target = table[letters.index(key[i])]
        num = target.index(text[i])
        targetText += letters[num]
    return (targetText)


key = "ATTACKONTITANENDING"
cr = Encrypt("UNLIMITEDBLADEWORKS", key)
res = Decrypt(cr, key)

print(cr)
print(res)