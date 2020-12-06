import hashlib
inputString = "yzbqklnj"

i = 0
while(True):
    i += 1
    inStringPlusInt = inputString + str(i)
    temp = hashlib.md5(inStringPlusInt.encode())
    temp = temp.hexdigest()
    print(inStringPlusInt, "-", temp, "-", i)
    if temp[0] == '0' and temp[1] == '0' and temp[2] == '0' and temp[3] == '0' and temp[4] == '0':
        print("Numero", i)
        break
i = 0
while(True):
    i += 1
    inStringPlusInt = inputString + str(i)
    temp = hashlib.md5(inStringPlusInt.encode())
    temp = temp.hexdigest()
    print(inStringPlusInt, "-", temp, "-", i)
    if temp[0] == '0' and temp[1] == '0' and temp[2] == '0' and temp[3] == '0' and temp[4] == '0' and temp[5] == '0':
        print("Numero", i)
        break