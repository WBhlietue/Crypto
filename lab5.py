# vernum
# rotormashine
# railfence

import random

letters = [chr(i) for i in range(65, 91)] + [",", ".", "/", ";", "'", "?"]


def VernumEncrypt(text):
    text = text.upper()
    key = ''.join(
        random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(len(text)))
    str = ""
    for i in range(len(text)):
        a = letters.index(text[i])
        b = letters.index(key[i])
        c = letters[(a ^ b)]
        str += c
    return str, key


def VernumDecrypt(text, key):
    text = text.upper()
    key = key.upper()
    str = ""
    for i in range(len(text)):
        a = letters.index(text[i])
        b = letters.index(key[i])
        c = letters[a ^ b]
        str += c
    return str


def RailFenceEncrypt(text, key):
    table = [["" for _ in (text)] for _ in range(key)]
    x = 0
    y = 0
    rev = 0
    for i in text:
        table[y][x] = i
        x += 1
        if (rev == 0):
            y += 1
            if (y == key - 1):
                rev = 1
        else:
            y -= 1
            if (y == 0):
                rev = 0
    targetText = ""
    for i in table:
        targetText += "".join(i)
    for i in table:
        print(i)
    return targetText


def RailFenceDecrypt(text, key):
    num = key * 2 - 3
    table = [["" for _ in (text)] for _ in range(key)]
    current = 0
    for i in range(key):
        x = i
        pre = 0
        plusNum = num - 2 * i + 1
        plusNum2 = num - plusNum + 1
        if (i == 0 or i == key - 1):
            plusNum2 = num + 1
            plusNum = num + 1
        for j in range(current, len(text)):
            current = j
            if (x >= len(text)):
                break
            table[i][x] = text[j]
            if (pre == 0):
                x += plusNum
                pre = 1
            else:
                x += plusNum2
                pre = 0
        # break
    for i in table:
        print(i)
    x = 0
    y = 0
    rev = 0
    str = ''
    for i in text:
        str += table[y][x]
        x += 1
        if (rev == 0):
            y += 1
            if (y == key - 1):
                rev = 1
        else:
            y -= 1
            if (y == 0):
                rev = 0
    return str


# a*2-3

s = RailFenceEncrypt("unlimited Blade Works", 6)
print("\n")
print(s)
r = RailFenceDecrypt(s, 6)
print(r)

# s, key = VernumEncrypt("unlimitedBladeWOrks")
# print(s, key)
# print(VernumDecrypt(s, key))