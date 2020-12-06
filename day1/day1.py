import os

""" PARTE COMUNE """
f = open((os.path.dirname(__file__) + '\day1_input'), 'r')
temp = f.read()
f.close()

""" PARTE UNO """
upCount = temp.count('(')
downCount = temp.count(')')
print("Piano:", upCount-downCount)

""" PARTE DUE """
tempSep = list(temp)
floor = 0
count = 0
for i in temp:
    if(i == '('):
        floor += 1
        count += 1
    if(i == ')'):
        floor -= 1
        count += 1
    if(floor == -1):
        print("Piano:", str(floor), "Step:", str(count))
        break