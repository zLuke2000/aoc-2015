import os

""" PARTE COMUNE """
f = open((os.path.dirname(__file__) + '\day2_input'), 'r')
temp = f.read()
f.close()
temp = temp.split("\n")

""" PARTE UNO """
dim = [0,0,0]
area = 0
for  i in temp:
    i = i.split('x')
    l = int(i[0])
    w = int(i[1])
    h = int(i[2])
    area += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
print("Totale:", area)

""" PARTE DUE """
area = 0
for  i in temp:
    i = i.split('x')
    l = int(i[0])
    w = int(i[1])
    h = int(i[2])
    area += 2*min(l+w, w+h, h+l) + (w*h*l)
print("Totale:", area)