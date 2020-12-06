import os

""" PARTE COMUNE """
f = open((os.path.dirname(__file__) + '\day3_input'), 'r')
temp = f.read()
f.close()
temp = temp.split("\n")

""" PARTE UNO """
x,y = 0,0
casaXY_1 = []
temp = str(temp[0])
tuplaXY = (x,y)
casaXY_1.append(tuplaXY)
for i in temp:
    if i == '^':
        y += 1
    elif i == 'v':
        y -= 1
    elif i == '>':
        x += 1
    elif i == '<':
        x -= 1
    tuplaXY = (x,y)
    if tuplaXY not in casaXY_1:
        casaXY_1.append(tuplaXY)
print("Num case:",len(casaXY_1))

""" PARTE UNO """
Bx, By, Rx, Ry = 0,0,0,0
casaXY_2 = []
BabboXY = (x,y)
RoboXY = (x,y)
index = 0
for i in temp:
    if index%2 == 0:
        if i == '^':
            By += 1
        elif i == 'v':
            By -= 1
        elif i == '>':
            Bx += 1
        elif i == '<':
            Bx -= 1
        BabboXY = (Bx,By)
        if BabboXY not in casaXY_2:
            casaXY_2.append(BabboXY)
    else:
        if i == '^':
            Ry += 1
        elif i == 'v':
            Ry -= 1
        elif i == '>':
            Rx += 1
        elif i == '<':
            Rx -= 1
        RoboXY = (Rx,Ry)
        if RoboXY not in casaXY_2:
            casaXY_2.append(RoboXY)
    index += 1
print("Num case:",len(casaXY_2))
