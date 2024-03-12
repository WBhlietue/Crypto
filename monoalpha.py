import random


def Encrypt(text):
    text = text.upper()
    key = []
    for i in range(65, 91):
        key.insert(random.randint(0, len(key)), chr(i))
    targetTxt = ""
    for i in text:
        char = " "
        if(ord(i) >= 65 and ord(i) <= 91):
            char = key[ord(i)-65]
        targetTxt += char
    key ="".join(key)
    return (targetTxt, key)

def Decrypt(text, key):
    targetTxt = ""
    key = [i for i in key]
    for i in text:
        char = " "
        if(ord(i) >= 65 and ord(i) <= 91):
            char = chr(key.index(i) + 65)
        targetTxt += char
    return targetTxt

ans = Encrypt("Unlimited Blade Works")
print(ans[0], ans[1])
print(Decrypt(ans[0], ans[1]))