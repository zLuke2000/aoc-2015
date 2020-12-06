import os

""" PARTE COMUNE """
f = open((os.path.dirname(__file__) + '\day5_input'), 'r')
temp = f.read()
f.close()
temp = temp.split("\n")

""" PARTE UNO """
corretti = 0
for i in temp:
    valido = False
    for j in range(len(i)-1):
        if i[j] == i[j+1]:
            valido = True
    countVocali = i.count('a') + i.count('e') + i.count('i') + i.count('o') + i.count('u')
    if countVocali < 3:
        valido = False
    if "ab" in i or "cd" in i or "pq" in i or "xy" in i:
        valido = False
    if valido:
        corretti += 1
print("Corretti:", corretti)


""" PARTE UNO """
corretti = 0
for i in temp:
    valido1 = False
    valido2 = False
    for j in range(len(i)-2):
        if i[j] == i[j+2]:
            valido1 = True
    for j in range(len(i)-1):
        testString = i[j]+i[j+1]
        if(i.count(testString) > 1):
            valido2 = True
            break
    if valido1 and valido2:
        corretti += 1
print("Corretti:", corretti)