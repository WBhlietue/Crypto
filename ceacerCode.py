littleLetter = []
for i in range(97, 97 + 26):
    littleLetter.append(chr(i))

bigLetter = []
for i in range(65, 65 + 26):
    bigLetter.append(chr(i))

cryll = [
    "а",
    "б",
    "в",
    "г",
    "д",
    "е",
    "ё",
    "ж",
    "з",
    "и",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "ө",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ү",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ъ",
    "ы",
    "ь",
    "э",
    "ю",
    "я",
]
cryllBig = [
    "а".upper(),
    "б".upper(),
    "в".upper(),
    "г".upper(),
    "д".upper(),
    "е".upper(),
    "ё".upper(),
    "ж".upper(),
    "з".upper(),
    "и".upper(),
    "й".upper(),
    "к".upper(),
    "л".upper(),
    "м".upper(),
    "н".upper(),
    "о".upper(),
    "ө".upper(),
    "п".upper(),
    "р".upper(),
    "с".upper(),
    "т".upper(),
    "у".upper(),
    "ү".upper(),
    "ф".upper(),
    "х".upper(),
    "ц".upper(),
    "ч".upper(),
    "ш".upper(),
    "щ".upper(),
    "ъ".upper(),
    "ы".upper(),
    "ь".upper(),
    "э".upper(),
    "ю".upper(),
    "я".upper(),
]

symbol = [
    ",",
    ".",
    "/",
    ";",
    "'",
    '"',
    "[",
    "]",
    "\\",
    "-",
    "=",
    "<",
    ">",
    "?",
    ":",
    "{",
    "}",
    "|",
    "_",
    "+",
]

letters = (
    littleLetter
    + bigLetter
    + ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    + cryll
    + cryllBig
    + symbol
)

def EnCryptC(str, num):
    newStr = ""
    for i in str:
        if i in letters:
            index = letters.index(i)
            index += num
            index %= len(letters)
            newStr += letters[index]
        else:
            newStr += i
    return newStr


def DeCryptC(str, num):
    newStr = ""
    for i in str:
        if i in letters:
            index = letters.index(i)
            index -= num
            index %= len(letters)
            newStr += letters[index]
        else:
            newStr += i
    return newStr


def EnCryptA(str, num):
    newStr = ""
    for i in str:
        if i in letters:
            index = letters.index(i)
            index *= num
            index %= len(letters)
            newStr += letters[index]
        else:
            newStr += i
    return newStr


def DeCryptA(str, num):
    i = 1
    while ((i * num) % len(letters) != 1):
        i += 1
    num = i
    newStr = ""
    for i in str:
        if i in letters:
            index = letters.index(i)
            index *= num
            index %= len(letters)
            newStr += letters[index]
        else:
            newStr += i
    return newStr



# C
cryptNum = int(input(f"enter Num(1-{len(letters)}): "))

file = open("./crypto/from.txt", "r", encoding="utf-8")
str = file.read()
file.close()
file = open("./crypto/toC.txt", "w", encoding="utf-8")

str = EnCryptC(str, cryptNum)

file.write(str)
file.close()

file = open("./crypto/dC.txt", "w", encoding="utf-8")
file.write(DeCryptC(str, cryptNum))
file.close()


# A

list  = []
for i in range(1, len(letters)):
    if(len(letters) % i == 0):
        list.append(i) 
cryptNum = int(input(f"enter Num(cannot in {list}): "))
while cryptNum in list:
    cryptNum = int(input(f"enter Num(cannot in {list}): "))
file = open("./crypto/from.txt", "r", encoding="utf-8")
str = file.read()
file.close()
file = open("./crypto/toA.txt", "w", encoding="utf-8")

str = EnCryptA(str, cryptNum)

file.write(str)
file.close()

file = open("./crypto/dA.txt", "w", encoding="utf-8")
file.write(DeCryptA(str, cryptNum))
file.close()
