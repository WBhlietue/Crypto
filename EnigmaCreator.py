import random


class Rotor:

    def __init__(self) -> None:
        self.keymap = []
        self.initKeyMap = []
        self.letters = [chr(i) for i in range(65, 91)]
        self.list = []

    def InitRandom(self):
        for i in self.letters:
            self.keymap.insert(random.randint(0, len(self.keymap)), i)
        self.initKeyMap = self.keymap.copy()

    def InitConstant(self, keymap):
        self.keymap = keymap
        self.initKeyMap = keymap.copy()

    def Rotate(self, num):
        for _ in range(num):
            a = self.keymap[0]
            self.keymap.remove(a)
            self.keymap.append(a)

    def GetValue(self, key, dir):
        if (key in self.letters):
            if (dir == 1):
                value = self.keymap[self.letters.index(key)]
            else:
                # print(self.keymap.index(key))
                value = self.letters[self.keymap.index(key)]
        else:
            value = key
        return value

    def InitRotate(self):
        self.keymap = self.initKeyMap.copy()


class Reflecter:

    def __init__(self) -> None:
        self.keymap = []
        self.letters = [chr(i) for i in range(65, 91)]

    def InitRandom(self):
        self.list = []
        for i in self.letters:
            self.list.insert(random.randint(0, len(self.keymap)), i)
        self.keymap = []
        for i in range(13):
            self.keymap.append([self.list[i], self.list[i + 13]])

    def InitConstant(self, keymap):
        self.list = keymap
        self.keymap = []
        for i in range(13):
            self.keymap.append([self.list[i], self.list[i + 13]])
        

    def GetValue(self, key):
        if key in self.letters:
            for i in self.keymap:
                if (key in i):
                    if i[0] == key:
                        value = i[1]
                    else:
                        value = i[0]
        else:
            value = key
        return value


class Enigma:

    def __init__(self) -> None:
        self.rotor1 = Rotor()
        self.rotor2 = Rotor()
        self.rotor3 = Rotor()
        self.rotate = []
        self.reflect = Reflecter()
        self.rotor1Rotate = 0
        self.rotor2Rotate = 0
        pass

    def InitRandom(self):
        self.rotor1.InitRandom()
        self.rotor2.InitRandom()
        self.rotor3.InitRandom()
        self.reflect.InitRandom()
        self.Rotate([
            random.randint(0, 25),
            random.randint(0, 25),
            random.randint(0, 25)
        ])

    def GetValue(self, key):
        r = self.rotor1.GetValue(key, 1)
        r = self.rotor2.GetValue(r, 1)
        r = self.rotor3.GetValue(r, 1)
        r = self.reflect.GetValue(r)
        r = self.rotor3.GetValue(r, 0)
        r = self.rotor2.GetValue(r, 0)
        r = self.rotor1.GetValue(r, 0)
        self.rotor1Rotate += 1
        self.rotor1.Rotate(1)
        if (self.rotor1Rotate == 26):
            self.rotor1Rotate = 0
            self.rotor2Rotate += 1
            self.rotor2.Rotate(1)
            if (self.rotor2Rotate == 26):
                self.rotor2Rotate = 0
                self.rotor3.Rotate(1)
        return r

    def InitRotate(self):
        self.rotor1Rotate = 0
        self.rotor2Rotate = 0
        self.rotor1.InitRotate()
        self.rotor2.InitRotate()
        self.rotor3.InitRotate()
    def ToInitRotate(self):
        self.InitRotate()
        self.Rotate(self.rotate)

    def Rotate(self, value):
        self.rotate = value
        self.rotor1.Rotate(value[0])
        self.rotor2.Rotate(value[1])
        self.rotor3.Rotate(value[2])

    def SaveToFile(self, name):
        file = open(name, "w")
        rotor1 = "".join(self.rotor1.keymap) + "\n"
        rotor2 = "".join(self.rotor2.keymap) + "\n"
        rotor3 = "".join(self.rotor3.keymap) + "\n"
        reflect = "".join(self.reflect.list) + "\n"
        rotate = str(self.rotate[0]) + "," + str(self.rotate[1]) + "," + str(
            self.rotate[2])
        file.write(rotor1)
        file.write(rotor2)
        file.write(rotor3)
        file.write(reflect)
        file.write(rotate)

    def ReadFromFile(self, name):
        file = open(name, "r")
        line = file.readlines()
        rotor1 = line[0]
        rotor2 = line[1]
        rotor3 = line[2]
        reflect = line[3]
        rotate = line[4]
        rotor1 = [i for i in rotor1]
        rotor2 = [i for i in rotor2]
        rotor3 = [i for i in rotor3]
        reflect = [i for i in reflect]
        rotor1.pop()
        rotor2.pop()
        rotor3.pop()
        reflect.pop()
        rotate = rotate.split(",")
        rotate = [int(i) for i in rotate]
        self.rotor1.InitConstant(rotor1)
        self.rotor2.InitConstant(rotor2)
        self.rotor3.InitConstant(rotor3)
        self.reflect.InitConstant(reflect)
        self.Rotate(rotate)
    def Convert(self, text):
        text = text.upper()
        t = ""
        for i in text:
            t += self.GetValue(i)
        return t