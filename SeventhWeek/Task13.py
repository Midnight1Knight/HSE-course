def fromSeven(number):
    return number[2:]


def fronEight(number):
    return number[1:]


def filt(number):
    for i in badChars:
        if i in number:
            number = number.replace(i, '')
    return number


def isntKode(number):
    number = '495' + number
    return number


inFile = open('input.txt')
inNumber = inFile.readline()
badChars = ['(', ')', '\n', '-']
inNumber = filt(inNumber)
if inNumber[0:2] == '+7':
    inNumber = fromSeven(inNumber)
if inNumber[0:1] == '8' and len(inNumber) == 11:
    inNumber = fronEight(inNumber)
if len(inNumber) < 10:
    inNumber = isntKode(inNumber)
for line in inFile:
    line = filt(line)
    if line[0:2] == '+7':
        line = fromSeven(line)
    elif line[0:1] == '8' and len(line) == 11:
        line = fronEight(line)
    elif (len(line) < 10) and (len(line) > 6):
        line = isntKode(line)
    if line == inNumber:
        print('YES')
    else:
        print('NO')
inFile.close()
