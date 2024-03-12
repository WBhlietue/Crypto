from EnigmaCreator import Enigma

enigma = Enigma()

# enigma.InitRandom()
# enigma.SaveToFile("enigma.txt")

enigma.ReadFromFile("enigma.txt")



text = "unlimited blade works"
text = enigma.Convert(text)
print(text)
enigma.ToInitRotate()
text = enigma.Convert(text)
print(text)