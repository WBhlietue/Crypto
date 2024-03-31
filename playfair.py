key = "GRAVITYFLSBCDEHKMNOPQUWXZ "
key = key.replace(" ", "")
key = key.upper()


def matric(x, y, initial):
    return [[initial for _ in range(x)] for _ in range(y)]


result = list()
for c in key:
    if c not in result:
        if c == 'J':
            result.append("I")
        else:
            result.append(c)

flag = 0
for i in range(65, 91):
    if (chr(i) not in result):
        if (i == 73 and chr(74) not in result):
            result.append("I")
            flag = 1
        elif flag == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))
k = 0
my_matrix = matric(5, 5, 0)
for i in range(0, 5):
    for j in range(0, 5):
        my_matrix[i][j] = result[k]
        k += 1


def GetMatrixIndex(a, b):
    f = ()
    s = ()
    for i in range(5):
        for j in range(5):
            if (my_matrix[i][j] == a):
                f = (i, j)
            if (my_matrix[i][j] == b):
                s = (i, j)
    return (f, s)


def Encrypt(text):
    text = text.upper()
    text = text.replace(" ", "")
    i = 0
    letterSet = []
    while (i < len(text)):
        if (i == len(text) - 1):
            letterSet.append([text[i], "X"])
            i += 1
            continue
        first = text[i]
        if (first == text[i + 1]):
            letterSet.append([first, "X"])
            i += 1
            continue
        letterSet.append([first, text[i + 1]])
        i += 2
    targetText = ""
    for i in letterSet:
        pos = GetMatrixIndex(i[0], i[1])
        newLetter = ()
        if (pos[0][0] == pos[1][0]):
            newLetter = (my_matrix[pos[0][0]-1][pos[0][1]], my_matrix[pos[1][0]-1][pos[1][1]])
        elif (pos[0][1] == pos[1][1]):
            newLetter = (my_matrix[pos[0][0]][pos[0][1]-1], my_matrix[pos[1][0]][pos[1][1]-1])
        else:
            newLetter = (my_matrix[pos[1][0]][pos[0][1]], my_matrix[pos[0][0]][pos[1][1]])
        targetText += newLetter[0] + newLetter[1]
    return (targetText)


def Decrypt(text):
    text = text.upper()
    text = text.replace(" ", "")
    i = 0
    letterSet = []
    for i in range(0, len(text),2):
        letterSet.append((text[i], text[i+1]))
    targetText = ""
    for i in letterSet:
        pos = GetMatrixIndex(i[0], i[1])
        newLetter = ()
        if (pos[0][0] == pos[1][0]):
            newLetter = (my_matrix[(pos[0][0]+1)%5][pos[0][1]], my_matrix[(pos[1][0]+1) % 5][pos[1][1]])
        elif (pos[0][1] == pos[1][1]):
            newLetter = (my_matrix[pos[0][0]][(pos[0][1]+1)%5], my_matrix[pos[1][0]][(pos[1][1]+1)%5])
        else:
            newLetter = (my_matrix[pos[1][0]][pos[0][1]], my_matrix[pos[0][0]][pos[1][1]])
        
        targetText += newLetter[0] + newLetter[1]
    if(len(targetText) % 2 == 0 and targetText[-1] == "X"):
        targetText = targetText[:len(targetText)-1]
    
    i = 1
    while(i < len(targetText)-1):
        if(targetText[i] == "X" and targetText[i-1] == targetText[i+1]):
            targetText = targetText[:i] + targetText[i+1:]
            i -= 1
        i+=1

    return (targetText)

text = Encrypt("Newspaper")
ans = Decrypt(text)
print(text)
print(ans)


# s u g a b
# c d e f h 
# i k l m n 
# o p q r t 
# v w x y z